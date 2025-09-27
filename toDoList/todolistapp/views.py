from django.shortcuts import render
from django.http import JsonResponse , HttpRequest 
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
 
def index(request):
  return JsonResponse({"message": "Hello from Django"})


def tasks(request):
  listOfTasks=Task.objects.all().values()
  return JsonResponse(list(listOfTasks),safe=False)


@csrf_exempt 
def updateIsDone(request: HttpRequest , task_id) :
  data = json.loads(request.body.decode("utf-8"))

  task=Task.objects.get(id=task_id)
  task.is_done=data.get("is_done", task.is_done)
  task.save()
  return JsonResponse({"state":"the update is done"})


@csrf_exempt 
def add_task(request : HttpRequest):
  data =json.loads(request.body.decode("utf-8"))
  task=Task(task_text=data.get("task_text"),is_done=data.get("is_done"))
  task.save()
  return JsonResponse({"state":f"the task is added , it's id is : {task.object.get}"})
  
@csrf_exempt 
def delete_task(request: HttpRequest, id):
   
    task=Task.objects.get(id=id)
    task.delete()
    return JsonResponse({"state":f"the task is deleted , it's id is : {task.object.get}"})
