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


class ScoreCard(object):

    workhours = 0
    moves = 8
    happiness = 100

    def __init__(self, input_name):
        self.name = str(input_name)

    # need to define functions to change the score

    # def take_action


class Engine(object):


    # insert the randomized "firing people" function here

    #  for each round, if not getting fired, then you will have an option
    
    def __init__self(self):
        pass


class Action(object):

    def choose(self):
        print("This action is not yet configured.")
        print("Subclass it and implement choose().")
        exit(1)


# For each action classes, will need to return changes to scorecard
# class
