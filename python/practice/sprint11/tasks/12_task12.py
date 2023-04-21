from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    freq_longer = {}
    for c in longer:
        freq_longer[c] = freq_longer.get(c, 0) + 1

    for c in shorter:
        freq_longer[c] -= 1

    for c in freq_longer:
        if freq_longer[c] == 1:
            return c
    return None


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
