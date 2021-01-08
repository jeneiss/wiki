from django.shortcuts import render

from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/not_found.html", {
            "title": title
        })

    return render(request, "encyclopedia/entry.html", {
        "title": title.upper(),
        "entry": markdown(entry)
    })
