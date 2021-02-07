from django.db.models import Count
from django.views.generic import ListView
from .models import Property, PropertyImage, City, Category, Types


class Home(ListView):
    model = Property
    context_object_name = 'houses'
    template_name = 'House/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cites'] = City.objects.all()
        context['categories'] = Category.objects.all()
        context['types'] = Types.objects.all()

        return context


class SearchView(ListView):
    model = Property
    context_object_name = 'houses'
    template_name = 'House/search.html'

    def get_queryset(self):
        min_size = self.request.GET['min']
        max_size = self.request.GET['max']
        city = self.request.GET['cities']
        prop_type = self.request.GET['types']
        prop_cat = self.request.GET['categories']

        if not min_size:
            min_size = 0
        if not max_size:
            max_size = 9999
        size_queryset = Property.objects.filter(status='A', data__meret__gte=min_size, data__meret__lte=max_size)
        if not city:
            city_queryset = Property.objects.filter(status='A')
        else:
            city_queryset = Property.objects.filter(status='A', city__name__icontains=city)

        type_query = Property.objects.filter(status='A', types__status=prop_type)
        cat_query = Property.objects.filter(status='A', category__status=prop_cat)
        # date_queryset = Property.objects.filter(status="A", date__icontains=query)
        # description_queryset = Property.objects.filter(status="A", description__icontains=query)
        queryset = city_queryset.intersection(size_queryset).intersection(type_query).intersection(cat_query)
        # TODO the rest.

        return queryset
