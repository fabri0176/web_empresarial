from django import template
from pages.models import Page


def get_page_list():
    pages = Page.objects.all()
    return pages
