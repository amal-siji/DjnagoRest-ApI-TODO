from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from todoapp.serializer import Todoserializer
from .models import Todo
import math
from datetime import datetime

# Create your views here.


class taskdetails(generics.GenericAPIView):
    task = Todo.objects.all()
    serializer_class = Todoserializer

    def get_task(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except:
            return None



    def get(self, request, pk):
        tasks = self.get_task(pk=pk)
        if tasks == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(tasks)
        return Response({"status": "success", "data": {"note": serializer.data}})

    def delete(self, request, pk):
        tasks = self.get_task(pk=pk)
        if tasks == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks.delete()
            return Response({"status": "successsfully deleted", })

    def patch(self, request, pk):
        tasks = self.get_task(pk)
        if tasks == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            tasks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}})
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class todopage(generics.GenericAPIView):
    serializer_class = Todoserializer
    queryset = Todo.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        tasks = Todo.objects.all()
        total_tasks = tasks.count()
       
        if search_param:
            tasks = tasks.filter(title__icontains=search_param)
        serializer = self.serializer_class(tasks[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_tasks,
            "page": page_num,
            "last_page": math.ceil(total_tasks / limit_num),
            "notes": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
