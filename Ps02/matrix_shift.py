from math import ceil


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


def encode_2a(M, n):
    key = list(map(lambda a: int(a) - 1, n.split("-")))
    
    ret = ""
    for i in range(len(M) + len(key)):
        index = ((i//len(key)) * len(key)) + key[i%len(key)]
        if index < len(M):
            ret += M[index]
    
    return ret


def decode_2a(M, n):
    key = list(map(lambda a: int(a) - 1, n.split("-")))
    ret = []

    for i in range(len(M) // len(key) + 1):
        ret.append(['' for i in range(len(key))])
        for j in range(len(key)):
            try:
                ret[len(ret)-1][key[j]] = M[i*len(key) + j]
            except:
                pass

    ret = list(map(lambda a: "".join(a), ret))
    ret = "".join(ret)

    if len(M) % len(key) > len(key) // 2:
        ret = ret[:-2] + ret[-1] + ret[-2]

    return ret
    
    
def encode_2b(M, key):
    if len(key) > len(M):
        key = key[:len(M)]

    indices = get_indices(key)
            
    ret = ""

    for x in range(len(key)):
        for y in range(int(len(M) / len(key)) + 1):
            index = (y*len(key)) + indices.index(x+1)
            if index < len(M):
                ret += M[index]
    
    return ret
    

def decode_2b(M, key):
    if len(key) > len(M):
        key = key[:len(M)]

    indices = get_indices(key)
    
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
    

def encode_2c(M, key):
    if len(key) > len(M):
        key = key[:len(M)]

    indices = get_indices(key)
    
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
    
    
def decode_2c(M, key):
    if len(key) > len(M):
        key = key[:len(M)]

    indices = get_indices(key)

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

    # 2C
    text = "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION"
    key = "CONVENIENCE"