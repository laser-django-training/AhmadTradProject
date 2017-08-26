from django.conf.urls import url

from TMS import views


urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^index/(?P<task_id>\d+)/$", views.subtasks, name="index"),
	url(r"^login/$", views.login, name="login"),
	url(r"^logout/$", views.logout, name="logout"),

]
