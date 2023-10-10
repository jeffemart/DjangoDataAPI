from django.urls import path, include
from rest_framework import routers
from myapi.views import ChamadoViewSet

router = routers.DefaultRouter()
router.register(r'chamados', ChamadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
