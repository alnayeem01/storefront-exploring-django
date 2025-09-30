from django.urls import path # path from django
from . import views #imort the view from current directory 


#an special urlpatterns that django will look for
#URLConf
urlpatterns = [
    path('hello/', views.hello_world) #passing the route and view 
]
