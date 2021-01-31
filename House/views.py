from django.views.generic import ListView
from .models import Property, PropertyImage


class Home(ListView):
    model = Property
    context_object_name = 'houses'
    template_name = 'House/index.html'
    queryset = Property.objects.filter(status="A")


class SearchView(ListView):
    model = Property
    context_object_name = 'houses'
    template_name = 'House/search.html'

    def get_queryset(self):
        query = self.request.GET['query']
        date_queryset = Property.objects.filter(status="A", date__icontains=query)
        description_queryset = Property.objects.filter(status="A", description__icontains=query)
        queryset = date_queryset.union(description_queryset)
        # TODO the rest.

        return queryset
