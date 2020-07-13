msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us
"""


def format_msg(name="Shaban", website="cfe.sh"):
    msg = msg_template.format(name=name, website=website)
    # print(msg)
    return msg
