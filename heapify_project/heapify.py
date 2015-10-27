'''Main module of heapify_project'''
from __future__ import print_function
import random


class Heap(object):
    '''Binary heap class'''

    def __init__(self, element_list=None):
        '''Take a list of elements'''
        self.heap_list = ["Not used"] + element_list
        self.size = len(element_list)

    def __repr__(self):
        result = "List of elements in heap:"
        counter = 0
        for heap_el in self.heap_list:
            result += "\n%i. " % (counter)
            result += str(heap_el)
            counter += 1
        return result

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return int(i / 2)


    def max_heapify(self, i):
        left_element_pos = self.left(i)
        right_element_pos = self.right(i)
        if left_element_pos < self.size and self.heap_list[left_element_pos] > self.heap_list[i]:
            largest = left_element_pos
        else:
            largest = i
        if r < self.size and self.heap_list[right_element_pos] > self.heap_list[largest]:
            largest = right_element_pos
        if largest != i:
            tmp = self.heap_list[i]
            self.heap_list[i] = self.heap_list[largest]
            self.heap_list[largest] = tmp
            self.max_heapify(largest)

    def build_max_heap(self):
        self.size = len(self.heap_list)
        for i in range(int(self.size / 2), 0, -1):
            self.max_heapify(i)


if __name__ == '__main__':
    MAIN_HEAP = Heap(random.sample(range(100), 9))
    print(MAIN_HEAP)
    MAIN_HEAP.max_heapify(2)
    print(MAIN_HEAP)
    MAIN_HEAP.build_max_heap()
    print(MAIN_HEAP)



