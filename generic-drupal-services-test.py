from locust import HttpLocust, TaskSet, task
import random
from pyquery import PyQuery

class ApiCalls(TaskSet):
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled
        self.login()

    def login(self):
        # login function using http session handler
        self.client.post("/user", {"include":"group_membership_type",  "name":"BCNegOUwDLQwv281D4ECzXqWlda2XlQNsBZiEHQTxNw3SPyX7iafW/IZh1N0T9WgGQ1yHeovk9hwDhxmv+aSzIzmKh+wi/BkrJwhDo/YrgaHAiM4gz/nhf+XQf8u4WExXWI1ED3wOXRBoDpUZpb00dTKDFxmJHL9QrKS7ziuOvc=", "pass":"Use3bOqIXkgt70P5Y+WrNRAL5FohuLsW9H/A8zXWITV9HTqynMAwFdSjOyYyCR6aDqqOTzYUpnTvbws6gtwi2Vuc+6MIykPPW6VGVxy1TXwH0p8dTFrQNiNj5QyCYhE4cyLuvu/LTASIXdrXpwVXnlcKR3ahO4wi45NfmM/JIz4="})


    # Module Request
    @task(10)
    def module_request(self):
        # http://test-cae-lms.pantheonsite.io/api/v1.0/course/267?include=modules,training_type,training_program,training_aircraft
        self.client.post("/api/v1.0/course/267", {"include":"modules,training_type,training_program,training_aircraft",  "name":"BCNegOUwDLQwv281D4ECzXqWlda2XlQNsBZiEHQTxNw3SPyX7iafW/IZh1N0T9WgGQ1yHeovk9hwDhxmv+aSzIzmKh+wi/BkrJwhDo/YrgaHAiM4gz/nhf+XQf8u4WExXWI1ED3wOXRBoDpUZpb00dTKDFxmJHL9QrKS7ziuOvc=", "pass":"Use3bOqIXkgt70P5Y+WrNRAL5FohuLsW9H/A8zXWITV9HTqynMAwFdSjOyYyCR6aDqqOTzYUpnTvbws6gtwi2Vuc+6MIykPPW6VGVxy1TXwH0p8dTFrQNiNj5QyCYhE4cyLuvu/LTASIXdrXpwVXnlcKR3ahO4wi45NfmM/JIz4="})

    # Module Courseware Request
    @task(10)
    def module_courseware_request(self):
        self.client.post("/api/v1.0/courseware", {"filter[group_audience][value][0]":"0", "filter[group_audience][value][1]":"114", "filter[group_audience][operator]":"IN", "include":"group_audience" })

    # Module Manual Request
    @task(10)
    def module_manual_request(self):
        self.client.post("/api/v1.0/manual", {"filter[group_audience][value][0]":"0", "filter[group_audience][value][1]":"114", "filter[group_audience][operator]":"IN", "include":"group_audience" })

    # Module Resource Request
    @task(10)
    def module_resource_request(self):
        self.client.post("/api/v1.0/resource", {"filter[group_audience][value][0]":"0", "filter[group_audience][value][1]":"114", "filter[group_audience][operator]":"IN", "include":"group_audience" })

    # Calendar Events
    @task(10)
    def module_courseware_request(self):
        self.client.post("/api/v1.0/calendar_event" )

    # Messages
    @task(10)
    def module_courseware_request(self):
        self.client.post("/api/v1.0/user_messages")



class WebsiteUser(HttpLocust):
    task_set = ApiCalls
    min_wait=5000
    max_wait=9000
