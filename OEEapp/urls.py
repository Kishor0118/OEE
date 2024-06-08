from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, ProductionLogViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'productionlogs', ProductionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('machines/<int:pk>/calculate_oee/', MachineViewSet.as_view({'get': 'calculate_oee'}), name='calculate_oee'),
]
