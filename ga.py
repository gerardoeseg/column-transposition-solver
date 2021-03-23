""" Genetic algorithm for fixed-length strings """

from random import randint, choice
from string import ascii_uppercase


def _ga_mutate(str_, charset, n=1):
    """
    Mutate string

    Take string `str_`, randomly replace `n` characters by others from
    `charset` and return the result
    """

    lst = list(str_)

    for _ in range(n):
        idx = randint(0, len(lst)-1)
        lst[idx] = choice(charset)

    return ''.join(lst)


def _ga_init(str_len, charset):
    """
    Generate a string of length `str_len` from randomly picked characters
    """
    return ''.join(choice(charset) for _ in range(str_len))


def ga_string(
    score,
    str_len=5,
    charset=ascii_uppercase,
    gen_size=20,
    n_generations=10,
    n_survivors=5,
    mutation_rate=2
   ):

    # Randomly generate initial survivors
    init = [_ga_init(str_len, charset) for _ in range(gen_size)]

    for gen in range(n_generations):

        candidates = list(init)

        for _ in range(gen_size - len(init)):
            candidates.append(
                _ga_mutate(choice(init), charset=charset, n=mutation_rate)
            )

        # Score candidates
        scores = tuple(
            (candidate, score(candidate))
            for candidate in candidates
        )

        # Sort by best
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        survivors = scores[:n_survivors]
        init = [survivor[0] for survivor in survivors]

        # TODO: Crossover
        print(scores[0])

    return init[0]
