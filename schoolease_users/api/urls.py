from django.urls import path
from schoolease_users.api.views import (
registration_view,getuser_view,edituser_view
)

app_name = 'user_api'

urlpatterns = [
    path('register',registration_view,name="register"),
    path('<slug>',getuser_view,name="details"),
    path('edituser/<slug>',edituser_view,name="edituser")
]