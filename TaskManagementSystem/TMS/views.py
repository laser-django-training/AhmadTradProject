from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user

from TMS.models import *


def check_login(func):
	def func_wrapper(*args, **kwargs):
		request = args[0]
		if not "username" in request.session:
			return redirect("login")
		return func(*args, **kwargs)
	return func_wrapper

def login(request):
	message = ""
	if request.method == "POST":
		is_user = authenticate(username=request.POST.get("username", ""),
			password=request.POST.get("password", ""))
		if is_user != None:
			get_employee = Employee.objects.filter(user__username=request.POST["username"])
			if get_employee:
				request.session["username"] = get_employee[0].firstname
				return redirect("index")
			else:
				message = "Username not associated with Employee!"
		else:
			message = "Wrong username or password!"

	return render(request, "login.html", {
		"message": message
		})
		
@check_login
def logout(request):
	if "username" in request.session:
		del request.session["username"]
	return redirect("login")


@check_login
def index(request):
	tasks = Task.objects.all()
	return render(request, "index.html", {
		"tasks": tasks
		})
def subtasks(request, task_id):
	message = None
	subtasks = SubTask.objects.filter(task__id = int(task_id))
	if not subtasks:
		message = "No sub tasks for this task"
		tasks = Task.objects.all()
		return render(request, "index.html", {
		"tasks": tasks,
		"message": message
		})
	else:
		return render(request, "sub_task.html",{
			"subtasks": subtasks
			})