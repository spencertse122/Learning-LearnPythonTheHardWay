class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        print(">>> engine starts to play: current scene ----", current_scene, "---", last_scene)
        while current_scene != last_scene:
            print("in the loop, current_scene", current_scene, "last scene", last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("<<< exiting the engine", current_scene)

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        print("entering next_scene from Map:", scene_name)
        pass

    def opening_scene(self):
        print("entering opening_scene from map")
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
