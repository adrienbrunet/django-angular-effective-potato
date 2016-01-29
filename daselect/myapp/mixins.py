from djangular.forms import NgModelFormMixin, NgFormValidationMixin
from djangular.styling.bootstrap3.forms import Bootstrap3ModelForm


class AngularModelFormMixin(NgModelFormMixin, NgFormValidationMixin, Bootstrap3ModelForm):
    pass
