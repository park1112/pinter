from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy


def hello_world(request):

    if request.method == "POST":

        ## 17강 post 통신 객체보내기 추가 부분
        temp = request.POST.get('hello_world_input')        ## 통신에서 텍스트 긁어 오기

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()


        ## 18강 새로고침으로 인해서 자동 생성되는거 막은거
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

## 21강 회원가입폼 만들기
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm   ## 원하는 폼을 가지고 온다 html파일과 연결시켜서 사용함 create.html {{ form }} 으로 사용
    success_url = reverse_lazy('accountapp:hello_world')    #계정 만들기에 성공하면 어디로 이동할것인가 ?
    template_name = 'accountapp/create.html'          ## 회원가입할때 볼 템플릿을 설정해준다


## 24강 디테일뷰 만들기
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


## 25강 업데이트뷰
class AccountUpdateView(UpdateView):        ## django에 (UpdateView)를 가지고 온다
    model = User
    context_object_name = 'target_user'     #27강 추가
    form_class = AccountUpdateForm   ## 원하는 폼을 가지고 온다 html파일과 연결시켜서 사용함 create.html {{ form }} 으로 사용
    success_url = reverse_lazy('accountapp:hello_world')    #계정 만들기에 성공하면 어디로 이동할것인가 ?
    template_name = 'accountapp/update.html'          ## 회원가입할때 볼 템플릿을 설정해준다

## 26강 delete
class AccountDeleteView(DeleteView):        ##이것도 가지고 온다
    model = User
    context_object_name = 'target_user'     #27강 추가
    success_url = reverse_lazy('accountapp:login')  # 계정 만들기에 성공하면 어디로 이동할것인가 ?
    template_name = 'accountapp/delete.html'  ## 회원가입할때 볼 템플릿을 설정해준다

