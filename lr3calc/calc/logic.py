import math

def format_result(value):
    """Форматирование числа с 3 знаками после запятой без использования round"""
    value_str = str(value)
    if "." in value_str:
        integer_part, decimal_part = value_str.split(".")
        decimal_part = decimal_part[:3]  # Ограничиваем до 3 знаков
        return f"{integer_part}.{decimal_part}" if decimal_part else integer_part
    return value_str


def calculate(num1, num2, operation):
    """Функция для выполнения арифметических операций"""
    try:
        num1, num2 = float(num1), float(num2)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            result = num1 / num2

        else:
            return "Ошибка: неизвестная операция"

        return format_result(result)  # Применяем форматирование
    except ValueError:
        return "Ошибка: некорректные данные"


def calculate_sin(angle):
    radians = math.radians(angle)  # Переводим градусы в радианы
    return format_result(math.sin(radians))
