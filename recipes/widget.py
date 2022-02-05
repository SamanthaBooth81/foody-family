from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django import forms


class MultiInputWidget(forms.widgets.TextInput):
    template_name = 'multi_input_widget.html'

    def render(self, name, value, attrs=None, renderer=None):
        print('Custom widget')
        return mark_safe(render_to_string(self.template_name))
