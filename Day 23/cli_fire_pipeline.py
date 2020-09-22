from getpass import getpass
import fire

class Auth(object):
    def login(self,username=None):
        if username == None:
            username = input("Username: ")
        if username == None:
            print("Username is required")
        pwd = getpass("Type password: ")
        return username,pwd

def login(self,username=None):
        if username == None:
            username = input("Username: ")
        if username == None:
            print("Username is required")
        pwd = getpass("Type password: ")
        return username,pwd

def scrape_tag(tag="machine-learning",query_filter="Votes",max_pages=50,pagesize=25):
    base_url = "https://stackoverflow.com/tags/"
    datas = []
    for p in range(max_pages):
        page_num = p + 1
        url = f"{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}"
        #print(url)
        datas.append(url)
    return datas

class Pipeline(object):
    def __init__(self):
        self.scrape = scrape_tag
        self.auth = Auth()
        self.login = login

if __name__ == "__main__":
     fire.Fire(Pipeline)
