from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('expenses/', views.expenses_page, name='expenses_page'),
    path('add-expense/', views.add_expense_page, name='add_expense_page'),
    path('',views.expenses_page,name='home'),
    
    path('api/auth/register/', RegisterView.as_view(), name='api_register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
