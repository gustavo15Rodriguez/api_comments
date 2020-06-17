from django import forms

from api_comments.apps.comments.models import Choice


class VoteForm(forms.ModelForm):

    class Meta:
        model = Choice

        fields = "__all__"

        labels = {
            'pregunta': 'question',
            'respuesta': 'choice_text',
            'votos': 'votes',
        }

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
