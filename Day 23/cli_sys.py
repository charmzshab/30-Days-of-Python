
import sys

if __name__ == "__main__":
#     print(sys.argv)
    try:
        name = sys.argv[1] #uses positional arguments
        pwd =""
        print(name, pwd)
    except:
        name = input("What's your name?\n")
        from getpass import getpass
        pwd = getpass("Type password\n")
        print(name, pwd)
