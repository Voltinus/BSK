from zad1 import LFSR


if __name__ == "__main__":
    text = "Linear Feedback Shift Register"
    encoded = ""
    decoded = ""
    
    lfsr = LFSR()
    for i in text:
        encoded += chr(ord(i) ^ lfsr.next())
    
    lfsr = LFSR()
    for i in encoded:
        decoded += chr(ord(i) ^ lfsr.next())

    print(text)
    print(encoded)
    print(decoded)