
from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task(1)
    def task01(self):
      import time
      ts = int(time.time())

      self.client.post("/form/data", {
          "first_name": "mytest_first",
          "last_name": "mytest_last_"+ts,
          "email":"tester1@testemaildomain.com",
          "organization": "Test Org",
          "country": "US",
          "state": "CA",
          "zip": "09384",
          "phone": "1-999-999-9999"
      })

class WebsiteUser(HttpLocust):
    host = "https://test.domain.com"
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 2000
