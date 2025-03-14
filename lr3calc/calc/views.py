from django.shortcuts import render
from .forms import CalculatorForm, SinCalculatorForm
from .logic import calculate, calculate_sin

def index(request):
    calc_result = None
    sin_result = None

    if request.method == "POST":
        if "calculate" in request.POST:  # Если отправили первую форму
            calc_form = CalculatorForm(request.POST)
            sin_form = SinCalculatorForm()  # Пустая форма для синуса

            if calc_form.is_valid():
                num1 = calc_form.cleaned_data["num1"]
                num2 = calc_form.cleaned_data["num2"]
                operation = calc_form.cleaned_data["operation"]
                calc_result = calculate(num1, num2, operation)

        elif "calculate_sin" in request.POST:  # Если отправили вторую форму
            sin_form = SinCalculatorForm(request.POST)
            calc_form = CalculatorForm()  # Пустая форма для обычных вычислений

            if sin_form.is_valid():
                angle = sin_form.cleaned_data["angle"]
                sin_result = calculate_sin(angle)


    else:
        calc_form = CalculatorForm()
        sin_form = SinCalculatorForm()

    return render(request, "calc/index.html", {
        "calc_form": calc_form,
        "sin_form": sin_form,
        "calc_result": calc_result,
        "sin_result": sin_result,
    })