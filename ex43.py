from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print " Error"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.open_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print "Dead!"
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "You're in CentralCorridor."
        print "A Gothon is in front of you. Beat him left or right?"
        print "1, right; 2, left."

        beat_num = 0

        while True:
            choice = raw_input("> ")
            choice = int(choice)
            gothon_num = randint(1,2)
            print gothon_num

            if choice == gothon_num and beat_num < 3:
                print "Nice job! You hit it."
                beat_num += 1

            if choice == gothon_num and beat_num == 3:
                print "You defeat it!"
                return "laserweaponarmory"

            else:
                print "Nice move! Try again."


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You enter the LaserWeaponArmory."
        print "You must find the bomb here before Gothon finding you."
        print "There is it. Damn it, a key pad."
        print "Try to gusess it. Hint: three numbers, Birthday."

        laser_num = 815

        while True :
            choice = raw_input('> ')

            if choice == str(laser_num):
                print "Good job! You get the bomb."
                return "thebridge"

            else:
                print "Wrong Passwords. Try again."

class TheBridge(Scene):

    def enter(self):
        print "You 're on the Bridge."
        print "Find a place to set bomb up."
        print "Good job."
        return "escapepod"

class EscapePod(Scene):

    def enter(self):
        print "You 're in EscapePod. Guess the right escapepod."
        print "Choose 1, 2, 3."
        choice = raw_input('> ')
        excapepod = 3

        if choice == str(excapepod):
            print "You win."
            return "finished"
        else:
            return "death"

class Finished(Scene):
    def enter(self):
        print "You win"
        return "finished"


class Map(object):

    scenes = {
        'centralcorridor': CentralCorridor(),
        'laserweaponarmory': LaserWeaponArmory(),
        'thebridge': TheBridge(),
        'escapepod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def open_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('centralcorridor')
a_game = Engine(a_map)
a_game.play()
