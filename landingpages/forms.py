from .models import ContatoForm
from django import forms

#styling e opções do fomulário de contato. Form control total no back-end
class Formulario(forms.ModelForm):
    class Meta:
        model = ContatoForm
        fields = '__all__'

        ESCOLHASHOTEL = (
            ('', 'Escolha sua opção'),
            ('Hotel 1','Opção 1'),
            ('Hotel 1','Opção 2'),
            ('Hotel 1', 'Opção 3'),
            ('Quero outras opçoes de hotéis', 'Quero outras opçoes de hotéis')
        )

        ESCOLHASQUARTOS = (
            ('', 'Escolha sua opção'),
            ('1 Adulto', '1 Adulto'),
            ('2 Adultos', '2 Adultos'),
            ('2 Adultos + 1 criança', '2 Adultos + 1 criança'),
            ('2 Adultos + 2 crianças', '2 Adultos + 2 crianças'),
            ('Somos em mais pessoas!', 'Somos em mais pessoas!'),
        )


        widgets = {
                    'hotel_pref': forms.Select(choices=ESCOLHASHOTEL, attrs={'class':'form-control'}),
                    'quarto_pref': forms.Select(choices=ESCOLHASQUARTOS, attrs={'class':'form-control'}),
                    'nome_1': forms.TextInput(attrs={'placeholder': 'Nome Completo + Sobrenome Completo', 'class': 'form-control'}),
                    'nome_2': forms.TextInput(attrs={'placeholder': 'Nome Completo + Sobrenome Completo', 'class': 'form-control'}),
                    'nome_3': forms.TextInput(attrs={'placeholder': 'Nome Completo + Sobrenome Completo', 'class': 'form-control'}),
                    'nome_4': forms.TextInput(attrs={'placeholder': 'Nome Completo + Sobrenome Completo', 'class': 'form-control'}),


                    'data_nascimento_1': forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa', 'class': 'form-control', 'type':'date'}),
                    'data_nascimento_2': forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa', 'class': 'form-control', 'type':'date'}),
                    'data_nascimento_3': forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa', 'class': 'form-control', 'type':'date'}),
                    'data_nascimento_4': forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa', 'class': 'form-control', 'type':'date'}),


                'email_contato': forms.EmailInput(attrs={'placeholder': 'exemplo@exemplo.com', 'class': 'form-control'}),
                'telefone_contato': forms.TextInput(attrs={'placeholder': '+xxx-xxx-xxxxxxxxxxx', 'class': 'form-control'}),
        }