from django.conf.urls import url

from . import views

urlpatterns = [
		# r'^$' refers to an empty string
		# index will call the view method called index

		#url(r'^$', views.index, name = 'index'),

		# + besides the [0-9] means one or more of those
		# if you wanted strings to work then [a-z] will work
		url(r'^$', views.IndexView.as_view(), name = 'index'),

		#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
		#url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
		#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote')

		url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
		url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results'),
		url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
]