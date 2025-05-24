# todos/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Todo.objects.all()  # Define base queryset

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)