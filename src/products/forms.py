from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "your title"
            }
        )
    )
    email = forms.EmailField()
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new_class_name two",
                "placeholder": "your description",
                "id": "my_id_text_area",
                "rows": 15,
                "cols": 120
            }
        )
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'email',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
            

class RawProductForm(forms.Form):

    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "your title"
            }
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "new_class_name two",
                "placeholder": "your description",
                "id": "my_id_text_area",
                "rows": 15,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)