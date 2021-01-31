from bs4 import BeautifulSoup
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('city', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Cities"


class Data(models.Model):
    allapot = [
        ('uj', 'uj'),
        ('normal', 'normal'),
        ('felujitando', 'felujitando')
    ]
    futes_choices = [
        ('gaz', 'gaz'),
        ('villany', 'villany'),
        ('kalyha', 'kalyha'),
    ]
    tajolas_choices = [
        ('E', 'E'),
        ('D', 'D'),
        ('K', 'K'),
        ('NY', 'NY')
    ]
    ingatlan_allapota = models.CharField(max_length=50, choices=allapot, blank=True, null=True)
    epites_eve = models.CharField(max_length=50, blank=True, null=True)
    komfort = models.CharField(max_length=50, blank=True, null=True)
    energiatanusitvany = models.CharField(max_length=50, blank=True, null=True)
    emelet = models.CharField(max_length=50, blank=True, null=True)
    epulet_szintjei = models.PositiveIntegerField(blank=True, null=True)
    lift = models.BooleanField(blank=True, null=True)
    belmagassag = models.PositiveIntegerField(blank=True, null=True)
    futes = models.CharField(max_length=50, choices=futes_choices, blank=True, null=True)
    legkondicionalo = models.BooleanField(blank=True, null=True)
    akadalymentesitett = models.BooleanField(blank=True, null=True)
    furdo_WC = models.BooleanField(blank=True, null=True)
    tajolas = models.CharField(max_length=50, choices=tajolas_choices, blank=True, null=True)
    kilatas = models.CharField(max_length=50, blank=True, null=True)
    kertkapcsolatos = models.BooleanField(blank=True, null=True)
    tetoter = models.BooleanField(blank=True, null=True)
    pince = models.BooleanField(blank=True, null=True)
    parkolas = models.BooleanField(blank=True, null=True)
    beepithetoseg = models.CharField(blank=True, max_length=50, null=True)
    szintteruleti_mutato = models.PositiveIntegerField(blank=True, null=True)
    brutto_szintterulet = models.PositiveIntegerField(blank=True, null=True)
    villany = models.BooleanField(blank=True, null=True)
    viz = models.BooleanField(blank=True, null=True)
    gaz = models.BooleanField(blank=True, null=True)
    csatorna = models.BooleanField(blank=True, null=True)
    telek_besorolas = models.CharField(max_length=50, blank=True, null=True)


class Category(models.Model):
    """
    Ház, lakás vagy telek például.
    """
    statuses = [
        ('E', 'Eladó'),
        ('K', 'Kiadó')
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    status = models.CharField(max_length=1, choices=statuses)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Categories"


class Property(models.Model):
    statuses = [
        ('A', 'Active'),
        ('I', 'InActive'),
        ('S', 'Sold')
    ]
    title = models.CharField(max_length=120, blank=True)
    description = tinymce_models.HTMLField()
    slug = models.CharField(max_length=60, unique=True, blank=True)
    data = models.OneToOneField(Data, on_delete=models.CASCADE, primary_key=False, blank=True, editable=True)
    status = models.CharField(max_length=1, choices=statuses)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=120, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)

    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('property-update', kwargs={'slug': self.slug})

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.description, features="html.parser")
        text = soup.get_text()
        return text

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Properties"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = CloudinaryField('image')
    description = models.CharField(max_length=120, default='', blank=True)

    def __unicode__(self):
        try:
            public_id = self.images.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s>" % public_id
