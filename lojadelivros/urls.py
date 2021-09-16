from django.contrib import admin
from django.urls import path, include

from livros.urls import livros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include(livros_urls))
]
