from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == "POST":
        username_sent = request.POST["username"]
        print(username_sent)
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html")

def thank_you(request):
    return render(request, "reviews/thankyou.html")