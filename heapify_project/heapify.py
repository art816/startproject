import random
import math

class Heap(object):
    '''Binary heap class'''

    def __init__(self,  element_list=[]):
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
        l = self.left(i)
        r = self.right(i)
        if l < self.size and self.heap_list[l] > self.heap_list[i]:
            largest = l
        else:
            largest = i
        if r < self.size and self.heap_list[r] > self.heap_list[largest]:
            largest = r
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
    main_heap = Heap(random.sample(range(100), 9))
    print(main_heap)

    main_heap.max_heapify(2)

    print(main_heap)

    main_heap.build_max_heap()

    print(main_heap)



