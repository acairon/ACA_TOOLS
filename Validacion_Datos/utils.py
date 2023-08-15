import re
import datetime

# Función para validar un correo electrónico
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Función para formatear un número de teléfono
def format_phone_number(phone):
    cleaned_phone = re.sub(r'\D', '', phone)  # Elimina todos los caracteres que no sean dígitos
    if len(cleaned_phone) == 10:
        return f"({cleaned_phone[:3]}) {cleaned_phone[3:6]}-{cleaned_phone[6:]}"
    elif len(cleaned_phone) == 11 and cleaned_phone.startswith('1'):
        return f"1 ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:]}"
    else:
        return "Número de teléfono inválido"

# Función para validar una fecha en formato 'YYYY-MM-DD'
def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Función para validar un número de tarjeta de crédito utilizando el algoritmo de Luhn
def validate_credit_card(card_number):
    cleaned_card_number = re.sub(r'\s', '', card_number)  # Elimina espacios en blanco
    if re.match(r'^\d{16}$', cleaned_card_number) is not None:
        return luhn_algorithm(cleaned_card_number)
    return False

# Algoritmo de Luhn para validar números de tarjeta de crédito
def luhn_algorithm(number):
    total = 0
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        digit_value = int(digit)
        if i % 2 == 1:
            digit_value *= 2
            if digit_value > 9:
                digit_value -= 9
        total += digit_value
    return total % 10 == 0

# Función para validar una dirección IP
def validate_ip_address(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

# Función para validar un código postal
def validate_postal_code(postal_code):
    pattern = r'^\d{5}$'
    return re.match(pattern, postal_code) is not None
