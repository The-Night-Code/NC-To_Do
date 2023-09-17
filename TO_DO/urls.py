from django.contrib import admin
from django.urls import path
from ToDo_app.views import Home, LoginU, SignupU,LogoutU,StickyWall
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('login/', LoginU),
    path('signup/', SignupU),
    path('logout/', LogoutU),
    path('stickywall/', StickyWall)
]
