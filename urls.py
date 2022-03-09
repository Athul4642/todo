from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.task_view,name='result'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cobtask/',views.TaskListView.as_view(),name='cobtask'),
    path('cobdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cobdetail'),
    path('cobupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cobupdate'),
    path('cobdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cobdelete')

]
