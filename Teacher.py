import os

class Teacher:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)

if __name__ == "__main__":
    teacher1 = Teacher('chris')
    teacher2 = Teacher('Tom')
    teacher1.getName()
