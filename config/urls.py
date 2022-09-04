from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login",include('base.urls'), name="home"),
    path("usuarios/",include('usuarios.urls'),name="usuarios"),
    path('checkout/',include("pagamentos.urls"),name="checkout"),
    path("",include("agendamentos.urls"),name="agendamento"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
