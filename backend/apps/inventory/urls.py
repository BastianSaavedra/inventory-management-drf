from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Inventory API")),
]
