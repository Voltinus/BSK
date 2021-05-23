class LFSR:
    def __init__(self, start=1, bits=8, taps=[1, 2, 3, 7]):
        self.bits = bits
        self.taps = taps
        self.state = start


    def set(self, state):
        self.state = state
    

    def get(self):
        return self.state
    

    def get_xored_taps(self):
        xored = 0

        for i in self.taps:
            xored ^= (self.state >> i) % 2

        return xored


    def next(self, new_bit = -1):
        if new_bit == -1:
            new_bit = self.get_xored_taps()
        
        self.state <<= 1
        self.state %= 2**self.bits
        self.state |= new_bit

        return self.state


if __name__ == "__main__":
    lfsr = LFSR()
    print(lfsr.get())

    for i in range(20):
        print(lfsr.next())

