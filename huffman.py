class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from heapq import heappush, heapify, heappop
class Huffman:
    def __init__(self, s: str):
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        pq = [(c, f) for c, f in freq.items()]
        heapify(pq)

        while len(pq) >= 2:
            freq1, node1 = heappop(pq)
            freq2, node2 = heappop(pq)

            new_freq = freq1 + freq2
            new_node = Node(val=new_freq, left=node1, right=node2)
            heappush(pq, (new_freq, new_node))

        _, root = pq[0]
        self.root = root


    def decrypt(s: str):
        return

    