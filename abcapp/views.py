from django.shortcuts import render
from django.db import connections

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import *
from . models import *
# from ..demoapp.models import Demo
from demoapp.models import Demo

from demoapp.serializers import DemoSerializer


class ABCApi(APIView):
    def post(self,request):
        serializer=ABCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success'})
    def get(self,request):
        data=ABC.objects.all()
        serializer=ABCSerializer(data,many=True)
        return Response(serializer.data)





class DemoView(APIView):
    def get(self, request):
        data = Demo.objects.all()
        serializer = DemoSerializer(data, many=True)
        # return Response(serializer.data)
        # with connections['demo_db'].cursor() as cursor:
        #     cursor.execute('SELECT * FROM demoapp_demo')
        #     result = cursor.fetchall()

        # Process the result as needed
        # data = []
        # for row in result:
        #     # Assuming your_table has columns 'id' and 'name'
        #     data.append({'id': row[0], 'name': row[1]})

        return Response(serializer.data)




# class DemoView(APIView):
#     def get(self, request):
#
#         with connections['demo_db'].cursor() as cursor:
#             cursor.execute('SELECT * FROM demoapp_demo')
#             result = cursor.fetchall()
#             print('result',result)
#
#         # Process the result as needed
#         data = []
#         for row in result:
#             # Assuming your_table has columns 'id' and 'name'
#             data.append({'id': row[0], 'first_name':row[1],'last_name':row[2],'phone':row[3]})
#         print('data',data)
#
#         # return Response(data)
#         return Response(data)
#
