# frmo sys import exit
#
# class Action(object):
#
#     def take_action(self):
#         print("This action is not yet configured.")
#         print("Subclass it and implement enter().")
#         exit(1)
#
# class Engine(object):
#
#     def __init__(self, ):
#         self.action_choice = action_choice
#
#     def play(self):


class Player(object):

    workhours = 0
    moves = 8
    happiness = 100

    def __init__(self, input_name):
        self.name = str(input_name)

    # def take_action
