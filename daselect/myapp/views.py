from django.views.generic import ListView, FormView

from rest_framework import viewsets

from .forms import ChildForm
from .models import Child
from .serializers import ChildSerializer


class ChildList(ListView):
    model = Child


class ChildEdit(FormView):
    template_name = 'child_form.html'
    model = Child
    form_class = ChildForm
    success_url = '/'


class ChildViewSet(viewsets.ModelViewSet):
    serializer_class = ChildSerializer

    def get_queryset(self):
        return Child.objects.all()
