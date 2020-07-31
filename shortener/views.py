from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.utils.crypto import get_random_string
from shortener.forms import UrlForm
from shortener.models import UrlModel


class UrlView(View):

    def get(self, request):
        return render(request, 'base.html', context={})

    def post(self, request):

        form = UrlForm(data=request.POST)
        if form.is_valid():
            # check if url exists in DB
            try:
                url = UrlModel.objects.get(url=form.cleaned_data['url'])
            except UrlModel.DoesNotExist:
                url = form.save(commit=False)
                # generates random slug
                slug = get_random_string(length=6)
                while UrlModel.objects.filter(slug=slug).exists():
                    slug = get_random_string(length=6)
                url.slug = slug
                url.save()
            return render(request, 'base.html', context={'new_url': url})
        return render(request, 'base.html', context={'form_errors': form.errors})


class UrlRedirectView(View):

    def get(self, request, slug):

        try:
            url = UrlModel.objects.get(slug=slug)
        except UrlModel.DoesNotExist:
            raise Http404
        return redirect(url.url)
