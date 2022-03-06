from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import StudentViewSet,StudentInfosViewSet

router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'students-infos', StudentInfosViewSet)


urlpatterns = [
    path('', include(router.urls)),
]