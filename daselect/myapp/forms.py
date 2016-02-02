from .mixins import AngularModelFormMixin
from .models import Child


class ChildForm(AngularModelFormMixin):
    scope_prefix = 'dj_child'
    form_name = 'child_form'

    class Meta:
        model = Child
        fields = ('parent', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs['ng-options'] = "prent.pk as parent.name for parent in parents"
