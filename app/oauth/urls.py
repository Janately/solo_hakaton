from django.contrib.auth import views as auth_views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserAPIView,
                    CreateTokenView,
                    AgentAPIView,
                    AddWishlistView,
                    AdsInUserWishListView,
                    AdsInUserWishListDetailView, AgentInfoViewSet)

router = DefaultRouter()

router.register(r'agents', AgentInfoViewSet, basename='agents')

urlpatterns = [
    path('register/', UserAPIView.as_view(), name='create-user'),
    path('become-agent/', AgentAPIView.as_view(), name='create-agent'),
    path('login/', CreateTokenView.as_view(), name='token'),
    path('add-wishlist/<int:pk>/', AddWishlistView.as_view(), name='add-wishlist'),
    path('wishlist/', AdsInUserWishListView.as_view(), name='user-wishlist'),
    path('ads-details/<int:pk>/', AdsInUserWishListDetailView.as_view(), name='ads-detail')

]
# urlpatterns += router.urls
