from .mixins import AngularModelFormMixin
from .models import Child


class ChildForm(AngularModelFormMixin):
    scope_prefix = 'dj_child'
    form_name = 'child_form'

    class Meta:
        model = Child
        fields = ('parent', )
