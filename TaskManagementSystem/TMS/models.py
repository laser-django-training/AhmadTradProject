from datetime import datetime
from django.utils import timezone

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Employee(models.Model):
	firstname = models.CharField(max_length=100, db_index=True)
	lastname = models.CharField(max_length=100)
	employeetype = models.CharField(max_length=30, null = True, blank = True)
	user = models.ForeignKey(User, db_index=True)

	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)


class Group(models.Model):
	name = models.CharField(max_length=100)
	employee = models.ManyToManyField(Employee)


class Task(models.Model):
	title = models.CharField(max_length=100, null = True, blank = True)
	description = models.CharField(max_length=500)
	creationdate = models.DateTimeField(default=timezone.now)
	updatedate = models.DateTimeField(null = True, blank = True)
	deadline = models.DateTimeField(null = True, blank = True)
	progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	iscompleted = models.BooleanField(default=False)
	owner = models.ForeignKey(Employee, null = True, blank = True)


class SubTask(models.Model):
	title = models.CharField(max_length=100, null = True, blank = True)
	description = models.CharField(max_length=500)
	creationdate = models.DateTimeField(default=timezone.now)
	updatedate = models.DateTimeField(null = True, blank = True)
	deadline = models.DateTimeField(null = True, blank = True)
	progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	iscompleted = models.BooleanField(default=False)
	task = models.ForeignKey(Task)
	


class TaskPreviliges(models.Model):
	task = models.ForeignKey(Task)
	employee = models.ForeignKey(Employee, null = True, blank = True)
	group = models.ForeignKey(Group, null = True, blank = True)


class SubTaskPreviliges(models.Model):
	task = models.ForeignKey(Task)
	employee = models.ForeignKey(Employee)
	group = models.ForeignKey(Group)
