'''
Закодируйте любую строку по алгоритму Хаффмана.
'''

import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, code, acc):
        code[self.char] = acc or '0'

def encode_huffman(s):
    huffman = []
    for ch, freq in Counter(s).items():
        huffman.append((freq, len(huffman), Leaf(ch)))
    heapq.heapify(huffman)
    count = len(huffman)

    while len(huffman) > 1:
        freq1, count1, left  = heapq.heappop(huffman)
        freq2, count2, right = heapq.heappop(huffman)

        heapq.heappush(huffman, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code ={}
    if huffman:
        [(freq, count, root)] = huffman
        root.walk(code, '')
    return code

def decode_huffman(encoded, code):
    sx     = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ''
                break
    return ''.join(sx)

def main():
    s = input('Введите фразу: ')
    code = encode_huffman(s)
    encode = ''.join(code[ch] for ch in s)

    print(encode)
    print(decode_huffman(encode, code))

if __name__ == '__main__':
    main()