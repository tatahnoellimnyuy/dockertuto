from django import forms




class Contactform(forms.Form):
     Name= forms.CharField(required=False)
     Email= forms.EmailField(required=True)
     subject = forms.CharField(required=True)
     message = forms.CharField(widget=forms.Textarea(attrs={
            'rows': 4
        }), required=True)



