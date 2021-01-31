from django.views.generic import ListView
from .models import Property


class Home(ListView):
    model = Property
    template_name = 'House/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["active"] = Property.objects.filter(status="A")

        return context


class SearchView(ListView):
    model = Property
    context_object_name = 'houses'
    template_name = 'House/search.html'

    def get_queryset(self):
        query = self.request.GET['query']
        date_queryset = Property.objects.filter(status="A", date__icontains=query)
        content_queryset = Property.objects.filter(status="A", content__icontains=query)
        queryset = date_queryset.union(content_queryset)
        # TODO the rest.

        return queryset
