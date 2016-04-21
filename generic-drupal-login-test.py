from locust import HttpLocust, TaskSet, task
import random
from pyquery import PyQuery

class UserBehavior(TaskSet):
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled
        self.login()

    def login(self):
        # login function using http session handler
        self.client.post("/user/login", {"name":"username", "pass":"userpass", "form_id": "user_login", "op": "Log in"})

    def index_page(self):
        # login function using http session handler. it gets the index "/"
        # url and parses the HTML for href tags. The href's are stored for
        # later use. To Do: Pass a page or path argument to parse pages other
        # than "/". -EHM
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq("a")
        self.urls_on_current_page = []
        for l in link_elements:
          if "href" in l.attrib:
            if l.attrib["href"] <> "/user/logout":
                self.urls_on_current_page.append(l.attrib["href"])

    @task(30)
    def load_page(self):
        self.index_page()
        url = random.choice(self.urls_on_current_page)
        print "Calling "+url
        r = self.client.get(url)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
