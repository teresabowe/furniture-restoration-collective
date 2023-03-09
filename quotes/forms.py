from django import forms
from quotes.models import Quote, QuoteCategoryDetail


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quotecategory', 'quotecategorydetail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quotecategorydetail'].queryset = QuoteCategoryDetail.objects.none()
