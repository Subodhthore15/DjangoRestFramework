from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def todo_get(request):
    todos=Todo.objects.all()
    ser = TodoSerializer(todos,many=True)
    return Response(ser.data)


@api_view(['POST'])
def todo_post(request):
    
    ser = TodoSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:

        return Response(ser.error_messages)


@api_view(['GET'])
def todo_get_pk(request,pk):
    to  = Todo.objects.get(pk=pk)
    ser = TodoSerializer(to)
    return Response(ser.data)


@api_view(['PUT'])
def todo_update_pk(request,pk):
    to  = Todo.objects.get(pk=pk)
    ser = TodoSerializer(to,data=request.data)

    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:
        return Response(ser.error_messages)
    
@api_view(['DELETE'])
def todo_delete_pk(request,pk):
    to  = Todo.objects.get(pk=pk)
    to.delete();
    return Response({"Msg":"Succesfully deleted"})
    

