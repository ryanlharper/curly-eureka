"""model_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from model_manager.views import SignUpView
from investment.views import add_strategy, strategies_list, transactions_list, create_transaction
from investment.views import positions

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('add_strategy/', add_strategy, name='add_strategy'),
    path('strategies/', strategies_list, name='strategies_list'),
    path('transactions/', transactions_list, name='transactions_list'),
    path('create_transaction/', create_transaction, name='create_transaction'),      
    path('positions/<int:strategy_id>/', positions, name='positions'),
]