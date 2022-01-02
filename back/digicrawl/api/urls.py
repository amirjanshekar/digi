from .views import ApiList
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api', ApiList)


urlpatterns = [
    path('', include(router.urls)),
    path('/<int:id>/', include(router.urls)),
]
