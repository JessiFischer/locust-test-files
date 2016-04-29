from locust import HttpLocust, TaskSet, task
import random
from pyquery import PyQuery

class UserBehavior(TaskSet):

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
                self.urls_on_current_page.append(l.attrib["href"])

    @task(30)
    def load_page(self):
        self.index_page()
        url = random.choice(self.urls_on_current_page)
        print "Calling "+url
        r = self.client.get(url)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=500
    max_wait=2000
