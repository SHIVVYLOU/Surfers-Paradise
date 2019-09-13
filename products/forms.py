from djang import forms
from .models import Product


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'content', 'image', 'tag', 'published_date')