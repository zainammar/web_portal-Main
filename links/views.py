from django.shortcuts import render, get_object_or_404
from .models import PageLink

def page_link(request, slug):
    page = get_object_or_404(PageLink, slug=slug)
    return render(request, 'links/page_link.html', {'page': page})
