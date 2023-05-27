from rest_framework import generics
from rest_framework.views import APIView
from .models import Drug
from .serializers import DrugSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q





@api_view(['POST'])
def search_models(request):
    query = request.data.get('query', '')
    if query:
        drugs = Drug.objects.filter(Q(name__icontains=query))
        serializer = DrugSerializer(drugs, many=True)

        return Response(serializer.data)
    
    else:
        return Response({'drugs': []})