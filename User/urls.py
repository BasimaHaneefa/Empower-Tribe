from django.urls import path
from User import views
app_name="Webuser"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('viewproduct/',views.viewproduct,name="viewproduct"),
    
]