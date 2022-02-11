from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django import forms


class MultiInputIngredientWidget(forms.widgets.TextInput):
    template_name = 'multi_input_ingredient_widget.html'
    ingredients = 'ingredients[]'

    def render(self, name, value, attrs=None, renderer=None):
        context = {'widget': {'name': 'ingredients', 'type': 'text'}}
        return mark_safe(render_to_string(self.template_name, context=context))

class MultiInputWidget(forms.widgets.TextInput):
    template_name = 'multi_input_widget.html'
    instructions = 'instructions[]'

    def render(self, name, value, attrs=None, renderer=None):
        context = {'widget': {'name': 'instructions', 'type': 'text'}}
        return mark_safe(render_to_string(self.template_name, context=context))
