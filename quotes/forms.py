from django import forms
from quotes.models import Quote, QuoteCategoryDetail


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('quotecategory', 'quotecategorydetail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quotecategorydetail'].queryset = QuoteCategoryDetail.objects.none()

        if 'quotecategory' in self.data:
            try:
                quotecategory_id = int(self.data.get('quotecategory'))
                self.fields['quotecategorydetail'].queryset = QuoteCategoryDetail.objects.filter(quotecategory_id=quotecategory_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['quotecategorydetail'].queryset = self.instance.quotecategory.name.order_by('name')
