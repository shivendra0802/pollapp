from django.shortcuts import render
from rest_framework.response import Response
from .serializers import TestSerializer
from .models import Album, TestModel
from rest_framework.views import APIView
from rest_framework.decorators import api_view



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from testapp import serializers


# Create your views here.
class TestView(APIView):
    def get(request, format=None):
        data = {
	        "key1" : "", 
	        "coverage_requirements" : [{"key" : "", "amount" : "", "start_date" : "","expiry_date" : '20211123T13:12:12'}],
	        "key2" : ""
        }
        return Response(request, data=Response.data)

    def post(request, format=None):
        pass
        return Response(request, data=Response.data)    

@api_view()
def testapi(request):
        pass
        """
        Return a list of all users.
          """
        people = {"key_test":"pythontest",
        "coverage_requirements":[{"coverage": 'John', 'amount': '27', 'start_date': '2020-03-22T13:17:27.853707Z','end_date':'2020-03-22T13:17:27.853707Z'},
        {"coverage": 'John', 'amount': '27', 'start_date': '2020-03-22T13:17:27.853707Z','end_date':'2020-03-22T13:17:27.853707Z'},
        {"coverage": 'John', 'amount': '27', 'start_date': '2020-03-22T13:17:27.853707Z','end_date':'2020-03-22T13:17:27.853707Z'},
        ],"key2_test":"dfdff"}
        print(people)
      
        return Response({"message": people})



from rest_framework import renderers
from rest_framework import generics
from .models import Track
from rest_framework import status



class TrackHighlight(generics.GenericAPIView):
    queryset = Track.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        track = self.get_object()
        return Response(track.highlighted)

from .serializers import AlbumSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Album.objects.all()
        serializer = AlbumSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        album = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    
    # elif request.method =='POST':
    #     serializer = AlbumSerializer(album, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        