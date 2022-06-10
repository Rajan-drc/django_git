from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello Rajan good work now you are about to use DJANGO and GIT to gather!")


def detail(request, question_id):
	return HttpResponse("Detail: question_id %s" % question_id)


def results(request, question_id):
	response = "results: You're looking at the result the results of question %s"
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("vote: question_id %s" % question_id)