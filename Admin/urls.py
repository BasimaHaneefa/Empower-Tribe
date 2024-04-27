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
    path('Assign/<int:id>',views.Assign,name="Assign"),
    path('editteam/<int:id>',views.editteam,name="editteam"),
    path('delteam/<int:id>',views.delteam,name="delteam"),

    path('AssignedTeams/',views.AssignedTeams,name="AssignedTeams"),
    path('MemberRegistration/<int:id>',views.MemberRegistration,name="MemberRegistration"),


    path('category/',views.category,name="category"),
    path('editcat/<int:id>',views.editcat,name="editcat"),
    path('delcat/<int:id>',views.delcat,name="delcat"),

]