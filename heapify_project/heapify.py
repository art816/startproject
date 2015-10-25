import random

class Heap(object):
    '''Бинарная пирамида, в которой хранятся элементы'''
    
    def __init__(self,  element_list=[]):
        '''Получает на вход список элементов'''
        self.heap_list = ["Не используется"] + element_list 
        self.size = len(element_list)        
        print("Размер листа равен " + str(self.size)) 
        print("А нулевой элемент равен " + str(self.heap_list[0]))
       
    def __repr__(self):
        result = "Список элементов в пирамиде:"
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
        print("Вызван max_heapify(%i)" % (i))
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
      
                

#Создаем пираммиду со случайным списком чисел    
main_heap = Heap(random.sample(range(100), 9))
print(main_heap)

main_heap.max_heapify(2)

print(main_heap)
   
   
    