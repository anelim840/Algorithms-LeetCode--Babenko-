import heapq
class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman(text):
    freq = {}

    # считаем частоты
    for ch in text:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    Q = []

    for ch in freq:
        heapq.heappush(Q, Node(ch, freq[ch]))

    while len(Q) > 1:   # строим дерево
        z = Node(None, 0)
        x = heapq.heappop(Q)
        y = heapq.heappop(Q)

        z.left = x
        z.right = y
        z.freq = x.freq + y.freq

        heapq.heappush(Q, z)
        
    return heapq.heappop(Q)
    