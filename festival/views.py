from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Artist, Installation, Venue, Edition

def artist_list(request):
    """Listado de artistas + filtro por país"""
    country = request.GET.get("country")
    artists = Artist.objects.all()

    if country:
        artists = artists.filter(country__icontains=country)

    return render(request, "festival/artist_list.html", {
        "artists": artists,
        "country": country,
    })


def artist_detail(request, artist_id):
    """Detalle del artista + sus instalaciones"""
    artist = get_object_or_404(Artist, id=artist_id)
    installations = artist.installations.all()

    return render(request, "festival/artist_detail.html", {
        "artist": artist,
        "installations": installations,
    })


def artist_create(request):
    """Crear artista"""
    if request.method == "POST":
        name = request.POST.get("name")
        country = request.POST.get("country")
        bio = request.POST.get("short_bio")
        website = request.POST.get("website")

        Artist.objects.create(
            name=name,
            country=country,
            short_bio=bio,
            website=website
        )
        return redirect("artist_list")

    return render(request, "festival/artist_form.html")


def artist_edit(request, artist_id):
    """Editar artista"""
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.name = request.POST.get("name")
        artist.country = request.POST.get("country")
        artist.short_bio = request.POST.get("short_bio")
        artist.website = request.POST.get("website")
        artist.save()
        return redirect("artist_detail", artist_id=artist.id)

    return render(request, "festival/artist_form.html", {"artist": artist})


def artist_delete(request, artist_id):
    """Eliminar artista"""
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.delete()
        return redirect("artist_list")

    return render(request, "festival/artist_delete.html", {"artist": artist})


def installation_list(request):
    """Listado con filtro por edición y ordenación"""
    edition_year = request.GET.get("edition")
    order = request.GET.get("order")

    installations = Installation.objects.all()

    if edition_year:
        installations = installations.filter(edition__year=edition_year)

    if order == "desc":
        installations = installations.order_by("-opening_date")
    else:
        installations = installations.order_by("opening_date")

    return render(request, "festival/installation_list.html", {
        "installations": installations,
        "edition_year": edition_year,
        "order": order,
    })


def installation_detail(request, installation_id):
    """Detalle de instalación"""
    inst = get_object_or_404(Installation, id=installation_id)

    return render(request, "festival/installation_detail.html", {
        "installation": inst
    })


def installation_create(request):
    """Crear instalación"""
    artists = Artist.objects.all()
    venues = Venue.objects.all()
    editions = Edition.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        opening_date = request.POST.get("opening_date")
        desc = request.POST.get("short_description")
        materials = request.POST.get("materials")
        artist_id = request.POST.get("artist")
        venue_id = request.POST.get("venue")
        edition_id = request.POST.get("edition")

        Installation.objects.create(
            title=title,
            opening_date=opening_date,
            short_description=desc,
            materials=materials,
            artist_id=artist_id,
            venue_id=venue_id,
            edition_id=edition_id,
        )
        return redirect("installation_list")

    return render(request, "festival/installation_form.html", {
        "artists": artists,
        "venues": venues,
        "editions": editions,
    })


def venue_list(request):
    venues = Venue.objects.all()
    return render(request, "festival/venue_list.html", {"venues": venues})


def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    installations = venue.installations.all()

    return render(request, "festival/venue_detail.html", {
        "venue": venue,
        "installations": installations
    })


def venue_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        description = request.POST.get("description")
        capacity = request.POST.get("max_capacity")

        Venue.objects.create(
            name=name,
            address=address,
            description=description,
            max_capacity=capacity
        )
        return redirect("venue_list")

    return render(request, "festival/venue_form.html")


def edition_list(request):
    editions = Edition.objects.all()
    return render(request, "festival/edition_list.html", {"editions": editions})


def edition_detail(request, edition_id):
    edition = get_object_or_404(Edition, id=edition_id)
    installations = edition.installations.all()

    return render(request, "festival/edition_detail.html", {
        "edition": edition,
        "installations": installations
    })


def edition_create(request):
    if request.method == "POST":
        year = request.POST.get("year")
        theme = request.POST.get("theme")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        Edition.objects.create(
            year=year,
            theme=theme,
            start_date=start_date,
            end_date=end_date
        )
        return redirect("edition_list")

def home(request):
    return render(request, "festival/home.html")

