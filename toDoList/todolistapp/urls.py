from django.urls import path  
from . import views

urlpatterns = [
    path("",views.index),
    path("tasks/",views.tasks),
    path("tasks/<int:task_id>/update/",views.updateIsDone),
    path("tasks/add/", views.add_task),
    path("tasks/<int:id>/delete/", views.delete_task)
]