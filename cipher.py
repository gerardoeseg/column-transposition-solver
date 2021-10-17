""" Transposition cypher encrypt/decrypt """

def encrypt(key, plaintext, pad=' '):
    key_len = len(key)

    rows = _to_rows(key_len, plaintext, pad=' ')
    order = _to_order(key)

    # Transpose
    columns = tuple(''.join(
            row[order.index(i)] for row in rows
        )
        for i in range(key_len)
    )

    return ''.join(columns)



def decrypt(key, cipher, pad=' '):
    key_len = len(key)
    row_len = len(cipher) // key_len

    rows = _to_rows(row_len, cipher, pad=pad)
    order = _to_order(key)

    # Detranspose
    rows = tuple(''.join(
                rows[order[i]][j] for i in range(key_len)
            )
            for j in range(row_len)
    )
    return ''.join(rows)


def _to_rows(key_len, text, pad=None):
    """
    Divide `text` in rows of length `len`, optionally padding the last line with
    `pad`
    """

    rows = [
        text[i:i+key_len]
        for i in range(0, len(text), key_len)
    ]

    # Pad if needed
    if pad is not None:
        rows[-1] = rows[-1] + '0' * (key_len - len(rows[-1]))

    return rows

def _to_order(key):
    """ Get column sort order based on `key` """
    return list(sorted(key).index(char) for char in key)
