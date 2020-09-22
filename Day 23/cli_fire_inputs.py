from getpass import getpass
import fire

def hello(name='World'):
    return f"Hello {name}"

def login(name=None):
    if name == None:
        name = input("What's your name?\n")
    pwd = getpass("Type password\n")
    return name,pwd
if __name__ == "__main__":
     fire.Fire(login)
