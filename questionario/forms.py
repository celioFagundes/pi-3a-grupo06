from django import forms
from perguntas.models import Pergunta

class ResponderQuestionarioForm(forms.Form):
    def __init__(self, *args, **kwargs):
        perguntas = kwargs.pop('perguntas')
        super().__init__(*args, **kwargs)

        for pergunta in perguntas:
            self.fields[f'pergunta_{pergunta.id}'] = forms.ChoiceField(
                label=pergunta.texto,
                choices=[('True', 'Sim'), ('False', 'Não')],
                widget=forms.RadioSelect,
                required=True
            )