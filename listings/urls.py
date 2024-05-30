from django.urls import path
from .views import ListingListCreateView, ReviewListCreateView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view()),
    path('listings/<int:pk>/', ListingListCreateView.as_view()),
    path('listings/<int:listing_key>/reviews/', ReviewListCreateView.as_view()),
]
