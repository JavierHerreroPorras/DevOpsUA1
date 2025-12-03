from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=80)
    short_bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    max_capacity = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name


class Edition(models.Model):
    year = models.PositiveIntegerField(unique=True)
    theme = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"FLORA {self.year}"


class Installation(models.Model):
    title = models.CharField(max_length=150)
    opening_date = models.DateField()
    short_description = models.TextField(blank=True)
    materials = models.CharField(max_length=250)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="installations")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="installations")
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name="installations")

    class Meta:
        unique_together = ("title", "edition")

    def __str__(self):
        return f"{self.title} ({self.artist.name})"

