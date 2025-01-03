from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Review

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
        "form":form})
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        form = ReviewForm()
        return render(request, "reviews/review.html", {
        "form":form})


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thankyou.html")
    
class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content["message"] = "This works!"
        return content
    
class ReviewList(ListView):
    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

    
    
class SingleReview(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
        