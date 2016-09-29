from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse

from django.core.urlresolvers import reverse

#from django.views import generic

from .models import Choice, Question

#class IndexView(generic.ListView):
#	templates_name = 'polls/index.html'
#	context_object_name = 'latest_question_list'

#	def get_queryset(self)

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse("Hello world! This is the polls index.")
	#return HttpResponse(output)
	context = {'latest_question_list': latest_question_list}
	return render(request, 'index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	#return HttpResponse("You're looking at question %s" % (question_id))
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	#return HttpResponse("You're looking at results for %s" % (question_id))
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	#return HttpResponse("You're voting on question %s" % (question_id))
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. this prevents data from being posted twice if
		# a user hits the back button
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))