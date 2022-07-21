from dal import autocomplete
from source.models import Source

class SourceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Source.objects.none()

        qs = Source.objects.all()

        if self.q:
            qs = qs.filter(nom__contains=self.q)

        return qs
