# coding=utf-8
"""Section forms."""

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Field,
    Submit,
)

from lesson.models.section import Section


class SectionForm(ModelForm):
    """Form for creating section"""

    class Meta:
        model = Section
        fields = (
            'section_number',
            'name',
            'notes'
        )

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project')
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Section details'),
                Field('section_number', css_class='form_control'),
                Field('name', css_class='form_control'),
                Field('notes', css_class='form_control'),

                css_id='project-form'
            )
        )

        self.helper.layout = layout
        self.helper.html5_required = False

        super(SectionForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super(SectionForm, self).save(commit=False)
        instance.project = self.project
        instance.save()
        return instance
