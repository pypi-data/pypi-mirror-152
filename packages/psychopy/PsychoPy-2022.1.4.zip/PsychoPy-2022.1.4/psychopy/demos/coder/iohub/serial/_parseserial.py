# Contains the custom serial parsing function that is used by
# the customparser.py demo script.

# IMPORTANT: Remember that this code will be called from the iohub server
# process, not the psychopy experiment process.
# When code is running in the ioHub Server Process, you can have text printed
# to the experiment process stderr by using the iohub 'print2err' function.
# Do not use the standard 'print' call, as it will do nothing except maybe make
# the iohub server not start.
from psychopy.iohub import print2err

def checkForSerialEvents(read_time, rx_data, parser_state, **kwargs):
    """
    Must have the following signature:

    evt_list = someCustomParserName(read_time, rx_data, parser_state, **kwargs)

    where:
        read_time: The time when the serial device read() returned
                with the new rx_data.
        rx_data: The new serial data received. Any buffering of data
                across function calls must be done by the function
                logic itself. parser_state could be used to hold
                such a buffer if needed.
        parser_state: A dict which can be used by the function to
                store any values that need to be accessed
                across multiple calls to the function. The dict
                is initially empty.
        kwargs: The parser_kwargs preference dict read from
                the event_parser preferences; or an empty dict if
                parser_kwargs was not found.

    If events should be generated by iohub, the function must return a
    list like object, used to provide ioHub with any new serial events that
    have been found. Each element of the list must be a dict like object,
    representing a single serial device event found by the parsing function.
    An event dict can contain the following key, value pairs:
       data: The string containing the parsed event data. (REQUIRED)
       time: The timestamp for the event (Optional). If not provided,
             the return time of the latest serial.read() is used.

    If the function has detected no serial events, an empty list or None
    can be returned.

    :return: list of ioHub serial device events found. None == [] here.
    """
    print2err("checkForSerialEvents called: ", (read_time, rx_data, parser_state, kwargs))
    parser_state['last_time'] = read_time

    serial_events = []
    if rx_data:
        serial_events.append({'data': rx_data})
    return serial_events