from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # ARTISTAS
    path("artists/", views.artist_list, name="artist_list"),
    path("artists/<int:artist_id>/", views.artist_detail, name="artist_detail"),
    path("artists/create/", views.artist_create, name="artist_create"),
    path("artists/<int:artist_id>/edit/", views.artist_edit, name="artist_edit"),
    path("artists/<int:artist_id>/delete/", views.artist_delete, name="artist_delete"),

    # INSTALLATIONS
    path("installations/", views.installation_list, name="installation_list"),
    path("installations/<int:installation_id>/", views.installation_detail, name="installation_detail"),
    path("installations/create/", views.installation_create, name="installation_create"),

    # VENUES
    path("venues/", views.venue_list, name="venue_list"),
    path("venues/<int:venue_id>/", views.venue_detail, name="venue_detail"),
    path("venues/create/", views.venue_create, name="venue_create"),

    # EDITIONS
    path("editions/", views.edition_list, name="edition_list"),
    path("editions/<int:edition_id>/", views.edition_detail, name="edition_detail"),
    path("editions/create/", views.edition_create, name="edition_create"),
]
