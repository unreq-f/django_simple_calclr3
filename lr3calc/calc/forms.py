from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="Перше число", required=True)
    num2 = forms.FloatField(label="Друге число", required=True)
    operation = forms.ChoiceField(
        choices=[("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")],
        label="Операція"

    )
class SinCalculatorForm(forms.Form):
    angle = forms.FloatField(label="Угол (градусы)", min_value=0, max_value=360)
