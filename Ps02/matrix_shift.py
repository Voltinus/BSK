from math import ceil

class MatrixShift:
    @staticmethod
    def get_indices(key):
        key = list(key)

        indices = [0 for i in range(len(key))]
        n = 1

        for i in range(ord("A"), ord("Z") + 1):
            letter = chr(i)
            while letter in key:
                indices[key.index(letter)] = n
                n += 1
                key[key.index(letter)] = "."
        
        return indices

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
        indices = MatrixShift.get_indices(key)
                
        ret = ""

        for x in range(len(key)):
            for y in range(int(len(M) / len(key)) + 1):
                index = (y*len(key)) + indices.index(x+1)
                if index < len(M):
                    ret += M[index]
        
        return ret
    
    @staticmethod
    def decode_2b(M, key):
        indices = MatrixShift.get_indices(key)
        
        longer_blocks = len(M) % len(indices)
        shorter_length = len(M) // len(indices)

        blocks = []
        block_start = 0

        for i in range(len(indices)):
            letters_in_block = shorter_length+1 if longer_blocks else shorter_length
            blocks.append(M[block_start: block_start+letters_in_block])
            block_start += letters_in_block
            if longer_blocks:
                longer_blocks -= 1
        
        output = ""

        for i in range(shorter_length+1): # position in block
            for j in indices:             # block number
                if i < len(blocks[j-1]):
                    output += blocks[j-1][i]

        return output
    
    @staticmethod
    def encode_2c(M, key):
        indices = MatrixShift.get_indices(key)
        
        blocks = []
        M_index = 0

        for i in range(len(indices)):
            blocks.append(M[M_index:M_index + indices.index(i+1) + 1])
            M_index = M_index + indices.index(i+1) + 1

            if M_index >= len(M):
                break
        
        output = ""

        for index in range(len(indices)):
            for block in blocks:
                if indices.index(index+1) < len(block):
                    output += block[indices.index(index+1)]

        return output
    
    @staticmethod
    def decode_2c(M, key):
        indices = MatrixShift.get_indices(key)

        M_left = len(M)
        blocks = []

        for i in range(len(indices)):
            string = (indices.index(i+1)+1 if indices.index(i+1)+1 < M_left else M_left) * "."
            blocks.append(string)
            M_left -= len(string)
            if not M_left:
                break
        
        M_index = 0

        for i in range(len(indices)):
            for j in range(len(blocks)):
                if M_index == len(M):
                    break
                if indices.index(i+1) < len(blocks[j]):
                    blocks[j] = blocks[j][:indices.index(i+1)] + M[M_index] + blocks[j][indices.index(i+1)+1:]
                    M_index += 1

        return "".join(blocks)


if __name__ == "__main__":

    # 2A

    text = "CRYPTOGRAPHYOSA"
    key = "3-1-4-2"
    encoded = MatrixShift.encode_2a(text, key)
    decoded = MatrixShift.decode_2a(encoded, key)

    print(text)
    print(encoded)
    print(decoded)
    print()


    # 2B

    text = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"
    encoded = MatrixShift.encode_2b(text, key)
    decoded = MatrixShift.decode_2b(encoded, key)

    print(text)
    print(encoded)
    print(decoded)
    print()


    # 2C

    text = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"
    encoded = MatrixShift.encode_2c(text, key)
    decoded = MatrixShift.decode_2c(encoded, key)

    print(text)
    print(encoded)
    print(decoded)