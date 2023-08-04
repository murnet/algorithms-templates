card_name = [
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять',
    'десять',
    'одинадцать',
]
card_len_dict = {card: len(card) for card in card_name}


def card_strength(card):  # ключ сравнения
    return [-card_len_dict[card], card]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(array, key):
    for i in range(1, len(array)):
        card = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and key(card) < key(array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = card
    return array


cards = [
    'два',
    'одинадцать',
    'девять',
    'пять',
    'восемь',
    'три',
    'семь',
    'десять',
    'четыре',
    'один',
    'шесть',
]
print(insertion_sort_by_key(cards, card_strength))
