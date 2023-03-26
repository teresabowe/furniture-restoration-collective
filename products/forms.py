from django import forms
from products.models import Product, Subcategory, Category


class ProductQuoteForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'name', 'price', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.name.order_by('name')
