from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    opt_text = re.sub(r'[^\w\s]', '', text)
    min_word, max_word = None, None
    if not opt_text.split():
        return min_word, max_word

    min_len = min(len(word) for word in opt_text.split())
    max_len = max(len(word) for word in opt_text.split())

    for word in opt_text.split():
        if len(word) == min_len:
            min_word = word
            break
    for word in opt_text.split():
        if len(word) == max_len:
            max_word = word
            break
    return min_word, max_word
