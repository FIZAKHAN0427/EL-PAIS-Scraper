import re
from collections import Counter


def find_repeated_words(titles, min_count=2):
    """
    Find words repeated min_count or more times across translated titles
    """

    all_words = []

    for title in titles:

        if not title:
            continue

        text = title.lower()

        # remove punctuation
        text = re.sub(r"[^\w\s]", "", text)

        words = text.split()

        all_words.extend(words)

    word_counts = Counter(all_words)

    repeated = {
        word: count
        for word, count in word_counts.items()
        if count >= min_count
    }

    return repeated