"""Add and Edit Recipe pages Widget File for ingredients and instructions"""
import ast  # eval string as list

from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django import forms


class MultiInputIngredientWidget(forms.widgets.TextInput):
    """allows user to create an ingredient list"""
    template_name = 'multi_input_ingredient_widget.html'
    ingredients = 'ingredients[]'

    def render(self, name, value, attrs=None, renderer=None):
        values = []
        _value = []
        if value:

            # evaluate string as list
            _value = ast.literal_eval(value)

            values = value.replace('[', '').replace(
                ']', '').replace("'", '').split(',')
            value = values.pop(0)

        context = {'widget': {'name': 'ingredients', 'type': 'text',
                              'value': value, 'extra_values': _value}}
        return mark_safe(render_to_string(self.template_name, context=context))


class MultiInputWidget(forms.widgets.Textarea):
    """allows user to create an instruction list"""
    template_name = 'multi_input_widget.html'
    instructions = 'instructions[]'

    def render(self, name, value, attrs=None, renderer=None):
        values = []
        _value = []
        if value:

            # evaluate string as list
            _value = ast.literal_eval(value)

            values = value.replace('[', '').replace(
                ']', '').replace("'", '').split(',')
            value = values.pop(0)

        context = {'widget': {'name': 'instructions', 'type': 'text',
                              'value': value, 'extra_values': _value}}
        return mark_safe(render_to_string(self.template_name, context=context))
