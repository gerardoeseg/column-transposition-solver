# Genetic solver for column transposition cipher

Implements a genetic algorithm solver for strings and the simple column
transposition cipher.
Solves a simple, singular column transposition cipher using the genetic
algorithm.
Probably useful if you're a spy and it's 1970.

The scoring function is the number of words (from the [list of 1000 most common
english words][word-list] by [deekayen][github-deekayen]) present in the
plaintext candidate.
Words can overlap, so 'area' will be counted twice (it contains 'are').
This makes a pretty bad metric, but works for the [example case][wiki-example]
and does not require spaces between words.

See `__main__.py` for the running example.

## Usage

There's no command line interface for the proof of concept, just edit 
`__main__.py` to use.

### Multiplication cipher

The file `cipher.py` contains:

- `encrypt(plaintext, key, pad=' ')` 
- `decrypt(plaintext, key, pad=' ')`

For your encryption/decription needs.
A custom padding character can be specified.
Using a common vowel seems to make the cipher a bit stronger against word count
attacks as it will result in more 'garbage words' in the plaintext candidates.

Satisfies the example from the [wiki][wiki-cipher]:

```python
>> print(encrypt('ZEBRAS', 'WEAREDISCOVEREDFLEEATONCE'))
EVLN0ACDT0ESEA0ROFO0DEEC0WIREE
```

### String genetic-algorithm

The file `ga.py` contains `ga_string(...)` with arguments:

- `score`: Score function, the algorithm will try to _maximise_ the function
- `str_len`: String length, default 5
- `charset`: Character set to choose mutations from. Defaults to uppercase ascii
  characters A-Z.
- `gen_size`: Total size of generation, default 20. 
- `n_generations`: Number of generations, default 10
- `n_survivors`: Number of candidates that survive the generation. Default 5.
- `mutation_rate`: Number of mutated characters per mutation.

The first generation starts with `n_survivors` fully random strings (picked from
`charset`), all subsequent generation with the `n_survivors` best-fitting
candidates from the previous generation.

Of this initial population, candidates are picked randomly and mutated such that
the total population size is always `n_mutations`.
There is no cross-over currently.

A working example is shown in `main.py`.

[word-list]: https://gist.github.com/deekayen/4148741
[wiki-cipher]: https://en.wikipedia.org/wiki/Transposition_cipher
[wiki-ga]: https://en.wikipedia.org/wiki/Genetic_algorithm
[wiki-example]: https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transpositio
