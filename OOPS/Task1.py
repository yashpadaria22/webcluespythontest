class CustomIterable:
    def __init__(self, range):
        self.value = 0
        self.range = range

    def __iter__(self):
        return self

    def __next__(self):
        while self.value <= self.range:
            if self.value % 2 == 0:
                even_num = self.value
                self.value += 2  
                return even_num
            else:
                self.value += 1
        raise StopIteration
    
user_range=int(input("Enter Limit of number to print even Number: "))
obj = CustomIterable(user_range)
for i in obj:
    print(i)

