from django.urls import path
from Teammember import views
app_name="Webteammember"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('family/',views.family,name="family"),
    path('familymembers/<int:id>',views.familymembers,name="familymembers"),
    path('Product/<int:id>',views.Product,name="Product"),
    path('viewproduct/',views.viewproduct,name="viewproduct"),
    

    
    
]