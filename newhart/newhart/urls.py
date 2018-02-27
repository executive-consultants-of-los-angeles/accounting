"""newhart URL Configuration"""
# pylint: disable=invalid-name
from django.contrib import admin
from django.urls import path
from chart import views
from account import views as account_views

"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('', views.index, name='home'),
    path('account/', account_views.index, name='accounts_list'),
    path('account/edit/<int:account_id>',
         account_views.index,
         name='edit_account'),
    path('account/update/<int:account_id>',
         account_views.update,
         name='update_account'),
    path('account/delete/<int:account_id>',
         account_views.delete, name='delete_account'),
    path('admin/', admin.site.urls),
]
