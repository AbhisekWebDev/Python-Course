# the root/parent class of all other classes we create is called the object class

class Human:
    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")

class Male(Human):
    def sleep(self):
        print("I can sleep whole day")

class Boy(Male):
    def work(self):
        Human.work(self)
        print("I can code")

class Programming(Boy):
    def work(self):
        print("I can write programs")

boy = Boy()
boy.sleep()
boy.eat()
boy.work()

prog = Programming()
prog.eat()
prog.sleep()
prog.work()
