class Vigenere:
    @staticmethod
    def encode(M, key):
        ret = ""
        for index, item in enumerate(M):
            a = ord(item) - ord("A")
            b = ord(key[index % len(key)]) - ord("A")
            ret += chr((a + b) % 26 + ord("A"))
        return ret


    @staticmethod
    def decode(M, key):
        ret = ""
        for index, item in enumerate(M):
            a = ord(item) - ord("A")
            b = ord(key[index % len(key)]) - ord("A")
            ret += chr((a - b) % 26 + ord("A"))
        return ret
        


if __name__ == "__main__":
    text = "CRYPTOGRAPHY"
    key = "BREAK"
    encoded = Vigenere.encode(text, key)
    decoded = Vigenere.decode(encoded, key)

    print(text)
    print(encoded)
    print(decoded)