#  ACTIVIDAD: Queue de Stacks - 15/08/2021

#  INSTRUCCIONES: Implementa una Clase Queue en python, utilizando solamente 2 stacks.

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if self.isEmpty(self.stack1) and self.isEmpty(self.stack2):
            return "La fila está vacía"
        elif not self.isEmpty(self.stack1) and self.isEmpty(self.stack2):
            while not self.isEmpty(self.stack1):
                popped_element = self.stack1.pop()
                self.stack2.append(popped_element)
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def isEmpty(self, stack):
        return len(stack) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
