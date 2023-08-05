#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Part of the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""Experiment classes:
    Experiment, Flow, Routine, Param, Loop*, *Handlers, and NameSpace

The code that writes out a *_lastrun.py experiment file is (in order):
    experiment.Experiment.writeScript() - starts things off, calls other parts
    settings.SettingsComponent.writeStartCode()
    experiment.Flow.writeBody()
        which will call the .writeBody() methods from each component
    settings.SettingsComponent.writeEndCode()
"""
from xml.etree.ElementTree import Element

import re
from pathlib import Path

from psychopy import logging
from . import utils
from . import py2js

from ..colors import Color
from numpy import ndarray
from ..alerts import alert


def _findParam(name, node):
    """Searches an XML node in search of a particular param name

    :param name: str indicating the name of the attribute
    :param node: xml element/node to be searched
    :return: None, or a parameter child node
    """
    for attr in node:
        if attr.get('name') == name:
            return attr

inputDefaults = {
    'str': 'single',
    'code': 'single',
    'num': 'single',
    'bool': 'bool',
    'list': 'single',
    'file': 'file',
    'color': 'color',
}

# These are parameters which once existed but are no longer needed, so inclusion in this list will silence any "future
# version" warnings
legacyParams = [
    'lineColorSpace', 'borderColorSpace', 'fillColorSpace', 'foreColorSpace',  # 2021.1, we standardised colorSpace to be object-wide rather than param-specific
]

class Param():
    r"""Defines parameters for Experiment Components
    A string representation of the parameter will depend on the valType:

    >>> print(Param(val=[3,4], valType='num'))
    asarray([3, 4])
    >>> print(Param(val=3, valType='num')) # num converts int to float
    3.0
    >>> print(Param(val=3, valType='str') # str keeps as int, converts to code
    3
    >>> print(Param(val='3', valType='str')) # ... and keeps str as str
    '3'
    >>> print(Param(val=[3,4], valType='str')) # val is <type 'list'> -> code
    [3, 4]
    >>> print(Param(val='[3,4]', valType='str'))
    '[3,4]'
    >>> print(Param(val=[3,4], valType='code'))
    [3, 4]
    >>> print(Param(val='"yes", "no"', valType='list'))
    ["yes", "no"]

    >>> #### auto str -> code:  at least one non-escaped '$' triggers
    >>> print(Param('[x,y]','str')) # str normally returns string
    '[x,y]'
    >>> print(Param('$[x,y]','str')) # code, as triggered by $
    [x,y]
    >>> print(Param('[$x,$y]','str')) # code, redundant $ ok, cleaned up
    [x,y]
    >>> print(Param('[$x,y]','str')) # code, a $ anywhere means code
    [x,y]
    >>> print(Param('[x,y]$','str')) # ... even at the end
    [x,y]
    >>> print(Param('[x,\$y]','str')) # string, because the only $ is escaped
    '[x,$y]'
    >>> print(Param('[x,\ $y]','str')) # improper escape -> code
    [x,\ y]
    >>> print(Param('/$[x,y]','str')) # improper escape -> code
    /[x,y]
    >>> print(Param('[\$x,$y]','str')) # code, python syntax error
    [$x,y]
    >>> print(Param('["\$x",$y]','str') # ... python syntax ok
    ["$x",y]
    >>> print(Param("'$a'",'str')) # code, with the code being a string
    'a'
    >>> print(Param("'\$a'",'str')) # str, with the str containing a str
    "'$a'"
    >>> print(Param('$$$$$myPathologicalVa$$$$$rName','str'))
    myPathologicalVarName
    >>> print(Param('\$$$$$myPathologicalVa$$$$$rName','str'))
    $myPathologicalVarName
    >>> print(Param('$$$$\$myPathologicalVa$$$$$rName','str'))
    $myPathologicalVarName
    >>> print(Param('$$$$\$$$myPathologicalVa$$$\$$$rName','str'))
    $myPathologicalVa$rName
    """

    def __init__(self, val, valType, inputType=None, allowedVals=None, allowedTypes=None,
                 hint="", label="", updates=None, allowedUpdates=None,
                 allowedLabels=None, direct=True,
                 canBePath=True,
                 categ="Basic"):
        """
        @param val: the value for this parameter
        @type val: any
        @param valType: the type of this parameter ('num', 'str', 'code')
        @type valType: string
        @param allowedVals: possible vals for this param
            (e.g. units param can only be 'norm','pix',...)
        @type allowedVals: any
        @param allowedTypes: if other types are allowed then this is
            the possible types this parameter can have
            (e.g. rgb can be 'red' or [1,0,1])
        @type allowedTypes: list
        @param hint: describe this parameter for the user
        @type hint: string
        @param updates: how often does this parameter update
            ('experiment', 'routine', 'set every frame')
        @type updates: string
        @param allowedUpdates: conceivable updates for this param
            [None, 'routine', 'set every frame']
        @type allowedUpdates: list
        @param categ: category for this parameter
            will populate tabs in Component Dlg
        @type allowedUpdates: string
        @param canBePath: is it possible for this parameter to be
            a path? If so, writing as str will check for pathlike
            characters and sanitise if needed.
        @type canBePath: bool
        @param direct: purely used in the test suite, marks whether this
        param's value is expected to appear in the script
        @type direct: bool
        """
        super(Param, self).__init__()
        self.label = label
        self.val = val
        self.valType = valType
        self.allowedTypes = allowedTypes or []
        self.hint = hint
        self.updates = updates
        self.allowedUpdates = allowedUpdates
        self.allowedVals = allowedVals or []
        self.allowedLabels = allowedLabels or []
        self.staticUpdater = None
        self.categ = categ
        self.readOnly = False
        self.codeWanted = False
        self.canBePath = canBePath
        self.direct = direct
        if inputType:
            self.inputType = inputType
        elif valType in inputDefaults:
            self.inputType = inputDefaults[valType]
        else:
            self.inputType = "String"

    def __str__(self):
        if self.valType == 'num':
            if self.val in [None, ""]:
                return "None"
            try:
                # will work if it can be represented as a float
                return "{}".format(float(self.val))
            except Exception:  # might be an array
                return "%s" % self.val
        elif self.valType == 'int':
            try:
                return "%i" % self.val  # int and float -> str(int)
            except TypeError:
                return "%s" % self.val  # try array of float instead?
        elif self.valType in ['extendedStr','str', 'file', 'table']:
            # at least 1 non-escaped '$' anywhere --> code wanted
            # return str if code wanted
            # return repr if str wanted; this neatly handles "it's" and 'He
            # says "hello"'
            val = self.val
            if isinstance(self.val, str):
                valid, val = self.dollarSyntax()
                if self.codeWanted and valid:
                    # If code is wanted, return code (translated to JS if needed)
                    if utils.scriptTarget == 'PsychoJS':
                        valJS = py2js.expression2js(val)
                        if self.val != valJS:
                            logging.debug("Rewriting with py2js: {} -> {}".format(self.val, valJS))
                        return valJS
                    else:
                        return val
                else:
                    # If str is wanted, return literal
                    if utils.scriptTarget != 'PsychoPy':
                        if val.startswith("u'") or val.startswith('u"'):
                            # if target is python2.x then unicode will be u'something'
                            # but for other targets that will raise an annoying error
                            val = val[1:]
                    # If param is a path or pathlike use Path to make sure it's valid (with / not \)
                    isPathLike = bool(re.findall(r"[\\/](?!\W)", val))
                    if self.valType in ['file', 'table'] or (isPathLike and self.canBePath):
                        val = val.replace("\\\\", "/")
                        val = val.replace("\\", "/")
                    # Hide escape char on escaped $ (other escaped chars are handled by wx but $ is unique to us)
                    val = re.sub(r"\\\$", "$", val)
                    # Replace line breaks with escaped line break character
                    val = re.sub("\n", "\\n", val)
                    return repr(val)
            return repr(self.val)
        elif self.valType in ['code', 'extendedCode']:
            isStr = isinstance(self.val, str)
            if isStr and self.val.startswith("$"):
                # a $ in a code parameter is unnecessary so remove it
                val = "%s" % self.val[1:]
            elif isStr and self.val.startswith(r"\$"):
                # the user actually wanted just the $
                val = "%s" % self.val[1:]
            elif isStr:
                val = "%s" % self.val
            else:  # if val was a tuple it needs converting to a string first
                val = "%s" % repr(self.val)
            if utils.scriptTarget == "PsychoJS":
                if self.valType == 'code':
                    valJS = py2js.expression2js(val)
                elif self.valType == 'extendedCode':
                    valJS = py2js.snippet2js(val)
                if val != valJS:
                    logging.debug("Rewriting with py2js: {} -> {}".format(val, valJS))
                return valJS
            else:
                return val
        elif self.valType == 'color':
            _, val = self.dollarSyntax()
            if self.codeWanted:
                # Handle code
                return val
            elif "," in val:
                # Handle lists (e.g. RGB, HSV, etc.)
                val = toList(val)
                return "{}".format(val)
            else:
                # Otherwise, treat as string
                return repr(val)
        elif self.valType == 'list':
            valid, val = self.dollarSyntax()
            val = toList(val)
            return "{}".format(val)
        elif self.valType == 'fixedList':
            return "{}".format(self.val)
        elif self.valType == 'fileList':
            return "{}".format(self.val)
        elif self.valType == 'bool':
            if utils.scriptTarget == "PsychoJS":
                return ("%s" % self.val).lower()  # make True -> "true"
            else:
                return "%s" % self.val
        elif self.valType == "table":
            return "%s" % self.val
        elif self.valType == "color":
            if re.match(r"\$", self.val):
                return self.val.strip('$')
            else:
                return f"\"{self.val}\""
        else:
            raise TypeError("Can't represent a Param of type %s" %
                            self.valType)

    def __repr__(self):
        return f"<Param: val={self.val}, valType={self.valType}>"

    def __eq__(self, other):
        """Test for equivalence is needed for Params because what really
        typically want to test is whether the val is the same
        """
        return self.val == other

    def __ne__(self, other):
        """Test for (non)equivalence is needed for Params because what really
        typically want to test is whether the val is the same/different
        """
        return self.val != other

    def __bool__(self):
        """Return a bool, so we can do `if thisParam`
        rather than `if thisParam.val`"""
        if self.val in ['True', 'true', 'TRUE', True, 1, 1.0]:
            # Return True for aliases of True
            return True
        if self.val in ['False', 'false', 'FALSE', False, 0, 0.0]:
            # Return False for aliases of False
            return False
        # If not a clear alias, use bool method of value
        return bool(self.val)

    @property
    def _xml(self):
        # Make root element
        element = Element('Param')
        # Assign values
        if hasattr(self, 'val'):
            element.set('val', u"{}".format(self.val).replace("\n", "&#10;"))
        if hasattr(self, 'valType'):
            element.set('valType', self.valType)
        if hasattr(self, 'updates'):
            element.set('updates', "{}".format(self.updates))

        return element

    def dollarSyntax(self):
        """
        Interpret string according to dollar syntax, return:
        1: Whether syntax is valid (True/False)
        2: Whether code is wanted (True/False)
        3: The value, stripped of any unnecessary $
        """
        val = self.val
        if self.valType in ['extendedStr','str', 'file', 'table', 'color', 'list']:
            # How to handle dollar signs in a string param
            self.codeWanted = str(val).startswith("$")

            if not re.search(r"\$", str(val)):
                # Return if there are no $
                return True, val
            if self.codeWanted:
                # If value begins with an unescaped $, remove the first char and treat the rest as code
                val = val[1:]
                inComment = "".join(re.findall(r"\#.*", val))
                inQuotes = "".join(re.findall("[\'\"][^\"|^\']*[\'\"]", val))
                if not re.findall(r"\$", val):
                    # Return if there are no further dollar signs
                    return True, val
                if len(re.findall(r"\$", val)) == len(re.findall(r"\$", inComment)):
                    # Return if all $ are commented out
                    return True, val
                if len(re.findall(r"\$", val)) - len(re.findall(r"\$", inComment)) == len(re.findall(r"\$", inQuotes)):
                    # Return if all non-commended $ are in strings
                    return True, val
            else:
                # If value does not begin with an unescaped $, treat it as a string
                if not re.findall(r"(?<!\\)\$", val):
                    # Return if all $ are escaped (\$)
                    return True, val
        else:
            # If valType does not interact with $, return True
            return True, val
        # Return false if method has not returned yet
        return False, val

    __nonzero__ = __bool__  # for python2 compatibility


def getCodeFromParamStr(val, target=None):
    """Convert a Param.val string to its intended python code
    (as triggered by special char $)
    """
    # Substitute target
    if target is None:
        target = utils.scriptTarget
    # remove leading $, if any
    tmp = re.sub(r"^(\$)+", '', val)
    # remove all nonescaped $, squash $$$$$
    tmp2 = re.sub(r"([^\\])(\$)+", r"\1", tmp)
    out = re.sub(r"[\\]\$", '$', tmp2)  # remove \ from all \$
    if target == 'PsychoJS':
        out = py2js.expression2js(out)
    return out if out else ''


def toList(val):
    """

    Parameters
    ----------
    val

    Returns
    -------
    A list of entries in the string value
    """
    if isinstance(val, (list, tuple, ndarray)):
        return val  # already a list. Nothing to do
    if isinstance(val, (int, float)):
        return [val]  # single value, just needs putting in a cell
    # we really just need to check if they need parentheses
    stripped = val.strip()
    if utils.scriptTarget == "PsychoJS":
        return py2js.expression2js(stripped)
    elif (stripped.startswith('(') and stripped.endswith(')')) or (stripped.startswith('[') and stripped.endswith(']')):
        return stripped
    elif utils.valid_var_re.fullmatch(stripped):
        return "{}".format(stripped)
    else:
        return "[{}]".format(stripped)
