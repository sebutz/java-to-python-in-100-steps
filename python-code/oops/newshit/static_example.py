class Player:
    count = 0  # static variable

    def __init__(self, name):
        self.name = name
        Player.count += 1  # refering a static

    def get_count(self):
        return Player.count

    @staticmethod
    def get_count_static():  # you don't need self for static methods
        return Player.count

messi = Player("Messi")
ronaldo = Player("Ronaldo")


print(Player.count)
print(messi.count)
print(ronaldo.count)


'''
2
2
2
'''
# you should not write on static
# never use an instance to change a static value
messi.count = 100  # this count is now an instance variable

print(Player.count)
print(messi.count)
print(ronaldo.count)
'''
2
100
2
'''

Player.count = 100
print(Player.count)
print(messi.count)
print(ronaldo.count)

'''
100
100
100
'''


print(messi.get_count())
print(ronaldo.get_count())
# 100
# 100

# print(Player.get_count())  TypeError: get_count() missing 1 required positional argument: 'self'
# we are not passing self when we call it on a class
# self is passed only when it's called on an instance

print(Player.get_count_static())
#100

# it's not recommandable to call static methods on an instance
print(messi.get_count_static())
#100