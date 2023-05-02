from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('register/', views.registerUser, name='register'),
    path('record/<int:pk>', views.record, name='record'),
    path('delete_ID/<int:pk>', views.delete_ID, name='delete_ID'),
    path('addRecord/', views.addRecord, name='addRecord'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]