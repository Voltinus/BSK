from math import ceil

class MatrixShift:
    @staticmethod
    def encode_2a(M, n):
        key = list(map(lambda a: int(a) - 1, n.split("-")))
        
        ret = ""
        for i in range(len(M) + len(key)):
            index = ((i//len(key)) * len(key)) + key[i%len(key)]
            if index < len(M):
                ret += M[index]
        
        return ret

    @staticmethod
    def decode_2a(M, n):
        ret = MatrixShift.encode_2a(M, n[::-1])
        if len(ret)%4 in [2, 3]:
            ret = ret[:-2] + ret[-1] + ret[-2]
        return ret
    
    @staticmethod
    def encode_2b(M, key):
        key = list(key)

        indices = [0 for i in range(len(key))]
        n = 1

        for i in range(ord("A"), ord("Z") + 1):
            letter = chr(i)
            while letter in key:
                indices[key.index(letter)] = n
                n += 1
                key[key.index(letter)] = "."
                
        ret = ""

        for x in range(len(key)):
            for y in range(int(len(M) / len(key)) + 1):
                index = (y*len(key)) + indices.index(x+1)
                if index < len(M):
                    ret += M[index]
        
        return ret
    
    @staticmethod
    def decode_2b(M, key):
        key = list(key)

        indices = [0 for i in range(len(key))]
        n = 1

        for i in range(ord("A"), ord("Z") + 1):
            letter = chr(i)
            while letter in key:
                indices[key.index(letter)] = n
                n += 1
                key[key.index(letter)] = "."
        
        length = ceil(len(M) / len(indices))
        chars_left = len(M)
        blocks = ["" for i in indices]

        indices_index = 1
        M_index = 0
        for i in indices:
            shorter_length = len(M) // len(indices)
            if shorter_length < length and chars_left % length-1 == 0:
                length = shorter_length
            for j in range(length):
                blocks[indices.index(indices_index)] += M[M_index]
                M_index += 1
            indices_index += 1

        return blocks


if __name__ == "__main__":
    text = "CRYPTOGRAPHYOSA"
    key = "3-1-4-2"
    encoded = MatrixShift.encode_2a(text, key)
    decoded = MatrixShift.decode_2a(encoded, key)

    print(text)
    print(encoded)
    print(decoded)
    print()

    text = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"
    encoded = MatrixShift.encode_2b(text, key)
    decoded = MatrixShift.decode_2b(encoded, key)

    print(text)
    print(encoded)
    print(decoded)