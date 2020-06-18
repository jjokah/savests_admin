from django import forms


class EmailPostForm(forms.Form):
    message = forms.CharField(required=False, widget=forms.Textarea)
