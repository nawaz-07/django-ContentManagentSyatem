from django.urls import path,include
from cms_app.views import UserSignupView,UserLoginView, ContentItemListCreateView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('content/', ContentItemListCreateView.as_view(), name='content-list-create'),
    # path('content/<int:pk>/', ContentItemDetailView.as_view(), name='content-detail'),
]
