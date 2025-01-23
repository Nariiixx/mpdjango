
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://nariiixx.github.io/mpdjango/', include('estoque_online.urls'))
]
