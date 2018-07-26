from locust import HttpLocust, TaskSet, task
import random
class MyTaskSet(TaskSet):
	# cookie = ""
	# def on_start(self):
	# 	self.cookie = self.get_user_cookie()
	# def get_user_cookie(self):
	# 	if BASIC_AUTH_CREDENTIALS:
	# 		self.client.auth = BASIC_AUTH_CREDENTIALS
	@task(2)
	def index(self):
		self.client.get("/")
	@task(1)
	def about(self):
		headers = {'referer': 'http://www.relearn.pro'}
		r = self.client.get('/')
		qnum = random.randint(1, 10)
		# r = self.client.post("/kaarstudent",{"regno":"447","email":"theincredible13@gmail.com",'csrfmiddlewaretoken': r.cookies['csrftoken']})
		print(r)
		# self.cookies = { '_session': r.cookies['_session'] }
		data = {'csrfmiddlewaretoken': r.cookies['csrftoken'],'username': '447','password': 'theincredible13@gmail.com',"user":"447","question":"qqqqq","qnum":qnum,"currq":qnum,"sub":[1,2],"mark":[1,2],"skip":[1,2],"time":"60:00","seconds":"2000","section":1,'answer':"@"}
		# if r.status_code == 200:
		# 	return r.request.headers['Cookie']
		# else:
		# 	print ("User cannot login")
		# print(self)
		self.client.post("/test",data=data, headers=headers)

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 100
    max_wait = 100

