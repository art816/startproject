import heapify
import unittest
import random
import math

class TestHeapify(unittest.TestCase):
    def setUp(self):
        self.heap = heapify.Heap(random.sample(range(100), 10))


class TestHeapify(unittest.TestCase):
    def setUp(self):
        self.heap = heapify.Heap(random.sample(range(10000), 1000))
        
    def test_heapify(self):
        self.passed = bool(1)
        self.heap.build_max_heap()
        for i in range(math.trunc(self.heap.size / 2), 2, -1):
            print("Рассматриваем элемет %i" % (i))
        for i in range(self.heap.size-1, 2, -1):
        	#вместо ифа юзай ассерт
        	# self.assertLess в todo ссылка
            if self.heap.heap_list[self.heap.parent(i)] < self.heap.heap_list[i]:
                self.passed = bool(0)
                print(self.heap)
                print("Условие heapify не выполняется для элемента %i" % (i))
        print(self.heap)
        #print(self.heap)
        self.assertEqual(bool(1), self.passed)


if __name__ == '__main__':
	unittest.main()
    
