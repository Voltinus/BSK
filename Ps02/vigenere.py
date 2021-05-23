def vigenere_encode(M, key):
    ret = ""
    for index, item in enumerate(M):
        a = ord(item) - ord("A")
        b = ord(key[index % len(key)]) - ord("A")
        ret += chr((a + b) % 26 + ord("A"))
    return ret


def vigenere_decode(M, key):
    ret = ""
    for index, item in enumerate(M):
        a = ord(item) - ord("A")
        b = ord(key[index % len(key)]) - ord("A")
        ret += chr((a - b) % 26 + ord("A"))
    return ret