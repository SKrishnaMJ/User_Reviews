from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=26, label="Your Name", error_messages={
        "max_length":"Please enter a shorter name",
        "required":"Dont leave your name field empty"
    })
