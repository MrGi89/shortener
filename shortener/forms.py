import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError


from django.forms import ModelForm, ValidationError
from shortener.models import UrlModel


class UrlForm(ModelForm):

    class Meta:
        model = UrlModel
        fields = ('url', )

    def clean_url(self):
        """
        Checks if url is valid. Raises Validation error if response code is other than success or redirect
        """
        url = self.cleaned_data['url']
        session = requests.Session()
        session.mount(url, HTTPAdapter(max_retries=3))
        try:
            response = session.get(url, timeout=(5, 10))
            if response.status_code < 200 or response.status_code > 399:
                raise ConnectionError
        except (ConnectionError, TimeoutError):
            raise ValidationError('Bad url - connection error')
        return url
