from django.shortcuts import render
from django.http import HttpResponse
from .models import Question;
from django.template import loader
from django.http import Http404
def index(request):
    latest_question_list1=Question.objects.order_by('pub_date')[:5];
    template=loader.get_template('polls/index.html');
    context={'latest_question_list':latest_question_list1};
    return HttpResponse(template.render(context,request));
   

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist");
        return render(request,'polls/detail.html',{'Question':question});
    
    return HttpResponse("you are looking at question %s."%question.id);

def results(request,question_id):
    response="You are looking at the result new of question %s.";
    return HttpResponse(response%question_id);

def vote(request,question_id):
    return HttpResponse("You are voting on question %s."%question_id);