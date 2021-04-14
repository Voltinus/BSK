class LFSR:
    def __init__(self, start=0b1, bits=8, taps=[1, 2, 3, 7]):
        self.bits = bits
        self.taps = taps
        self.state = start
    
    def get(self):
        return self.state
    
    def next(self):
        new_bit = 0

        for i in self.taps:
            new_bit ^= (self.state >> i) % 2
        
        self.state <<= 1
        self.state %= 2**self.bits
        self.state |= new_bit

        return self.state


if __name__ == "__main__":
    lfsr = LFSR()


    for i in range(20):
        print(lfsr.next())