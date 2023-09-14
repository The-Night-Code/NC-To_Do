from django.contrib import admin
from django.urls import path
from ToDo_app.views import Home, Login, Signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('login/', Login),
    path('signup/', Signup)
]
