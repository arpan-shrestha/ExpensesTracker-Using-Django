from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, Register
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
# Create your views here.

class auth(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [auth]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ExpenseIncome.objects.all().order_by('-created_at')
        return ExpenseIncome.objects.filter(user=user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = Register(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User register successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def register_page(request):
    return render(request, 'register.html')
def login_page(request):
    return render(request, 'login.html')
def expenses_page(request):
    return render(request,'expenses.html')
def add_expense_page(request):
    return render(request, 'add_expense.html')
