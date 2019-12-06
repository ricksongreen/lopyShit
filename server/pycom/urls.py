from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'toilet', views.ToiletViewSet)
router.register(r'usage', views.UsageViewSet)
router.register(r'refiller', views.RefillerViewSet)
router.register(r'refill', views.RefillViewSet)
router.register(r'tag',views.TagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', include(router.urls)),
]
