from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    ## 장고 템플릿으로 바로 만들수 있다
    path('list/', ArticleListView.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

]