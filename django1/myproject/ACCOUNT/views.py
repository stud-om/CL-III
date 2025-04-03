from django.shortcuts import render
from LIBRARY.models import books
from ACCOUNT.models import account
import ACCOUNT










def view_hello_20(request):   

    return render(request,'hello-20.html',{})



def view_record(request):

    stud_record = books.objects.all()
    city_record = account.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'city12':city_record})


       # return render_to_response('courtcase/report_display.html', {'entry_list': q, 'entry_list1': q1,})


    # return render_to_response('hello.html', {'entry_list': q, 'entry_list1': q1,})





# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# Note that once we’ve done this in all these views, we no longer need to import loader and Ht




# Create your views here.