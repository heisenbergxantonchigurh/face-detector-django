from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField(required=False)
    url = forms.URLField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        url = cleaned_data.get('url')

        if not image and not url:
            raise forms.ValidationError('You must provide either an image file or an image URL.')

        return cleaned_data
