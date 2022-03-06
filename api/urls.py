from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import StudentViewSet,StudentInfosViewSet

router = DefaultRouter()

router.register(r'students', StudentViewSet, basename="students-api")
router.register(r'students-infos', StudentInfosViewSet, basename="students-secured-api")


urlpatterns = [
    path('', include(router.urls)),
]