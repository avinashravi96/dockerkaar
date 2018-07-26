from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Student,AptQuestion,Submit,Marked,Skip,Finished,Order,Answered
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.template import RequestContext
import re
import random

def kaarindex(request):

	return render(request,'kaarindex.html')

def kaarstudent(request):
	return render(request,"kaarsignin.html",{})

def instructions(request):
    try:
    	ob = Student(
		name = request.POST["name"],
# 	preference1 = request.POST["role"],
# 	preference2 = request.POST["role2"],
	regno = request.POST["regno"],
	email = request.POST["email"],
	number = request.POST["mobileno"],
	altnumber = request.POST["altnumber"],
	mothertoungue = request.POST["language"],
	dob = request.POST["dob"],
	gender = request.POST["gender"],
	tenth = request.POST["tenth"],
	twelth = request.POST["twelth"],
# 	college = request.POST["college"],
# 	stream = request.POST["stream"],
# 	graduation = request.POST["graduation"],

	ugcollege =  request.POST["college"],
    ugstream = request.POST["stream"],
    undergraduation =  request.POST["graduation"],
    pgcollege =  request.POST["pgcollege"],
    pgstream =  request.POST["pgstream"],
    postgraduation =  request.POST["pggraduation"],
    zone =  request.POST["zone"],
    members =  request.POST["fam"],
    earningmembers =  request.POST["earn"],
    fatherprof = request.POST["fatherprof"],
    motherprof = request.POST["motherprof"],
    written = request.POST["writtenenglish"],
    spoken =  request.POST["spokenenglish"],
    msoffice = request.POST["msoffice"],
    extracurricular = request.POST["extra"],

	QAscore = 0,
	LRscore = 0,
	VRscore = 0,
	time = "60:00")
    	ob.save()
    	user = User.objects.create_user(username= request.POST['regno'],password = request.POST['email'])
    	user.save()
    	user = authenticate(username = request.POST['regno'],password = request.POST['email'])



    	if user is not None:
    		if user.is_active:
    			login(request,user)
    			c3 = AptQuestion.objects.filter(section = 3).count()
    			c2 = AptQuestion.objects.filter(section = 2).count()
    			c1 = AptQuestion.objects.filter(section = 1).count()
    			for i in range(1,4):

    				ob = Submit(user = request.user.username,questions="",section=i)
    				ob.save()
    				ob = Marked(user = request.user.username,questions="",section=i)
    				ob.save()
    				ob = Skip(user = request.user.username,questions="",section=i)
    				ob.save()
    				if i==1:
    					nums = random.sample(range(1,c1),20)
    					nums = ','.join(map(str,nums))

    				if i==2:
    					nums = random.sample(range(1,c2),20)
    					nums = ','.join(map(str,nums))

    				if i==3:
    					nums = random.sample(range(1,c3),10)
    					nums = ','.join(map(str,nums))

    				ob = Order(user = request.user.username,questions=nums,section=i)
    				ob.save()
    				if i == 3:
    					ans = "@,@,@,@,@,@,@,@,@,@"
    				else:
    					ans = "@,@,@,@,@,@,@,@,@,@,@,@,@,@,@,@,@,@,@,@"
    				ob = Answered(user = request.user.username, section= i, answers = ans)
    				ob.save()
    			return render(request,'instructions.html')
    except Exception as e:
    	print(e)
    	pass

    return render(request,"kaarindex.html",{'flag':1})

def kaarsignin(request):
	user = authenticate(username = request.POST['regno'],password = request.POST['email'])



	if user is not None:
		if user.is_active:
			login(request,user)
			return redirect('kaartest')
			# for i in range(1,4):
			# 	try:
			# 		ob = Submit(user = request.user.username,questions="",section=i)
			# 		ob.save()
			# 	except:
			# 		pass
			# 	try:
			# 		ob = Marked(user = request.user.username,questions="",section=i)
			# 		ob.save()
			# 	except:
			# 		pass
			# 	try:
			# 		ob = Skip(user = request.user.username,questions="",section=i)
			# 		ob.save()
			# 	except:
			# 		pass
	return render(request,'kaarsignin.html',{'flag':1})


def test(request):
	try:
	    if Finished.objects.filter(user = request.user.username).exists():
	    	return redirect('endtest')
	    # print(request.user.username)
	    ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 1)[0][0]
	    ques = ques.split(',')

	    sec1 = AptQuestion.objects.all().filter(section = 1)[int(ques[0])]
	    qnum = "Q 01"
	    currq = "1"
	    section = 1

	    if "cursection" in request.POST:


	    	section = int(request.POST['cursection'])
	    	# print("ss")
    		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
    		ques = ques.split(',')
	    	sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    	try:
	    		a=1
	    		# count = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		# count = count.split(',')
	    		# count = len(count)
	    		# if count < 20 and section != 3:
	    		# 	currq = int(qno) + 1
	    		# 	sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		# 	sub = sub.split(',')
	    		# if currq == 21:
	    		# 	currq = 1
	    		# while str(currq) in sub :
	    		# 	currq += 1
	    		# 	if currq == 21:
	    		# 		currq = 1
	    		# if count < 10 and section == 3:
	    		# 	currq =  1
	    		# 	sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		# 	sub = sub.split(',')
	    		# 	if currq == 11:
	    		# 		currq = 1
	    		# 	while str(currq) in sub :
	    		# 		currq += 1
	    		# 		if currq == 11:
	    		# 			currq = 1
	    		# if int(currq) > 9:
	    		# 	qnum = "Q " + str(currq)
	    		# else:
	    		# 	qnum = "Q 0" + str(currq)
	    		# ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
	    		# ques = ques.split(',')
	    		# try:
	    		# 	sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    		# except:
	    		# 	sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    		# 	qnum = "Q 01"
	    		# 	currq = 1


	    	except:
	    		pass


	    if "section" in request.POST:


	    	section = int(request.POST['section'])
	    	# print(section)
	    	try:
	    		count = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		count = count.split(',')
	    		count = len(count)

	    		# print(qno,currq,section)
	    		if count < 20 and section != 3:
	    			# print("safe")
	    			# print(section)
	    			currq =  1
	    			sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    			sub = sub.split(',')
	    			if currq == 21:
	    				currq = 1
	    			while str(currq) in sub :
	    				currq += 1
	    				if currq == 21:
	    					curr=1
	    					break
	    		elif count < 10 and section == 3:
	    			# print(section,"ss")
	    			currq =  1
	    			sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    			sub = sub.split(',')
	    			if currq == 11:
	    				currq = 1
	    			while str(currq) in sub :
	    				currq += 1
	    				if currq == 11:
	    					currq=1
	    					break

	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
	    		ques = ques.split(',')
	    		try:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    		except:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    			qnum = "Q 01"
	    			currq = 1

	    		# sec1 = AptQuestion.objects.all().filter(section = section)[int(request.POST['qno'])]
	    	except:
	    		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
	    		ques = ques.split(',')
	    		sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    		# print("excepst")


	    	# sec1 = AptQuestion.objects.all().filter(section = section)[int(request.POST['secq'])]

	    if "qno" in request.POST:

	    	qno = request.POST['qno']
	    	qnum = "Q " + qno
	    	currq = qno


	    	qno = re.sub(r'0(\d)',r'\1',qno)

	    	ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
	    	ques = ques.split(',')
	    	try:
	    		sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[int(qno)-1])]
	    	except:
	    		sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    		qnum = "Q 01"
	    		# currq = 1

        # mark
	    if "markedq" in request.POST:


	    	qno = request.POST["markedq"]
	    	qno = re.sub(r'0(\d)',r'\1',qno)

	    	ob = Marked.objects.get(user = request.user.username,section=int(request.POST['cursection']))
	    	if ob.questions == "":
	    		ob.questions = qno
	    	else:
	    	    ob.questions += "," + qno
	    	ob.save()
	    	count = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    	count = count.split(',')
	    	count = len(count)

	    	# int(qno) <= 20 and
	    	if count < 20 and section != 3:
	    		currq = int(qno) + 1
	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    		sub = sub.split(',')


	    		if currq == 21:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 21:
	    				currq = 1
	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = int(request.POST['cursection']))[0][0]
	    		ques = ques.split(',')
	    		try:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    		except:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    			qnum = "Q 01"
	    			currq = 1

	    	elif count < 10 and section == 3:
	    		# print(qno)
	    		currq = int(qno) + 1
	    		# currq =  1
	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		sub = sub.split(',')
	    		if currq == 11:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 11:
	    				currq = 1

	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = int(request.POST['cursection']))[0][0]
	    		ques = ques.split(',')
	    		try:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    		except:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    			qnum = "Q 01"
	    			currq = 1


	    if "skipped" in request.POST:


	    	qno = request.POST["skipped"]
	    	qno = re.sub(r'0(\d)',r'\1',qno)

	    	ob = Skip.objects.get(user = request.user.username,section=int(request.POST['cursection']))
	    	if ob.questions == "":
	    		ob.questions = qno
	    	else:
	    	    ob.questions += "," + qno
	    	ob.save()
	    	count = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    	count = count.split(',')
	    	count = len(count)

	    	# int(qno) <= 20 and
	    	if count < 20 and section != 3:
	    		currq = int(qno) + 1
	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    		sub = sub.split(',')

	    		# print(sub)
	    		if currq == 21:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 21:
	    				currq = 1
	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    			ques = Order.objects.values_list('questions').filter(user = request.user.username,section =  int(request.POST['cursection']))[0][0]
	    			ques = ques.split(',')
	    			try:
	    				sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    			except:
	    				sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    				qnum = "Q 01"
	    				currq = 1


	    	elif count < 10 and section == 3:
	    		currq = int(qno) + 1
	    		# print(qno)
	    		# currq =  1
	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		sub = sub.split(',')
	    		if currq == 11:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 11:
	    				currq = 1
	    	if int(currq) > 9:
	    		qnum = "Q " + str(currq)
	    	else:
	    		qnum = "Q 0" + str(currq)
	    	ques = Order.objects.values_list('questions').filter(user = request.user.username,section =  section)[0][0]
	    	ques = ques.split(',')
	    	try:
	    		# print(ques[currq-1])
	    		sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    	except:
	    		sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    		qnum = "Q 01"
	    		currq = 1

        # Submit
	    if "questionno" in request.POST:


	    	qno = request.POST["questionno"]
	    	section=int(request.POST['cursection'])
	    	qno = re.sub(r'0(\d)',r'\1',qno)
	    	ob = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    	q = ob.split(",")
	    	# print(q)
	    	qflag = 0
	    	if qno in q:
	    		qflag = 1

	    	ob = Submit.objects.get(user = request.user.username,section=int(request.POST['cursection']))
	    	if ob.questions == "" and qflag == 0:
	    		ob.questions = qno
	    	elif qflag == 0:
	    	    ob.questions += "," + qno
	    	ob.save()
	    	ques = Order.objects.values_list('questions').filter(user = request.user.username, section = int(request.POST['cursection']))[0][0]
	    	ques = ques.split(',')
	    	sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[int(qno)-1])]

	    	if request.POST["optradio"] == sec1.answer and "optradio" in request.POST and qflag == 0:
	    		ob = Student.objects.get(regno = request.user.username)
	    		if section == 1:
	    			ob.QAscore += 1
	    		if section == 2:
	    			ob.LRscore += 1
	    		if section == 3:
	    			ob.VRscore += 1
	    		ob.save()
	    	elif qflag == 1:
	    		ob2 = Answered.objects.values_list('answers').filter(user = request.user.username, section = section)[0][0]
	    		thisanswer = ob2.split(',')
	    		# print(qno)
	    		thisanswer = thisanswer[int(qno)-1]

	    		if request.POST["optradio"] == sec1.answer and "optradio" in request.POST and thisanswer != sec1.answer:
	    			ob = Student.objects.get(regno = request.user.username)
	    			if section == 1:
	    				ob.QAscore += 1
	    			if section == 2:
	    				ob.LRscore += 1
	    			if section == 3:
	    				ob.VRscore += 1
	    			ob.save()

	    		elif request.POST["optradio"] != sec1.answer and "optradio" in request.POST and thisanswer == sec1.answer:
	    			ob = Student.objects.get(regno = request.user.username)
	    			if section == 1:
	    				ob.QAscore -= 1
	    			if section == 2:
	    				ob.LRscore -= 1
	    			if section == 3:
	    				ob.VRscore -= 1
	    			ob.save()

	    	if "optradio" in request.POST:
	    		ob = Answered.objects.get(user = request.user.username, section = section)
	    		ans = ob.answers
	    		ans = ans.split(',')
	    		try:
	    			ans[int(qno)-1] = 	request.POST["optradio"]
	    		except:
	    			pass
	    		# print(ans)
	    		ans = ','.join(ans)
	    		ob.answers = ans
	    		ob.save()


	    	count = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    	count = count.split(',')
	    	count = len(count)

	    	if count < 20 and section != 3:

	    		currq = int(qno) + 1

	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    		sub = sub.split(',')

	    		if currq == 21:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 21:
	    				currq = 1
	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    			ques = Order.objects.values_list('questions').filter(user = request.user.username, section = int(request.POST['cursection']))[0][0]
	    			ques = ques.split(',')
	    		try:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[currq-1])]
	    		except:
	    			sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    			qnum = "Q 01"
	    			currq = 1


	    	elif count < 10 and section == 3:


	    		currq =  1
	    		sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=3)[0][0]
	    		sub = sub.split(',')
	    		if currq == 11:
	    			currq = 1
	    		while str(currq) in sub :
	    			currq += 1
	    			if currq == 11:
	    				currq=1
	    				break
	    		if int(currq) > 9:
	    			qnum = "Q " + str(currq)
	    		else:
	    			qnum = "Q 0" + str(currq)
	    			ques = Order.objects.values_list('questions').filter(user = request.user.username, section = int(request.POST['cursection']))[0][0]
	    			ques = ques.split(',')
	    		try:
	    			sec1 = AptQuestion.objects.all().filter(section = 3)[int(ques[currq-1])]
	    		except:
	    			sec1 = AptQuestion.objects.all().filter(section = 3)[int(ques[0])]
	    			qnum = "Q 01"
	    			currq = 1


	    	else:
	    		count = Submit.objects.values_list('questions').filter(user = request.user.username,section=1)[0][0]
	    		count = count.split(',')
	    		count = len(count)
	    		section = 1
	    		if count < 20 :


	    			currq =  1
	    			sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    			sub = sub.split(',')
	    			if currq == 21:
	    				currq = 1
	    			while str(currq) in sub :
	    				currq += 1
	    				if currq == 21:
	    					currq=1
	    					break

	    			if int(currq) > 9:
	    				qnum = "Q " + str(currq)
	    			elif currq<=20:
	    				qnum = "Q 0" + str(currq)
	    				ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 1)[0][0]
	    				ques = ques.split(',')
	    				try:
	    					sec1 = AptQuestion.objects.all().filter(section = 1)[int(ques[currq-1])]
	    				except:
	    					sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]
	    					qnum = "Q 01"
	    					currq = 1

	    		# elif count < 10 and section == 3:
	    		# 	currq =  1
	    		# 	sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    		# 	sub = sub.split(',')
	    		# 	if currq == 11:
	    		# 		currq = 1
	    		# 	while str(currq) in sub :
	    		# 		currq += 1
	    		# 		if currq == 11:
	    		# 			currq = 1
	    		# 	if int(currq) > 9:
	    		# 		qnum = "Q " + str(currq)
	    		# 	elif currq<=20:
	    		# 		qnum = "Q 0" + str(currq)
	    		# 		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 1)[0][0]
	    		# 		ques = ques.split(',')
	    		# 		sec1 = AptQuestion.objects.all().filter(section = 1)[int(ques[currq-1])]
	    		else:
	    			count = Submit.objects.values_list('questions').filter(user = request.user.username,section=2)[0][0]
	    			count = count.split(',')
	    			count = len(count)
	    			section = 2
	    			if count < 20:
	    				currq =  1
	    				sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    				sub = sub.split(',')
	    				if currq == 21:
	    					currq = 1
	    				while str(currq) in sub :
	    					currq += 1
	    					if currq == 21:
	    						currq=1
	    						break

	    				if int(currq) > 9:
	    					qnum = "Q " + str(currq)
	    				elif currq<=20:
	    					qnum = "Q 0" + str(currq)
	    					ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 2)[0][0]
	    					ques = ques.split(',')
	    					sec1 = AptQuestion.objects.all().filter(section = 2)[int(ques[currq-1])]
	    			# elif count < 10 and section == 3:
	    			# 	currq =  1
	    			# 	sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=section)[0][0]
	    			# 	sub = sub.split(',')
	    			# 	if currq == 11:
	    			# 		currq = 1
	    			# 	while str(currq) in sub :
	    			# 		currq += 1
	    			# 		if currq == 11:
	    			# 			currq = 1
	    			# 	if int(currq) > 9:
	    			# 		qnum = "Q " + str(currq)
	    			# 	elif currq<=20:
	    			# 		qnum = "Q 0" + str(currq)
	    			# 		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 2)[0][0]
	    			# 		ques = ques.split(',')
	    			# 	sec1 = AptQuestion.objects.all().filter(section = 2)[int(ques[currq-1])]
	    			else:
	    				count = Submit.objects.values_list('questions').filter(user = request.user.username,section=3)[0][0]
	    				count = count.split(',')
	    				count = len(count)
	    				# print(count,section)

	    				# if count < 20 and section != 3:
	    				# 	currq =  1
	    				# 	sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(request.POST['cursection']))[0][0]
	    				# 	sub = sub.split(',')
	    				# 	if currq == 21:
	    				# 		currq = 1
	    				# 	while str(currq) in sub :
	    				# 		currq += 1
	    				# 		if currq == 21:
	    				# 			currq = 1
	    				# 			section = 3
	    				# 			break
	    				# 	if int(currq) > 9:
	    				# 		qnum = "Q " + str(currq)
	    				# 	elif currq<=20:
	    				# 		qnum = "Q 0" + str(currq)
	    				# 		ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 2)[0][0]
	    				# 		ques = ques.split(',')
	    				# 		sec1 = AptQuestion.objects.all().filter(section = 3)[int(ques[currq-1])]
	    				if count < 10 :
	    					currq =  1
	    					section = 3
	    					sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=3)[0][0]
	    					sub = sub.split(',')
	    					# print(sub)
	    					if currq == 11:
	    						currq = 1
	    					while str(currq) in sub :
	    						currq += 1
	    						if currq == 11:
	    							currq = 1
	    							break
	    					# print(currq,section)
	    					if int(currq) > 9:
	    						qnum = "Q " + str(currq)
	    					elif currq<=20:
	    						qnum = "Q 0" + str(currq)
	    						ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 3)[0][0]
	    						ques = ques.split(',')
	    						sec1 = AptQuestion.objects.all().filter(section = 3)[int(ques[currq-1])]
	    				else:
	    					# return redirect('endtest')
	    					# count = Submit.objects.values_list('questions').filter(user = request.user.username,section=1)[0][0]
	    					# count = sub.split(',')
	    					# if len(count) == 20:
	    					# 	count = Submit.objects.values_list('questions').filter(user = request.user.username,section=2)[0][0]
	    					# 	count = sub.split(',')
	    					# 	if len(count) == 20:
	    					# 		count = Submit.objects.values_list('questions').filter(user = request.user.username,section=3)[0][0]
	    					# 		count = sub.split(',')
	    					# 		if len(count) == 10:
	    					# 			count = Submit.objects.values_list('questions').filter(user = request.user.username,section=2)[0][0]
	    					# 			count = sub.split(',')
	    					# 		else:
	    					# 			section = 3
	    					# 	else:
	    					# 		section = 2
	    					# else:
	    					# 	section = 1

	    					currq =  1
	    					ques = Order.objects.values_list('questions').filter(user = request.user.username, section = section)[0][0]
	    					ques = ques.split(',')
	    					qnum = "Q 01"
	    					sec1 = AptQuestion.objects.all().filter(section = section)[int(ques[0])]



	    sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    sub = sub.split(',')

	    mark = Marked.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    mark = mark.split(',')

	    skip = Skip.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    skip = skip.split(',')

	    question = int(re.sub(r'0(\d)',r'\1',str(currq)))

	    ob = Answered.objects.values_list('answers').filter(user = request.user.username, section = section)[0][0]
	    ob = ob.split(',')
	    answer = ob[question-1]
	    # print(ob[question-1]," ",question)

	    # print(section,request.POST['section'])
	    if "time" in request.POST:
	    	time = request.POST['time']
	    	ob = Student.objects.get(regno = request.user.username)
	    	ob.time = request.POST['time']
	    	ob.save()
	    else:
	    	time = Student.objects.values_list('time').filter(regno = request.user.username)[0][0]
	    # print(time)

	    minute = time.split(":")
	    seconds = int(minute[0])*60 + int(minute[1])-1
	    # print(time,seconds)
	    return render(request,'test.html',{'user':request.user.username,'question':sec1,'qnum':qnum,'currq':currq,
	    	'sub':sub,'mark':mark,'skip':skip,'time':time,'seconds':seconds,'section':section,'answer':answer})
	except IndexError:

	    print("request.user.username")
	    ques = Order.objects.values_list('questions').filter(user = request.user.username, section = 1)[0][0]
	    ques = ques.split(',')

	    sec1 = AptQuestion.objects.all().filter(section = 1)[int(ques[0])]
	    qnum = "Q 01"
	    currq = "1"
	    section = 1



	    sub = Submit.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    sub = sub.split(',')

	    mark = Marked.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    mark = mark.split(',')

	    skip = Skip.objects.values_list('questions').filter(user = request.user.username,section=int(section))[0][0]
	    skip = skip.split(',')

	    question = int(re.sub(r'0(\d)',r'\1',str(currq)))

	    ob = Answered.objects.values_list('answers').filter(user = request.user.username, section = int(section))[0][0]
	    ob = ob.split(',')
	    answer = ob[question-1]

	    if "time" in request.POST:
	    	time = request.POST['time']
	    	ob = Student.objects.get(regno = request.user.username)
	    	ob.time = request.POST['time']
	    	ob.save()
	    else:
	    	time = Student.objects.values_list('time').filter(regno = request.user.username)[0][0]
	    # print(time)

	    minute = time.split(":")
	    seconds = int(minute[0])*60 + int(minute[1])-1
	    return render(request,'test.html',{'user':request.user.username,'question':sec1,'qnum':qnum,'currq':currq,
	    	'sub':sub,'mark':mark,'skip':skip,'time':time,'seconds':seconds,'section':section,'answer':answer})


def kaarfinish(request):
	if Finished.objects.filter(user = request.user.username).exists():
		pass
	else:
		ob = Finished(user = request.user.username)
		ob.save()
	logout(request)
	return render(request,'finish.html')

def karcheck(request):
    return render(request,"check.html")
# 	ob = AptQuestion.objects.filter(section = 3).count()
# 	print(ob)
	# ob = AptQuestion.objects.values_list('text').filter(section = 1)[1]
	# ob = ob.split(',')
	# print(ob[1])
# 	return HttpResponse(ob)
