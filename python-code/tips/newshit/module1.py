# a module: a set of classes, methods


def method_1():
    print("method_1")


class ClassA:
    def a_method_1(self):
        print("class A a_method_1")


# when you are importing a module this code will be executed
print(__name__)

# this gets executed only you are executed module1 directly
if __name__ == '__main__':
    method_1()
    ClassA().a_method_1()  # create an instance and call the method a_method_1 on it

# a single file can contain multiple classes
# group by functionality
