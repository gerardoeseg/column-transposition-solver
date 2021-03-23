from pathlib import Path

from ga.cipher import encrypt, decrypt
from ga.ga import ga_string


def _count_words(word_list, text):
    # Count the number of common words in `text`
    return sum(text.count(word.upper()) for word in word_list)


KEY = "ZEBRAS"
PLAINTEXT = "WEAREDISCOVEREDFLEEATONCE"
WORDS = Path('words.txt').read_text().splitlines()
CIPHER = (encrypt(KEY, PLAINTEXT))


def score(candidate):
    """ Determine the fitness of candidate string `candidate`

    The fitness for a plaintext candidate is determined as the number of words
    (including overlap) from the list of 1000 most common English words.
    """
    return _count_words(WORDS, decrypt(candidate, CIPHER))


best_guess = ga_string(
        score,
        str_len=6,
        n_generations=500,
        gen_size=50,
        n_survivors=10,
        mutation_rate=4

)

# Should print some key and the original plaintext (with padding)
# Works most of the time
print(best_guess, decrypt(best_guess, CIPHER))
