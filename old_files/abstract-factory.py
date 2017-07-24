# Factory/shapefact1/NestedShapeFactory.py
import random

class Shape(object):
    types = []

def factory(type):
    class ytd(Shape):
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")

    class Square(Shape):
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")

    if type == "ytd": return ytd()
    if type == "Square": return Square()
    assert 0, "Bad shape creation: " + type

size = ['ytd','Square'] # ,'6mon','12mon','3yr', '5yr', '10yr','start','end']

n = len(size)

def shapeNameGen(size):
    for thing in size:
        print thing
        yield factory(thing)

# Circle() # Not defined

for shape in shapeNameGen(size):
    shape.draw()
    shape.erase()

#
#
#
#
#
#
#
#
#
#
#
#
#
# # Factory/Games.py
# # An example of the Abstract Factory pattern.
#
# class Obstacle:
#     def action(self): pass
#
# class Character:
#     def interactWith(self, obstacle): pass
#
# class Kitty(Character):
#     def interactWith(self, obstacle):
#         print("Kitty has encountered a",
#         obstacle.action())
#
# class KungFuGuy(Character):
#     def interactWith(self, obstacle):
#         print("KungFuGuy now battles a",
#         obstacle.action())
#
# class Puzzle(Obstacle):
#     def action(self):
#         print("Puzzle")
#
# class NastyWeapon(Obstacle):
#     def action(self):
#         print("NastyWeapon")
#
# # The Abstract Factory:
# class GameElementFactory:
#     def makeCharacter(self): pass
#     def makeObstacle(self): pass
#
# # Concrete factories:
# class KittiesAndPuzzles(GameElementFactory):
#     def makeCharacter(self): return Kitty()
#     def makeObstacle(self): return Puzzle()
#
# class KillAndDismember(GameElementFactory):
#     def makeCharacter(self): return KungFuGuy()
#     def makeObstacle(self): return NastyWeapon()
#
# class GameEnvironment:
#     def __init__(self, factory):
#         self.factory = factory
#         self.p = factory.makeCharacter()
#         self.ob = factory.makeObstacle()
#     def play(self):
#         self.p.interactWith(self.ob)
#
# g1 = GameEnvironment(KittiesAndPuzzles())
# g2 = GameEnvironment(KillAndDismember())
# g1.play()
# g2.play()
