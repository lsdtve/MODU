from accounts.models import Trainer, Client
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TrainerSerializer, TrainerCommentSerialiezr
from ..models import TrainerComment

class TrainerView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(APIView):
    def get(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

    def put(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerCommentView(generics.ListCreateAPIView):
    queryset = TrainerComment.objects.all()
    serializer_class = TrainerCommentSerialiezr

    def post(self, request, pk, format=None):
        serializer = TrainerCommentSerialiezr(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer=pk, client=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)