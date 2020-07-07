from datetime import datetime
from formatting import format_msg


def send(name, website=None):
    if website != None:
        msg = format_msg(name=name, website=website)
    else:
        msg = format_msg(name=name)

    # send the message

    return msg
