from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("search", views.search, name="search"),
    path("create", views.create_entry, name="create_entry"),
    path("edit/<str:title>", views.edit_entry, name="edit_entry")
]
