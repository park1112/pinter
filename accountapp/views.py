
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse


def hello_world(request):

    if request.method == "POST":

        ## 17강 post 통신 객체보내기 추가 부분
        temp = request.POST.get('hello_world_input')        ## 통신에서 텍스트 긁어 오기

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()



        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})