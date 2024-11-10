def personal_sum(numbers):
    global incorrect_data
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError as tperr:
            incorrect_data += 1
            print(f'Некорректный тип данных дляподсчёта суммы - {i}')
    return result, incorrect_data

def calculate_average(numbers):
    global err
    avsum = 0
    try:
        avsum = personal_sum(numbers)[0] / len(numbers)
    except ZeroDivisionError as exc:
        print(f'Ошибка деления на ноль:{exc}')
        avsum = 0
    except:
        print(f'В numbers записан некорректный тип данных')
        return None
    return avsum


incorrect_data = 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

print(f'Результат 4: {calculate_average([])}')
