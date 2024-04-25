from django.urls import path
from Admin import views
app_name="Webadmin"

urlpatterns = [
    path('localbodytype/',views.localbodytype,name="localbodytype"),
    path('editbodytype/<int:id>',views.editbodytype,name="editbodytype"),
    path('delloctype/<int:id>',views.delloctype,name="delloctype"),

    path('localbody/',views.localbody,name="localbody"),
    path('editloc/<int:id>',views.editloc,name="editloc"),
    path('delloc/<int:id>',views.delloc,name="delloc"),

    path('ward/',views.ward,name="ward"),
    path('editward/<int:id>',views.editward,name="editward"),
    path('delward/<int:id>',views.delward,name="delward"),

    path('donation/',views.donation,name="donation"),
    path('editdonationtype/<int:id>',views.editdonationtype,name="editdonationtype"),
    path('deldonationtype/<int:id>',views.deldonationtype,name="deldonationtype"),

    path('team/',views.team,name="team"),

]