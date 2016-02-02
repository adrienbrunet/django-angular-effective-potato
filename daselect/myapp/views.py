from django.views.generic import ListView, FormView

from rest_framework import viewsets

from .forms import ChildForm
from .models import Child, Parent
from .serializers import ChildSerializer, ParentSerializer


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


class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer

    def get_queryset(self):
        return Parent.objects.all()
