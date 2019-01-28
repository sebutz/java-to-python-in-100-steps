from abc import ABC, abstractmethod

'''
implement an interface using am abstract class
as there are no interfaces in Python
'''


class GamingConsole(ABC):

    @abstractmethod
    def up(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass

    @abstractmethod
    def right(self): pass


class MarioGame(GamingConsole):
    def up(self): print("up Mario")

    def down(self): print("down Mario")

    def left(self): print("left Mario")

    def right(self): print("right Mario")


class ChessGame(GamingConsole):
    def up(self): print("up")

    def down(self): print("down")

    def left(self): print("left")

    def right(self): print("right")


game = MarioGame()
game.down()
game.up()

# polymorphism:  same interface, different behaviour
games = [ChessGame(), MarioGame()]
print(type(games))  # <class 'list'>

for game in games:
    print(type(game))
    game.up()
    game.down()
    game.left()
    game.right()


# even if they don't implement the same interface
# the objects still behave differently (duck typing)
class MarioGame1():
    def up(self): print("up Mario")

    def down(self): print("down Mario")

    def left(self): print("left Mario")

    def right(self): print("right Mario")


class ChessGame1():
    def up(self): print("up")

    def down(self): print("down")

    def left(self): print("left")

    def right(self): print("right")


games1 = [ChessGame(), MarioGame()]

for game in games1:
    game.up()
    game.down()
    game.left()
    game.right()


class Test1:
    def method(self): print("Test1")


class Test2:
    def method(self): print("Test2")


tests = [Test1(), Test2()]
for test in tests:
    test.method()


# Python: there is no need to implement a common interface
# as in Java
# Python: there is no need to have  a superclass with this interface defined in it (implemented already)
# as in Java
# and Test1, Test2 should either implement that interface
# or extend that superclass


# what you need in Python?
# the same method name : that 's call duck typing


# what if

class Test3:
    @staticmethod         # just make the method static, for the fun of it
    def method(name="kko"):
        print(name)


tests = [Test1(), Test2(), Test3()]
for test in tests:
    test.method()

'''
Test1

Test2

kko
'''
