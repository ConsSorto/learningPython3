from django import forms
from django.core import validators

class FormArticle(forms.Form):
    tittle = forms.CharField(
        label= "Ingrese el titulo :",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs = { 'class':"newcclass", 
                     'id':"newid", 
                     'placeholder':"newplaceholder"
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'Error el texto es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'Caracteres no validos en el titulo', 'error_caracter')
        ]
    )

    content = forms.CharField(
        label= "Ingrese el Contenido :",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(40, 'Error el texto es demasiado largo'),
        ]
    )    

    content.widget.attrs.update({ 'class':"newcclasscontent", 
                     'id':"newidcontent", 
                     'placeholder':"newplaceholdercontent"
            })
    
    options = [(1, "SI"),(0, "NO")]

    public = forms.ChoiceField(
        choices=options,
        label="Publicado :"
    )