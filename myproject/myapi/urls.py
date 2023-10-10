from django.urls import path, include
from rest_framework import routers
from myapi.views import MyModelViewSet, ChamadoViewSet

router = routers.DefaultRouter()
router.register(r'mymodel', MyModelViewSet)
router.register(r'chamados', ChamadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
