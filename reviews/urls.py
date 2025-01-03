from django.urls import path
from . import views

urlpatterns = [
path("", views.ReviewView.as_view()),
path("thank-you", views.ThankYouView.as_view()),
path("reviews", views.ReviewList.as_view()),
path("singlereview/<int:pk>", views.SingleReview.as_view())
]