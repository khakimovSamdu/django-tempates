from django.urls import path
from .views import homepage, add, brend_all
urlpatterns = [
    path('home/', homepage),
    path('smartphone/add/', add),
    path('home/<brend>/', brend_all),
    
    
]