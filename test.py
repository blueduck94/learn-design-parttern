class test:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @property
    def cv(self):
        return self.age + ' alo ' + self.name

    @cv.setter
    def cv(self, input):
        self.age = input
        self.name = input


test_class = test(name='long', age='27')
print(test_class.age)
print(test_class.cv)

test_class.cv = 'longngng'
print(test_class.cv)




