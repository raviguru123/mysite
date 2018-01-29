from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.http import Http404
from django.urls import reverse

def index(request):
    latest_question_list1=Question.objects.order_by('pub_date')[:5];
    template=loader.get_template('polls/index.html');
    context={'latest_question_list':latest_question_list1};
    return HttpResponse(template.render(context,request));
   

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id);
        context={'question':question};
        template=loader.get_template('polls/detail.html');
        return HttpResponse(template.render(context,request));
    except Question.DoesNotExist:
        raise Http404("Question does not exist");
        return render(request,'polls/detail.html',{'Question':question});
    
    
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id);
    template=loader.get_template('polls/result.html');
    context={'question':question};
    return HttpResponse(template.render(context,request));
    

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id);
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
            return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice"});
    else:
        selected_choice.votes+=1;
        selected_choice.save();
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

