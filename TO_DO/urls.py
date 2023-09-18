from django.contrib import admin
from django.urls import path
from ToDo_app.views import Home, LoginU, SignupU,LogoutU,StickyWall, TaskList, TopPriorities, Reminder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('login/', LoginU),
    path('signup/', SignupU),
    path('logout/', LogoutU),
    
    path('tasklist/', TaskList),
    path('toppriorities/', TopPriorities),
    path('reminder/', Reminder),
    path('stickywall/', StickyWall)
    
    
]
