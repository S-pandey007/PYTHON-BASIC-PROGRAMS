class A:
    def he(self):
        print("Hello from parent class")
        
class B(A):
    def he(self):
        print('Hello from child class')
        
obj = B()
obj.he()