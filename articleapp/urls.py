from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    ## 장고 템플릿으로 바로 만들수 있다
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]