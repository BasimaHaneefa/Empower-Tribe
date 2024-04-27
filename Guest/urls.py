from django.urls import path
from Guest import views
app_name="Webguest"

urlpatterns = [
        path('userreg/',views.UserRegistration,name="userreg"),
        path('login/',views.Login,name="login"),

]