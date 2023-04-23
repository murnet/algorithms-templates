def is_power_of_four(number: int) -> bool:
    # Здесь реализация вашего решения
    if number % 4 == 0:
        return True
    return False

print(is_power_of_four(int(input())))