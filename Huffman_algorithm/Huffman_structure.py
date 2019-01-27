import collections
from heapq import *
from Huffman_algorithm.Node import *
import operator

class Huffman_structure:

    queue = []
    code_book = {}

    def create_list(self, text):
        list = dict(collections.Counter(text))
        list_sorted = sorted(list.items(), key=operator.itemgetter(1), reverse=True)

        return list_sorted


    def make_code_book(self, s, node):
        if node.item:
            if not s:
                self.code_book[node.item] = '0'
            else:
                self.code_book[node.item] = s
        else:
            self.make_code_book(s + '0', node.child_left)
            self.make_code_book(s + '1', node.child_right)


    def huffman(self, text):
        sorted_text = self.create_list(text)
        for key, value in sorted_text:
            self.queue.append(Node(key, value))

        heapify(self.queue)

        while len(self.queue) > 1:
            smallest_1 = heappop(self.queue)
            smallest_2 = heappop(self.queue)
            n = Node(None, smallest_1.frequancy + smallest_2.frequancy)
            n.setChildren(smallest_1, smallest_2)
            heappush(self.queue, n)

        self.make_code_book('', self.queue[0])  # ''code write here

        return self.code_book


    def compression(self, text):
        after_compression = ''
        for i in text:
            for j in self.code_book.keys():
                if i == j:
                    after_compression += self.code_book[j]

        return after_compression

