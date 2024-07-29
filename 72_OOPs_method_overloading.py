class Demo:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total
    
demo = Demo()
print(demo.add(2, 3))
print(demo.add(1, 2, 3))
print(demo.add(1, 2, 3, 4, 5, 6))