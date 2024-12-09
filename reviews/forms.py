from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=26, label="Your Name", error_messages={
#         "max_length":"Please enter a shorter name",
#         "required":"Dont leave your name field empty"
#     })
#     review_feedback = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': "Your Name",
            'review_text': "Your Feedback",
            'rating': "Your Rating"
        }
        error_messages = {
            'user_name':{
                'required': "Username is required",
                'max_length': "Enter a valid/shorter username"
            }
        }

