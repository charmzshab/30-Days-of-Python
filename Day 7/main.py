def my_print(txt):
    print(txt)


msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us
"""


def format_msg(name, website):
    msg = msg_template.format(name=name, website=website)
    # print(msg)
    return msg


# format_msg(name="Shaban", website="cfe.sh")


def base_function(*args, **kwargs):
    print(args, kwargs)
