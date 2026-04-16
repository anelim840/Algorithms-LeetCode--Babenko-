import heapq
class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(text):
    freq = {}

    # считаем частоты
    for ch in text:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    Q = []

    # добавляем в очередь
    for ch in freq:
        heapq.heappush(Q, Node(ch, freq[ch]))

    # объединяем узлы
    while len(Q) > 1:
        x = heapq.heappop(Q)
        y = heapq.heappop(Q)

        z = Node(None, x.freq + y.freq)
        z.left = x
        z.right = y

        heapq.heappush(Q, z)

    return heapq.heappop(Q)


# строим коды
def build_codes(root):
    codes = {}

    def dfs(node, code):
        if node is None:
            return
        
        if node.ch is not None:
            codes[node.ch] = code
        
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")

    dfs(root, "")
    return codes


def encode(text, codes):
    res = ""
    for ch in text:
        res += codes[ch]
    return res

def decode(encoded, root): #декодирование 
    res = ""
    node = root

    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.ch is not None:
            res += node.ch
            node = root

    return res
