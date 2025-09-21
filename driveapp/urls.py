from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login, name="login"),
    path("signup/",views.SignUp,name="signup"),
    path("folder/<int:folderid>/",views.folder, name="folder"),
    path("addFolder/", views.addfolder, name="addfolder"),
    path("logout/", views.Logout, name="logout"),
    path("folder/<int:folder_id>/update/", views.update_folder, name="update_folder"),
    path("folder/<int:folder_id>/delete/", views.delete_folder, name="delete_folder"),
    
]
