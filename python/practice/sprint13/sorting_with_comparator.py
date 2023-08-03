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


def is_first_card_weaker(card_1, card_2):  # функция-компаратор
    return card_len_dict[card_1] < card_len_dict[card_2]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
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
print(insertion_sort_by_comparator(cards, is_first_card_weaker))
