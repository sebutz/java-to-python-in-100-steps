from abc import ABC, abstractmethod

'''
ABC : abstract base class
'''
class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


#recipe = AbstractRecipe()
#recipe.execute()

'''
    recipe = AbstractRecipe()
TypeError: Can't instantiate abstract class AbstractRecipe with abstract methods cleanup, do_the_dish, get_ready
'''


class Recipe1(AbstractRecipe):

   def get_ready(self):
       print("Get raw materials")
       print("Get utensils")

   def do_the_dish(self):
       print("Do the dish")

   def cleanup(self):
       print("clean up")


recipe1 = Recipe1()
recipe1.get_ready()
#recipe1.execute()
recipe1.cleanup()

