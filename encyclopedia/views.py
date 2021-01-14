from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util
from markdown2 import markdown


class NewSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=200)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewSearchForm()
    })


def entry_page(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/not_found.html", {
            "item": title,
            "form": NewSearchForm()
        })

    return render(request, "encyclopedia/entry.html", {
        "title": title.upper(),
        "entry": markdown(entry),
        "form": NewSearchForm()
    })


def search(request):
    form = NewSearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data["query"]
        entries = util.list_entries()

        if query not in (entry.lower() for entry in entries):
            matching_entries = [entry for entry in entries if query in entry.lower()]

            if matching_entries:
                return render(request, "encyclopedia/search_results.html", {
                    "entries": matching_entries,
                    "form": NewSearchForm()
                })
            else:
                return render(request, "encyclopedia/not_found.html", {
                    "item": query,
                    "form": NewSearchForm()
                })

        return HttpResponseRedirect(f"wiki/{query}")
    else:
        return render(request, "", {
            "form": NewSearchForm()
        })


