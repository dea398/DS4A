'''
Hello World
'''
# from direct.showbase.ShowBase import ShowBase
 
# class MyApp(ShowBase):
 
#     def __init__(self):
#         ShowBase.__init__(self)
 
# app = MyApp()
# app.run()

'''
Hello World part 2
'''
# from direct.showbase.ShowBase import ShowBase
 
# class MyApp(ShowBase):
 
#     def __init__(self):
#         ShowBase.__init__(self)
 
#         # Load the environment model.
#         self.scene = self.loader.loadModel("models/environment")
#         # Reparent the model to render.
#         self.scene.reparentTo(self.render)
#         # Apply scale and position transforms on the model.
#         self.scene.setScale(0.25, 0.25, 0.25)
#         self.scene.setPos(-8, 42, 0)
 
 
# app = MyApp()
# app.run()

'''
Hello World part 3
'''
# from math import pi, sin, cos
 
# from direct.showbase.ShowBase import ShowBase
# from direct.task import Task
 
# class MyApp(ShowBase):
#     def __init__(self):
#         ShowBase.__init__(self)
 
#         # Load the environment model.
#         self.scene = self.loader.loadModel("models/environment")
#         # Reparent the model to render.
#         self.scene.reparentTo(self.render)
#         # Apply scale and position transforms on the model.
#         self.scene.setScale(0.25, 0.25, 0.25)
#         self.scene.setPos(-8, 42, 0)
 
#         # Add the spinCameraTask procedure to the task manager.
#         self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
#     # Define a procedure to move the camera.
#     def spinCameraTask(self, task):
#         angleDegrees = task.time * 6.0
#         angleRadians = angleDegrees * (pi / 180.0)
#         self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 5)
#         self.camera.setHpr(angleDegrees, 0, 0)
#         return Task.cont
 
# app = MyApp()
# app.run()

'''
Hello World part 4
'''
# from math import pi, sin, cos
 
# from direct.showbase.ShowBase import ShowBase
# from direct.task import Task
# from direct.actor.Actor import Actor
 
# class MyApp(ShowBase):
#     def __init__(self):
#         ShowBase.__init__(self)
 
#         # Load the environment model.
#         self.scene = self.loader.loadModel("models/environment")
#         # Reparent the model to render.
#         self.scene.reparentTo(self.render)
#         # Apply scale and position transforms on the model.
#         self.scene.setScale(0.25, 0.25, 0.25)
#         self.scene.setPos(-8, 42, 0)
 
#         # Add the spinCameraTask procedure to the task manager.
#         self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
#         # Load and transform the panda actor.
#         self.pandaActor = Actor("models/panda-model",
#                                 {"walk": "models/panda-walk4"})
#         self.pandaActor.setScale(0.005, 0.005, 0.005)
#         self.pandaActor.reparentTo(self.render)
#         # Loop its animation.
#         self.pandaActor.loop("walk")
 
#     # Define a procedure to move the camera.
#     def spinCameraTask(self, task):
#         angleDegrees = task.time * 6.0
#         angleRadians = angleDegrees * (pi / 180.0)
#         self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
#         self.camera.setHpr(angleDegrees, 0, 0)
#         return Task.cont
 
# app = MyApp()
# app.run()

'''
Hello World 5
'''

# from math import pi, sin, cos
 
# from direct.showbase.ShowBase import ShowBase
# from direct.task import Task
# from direct.actor.Actor import Actor
# from direct.interval.IntervalGlobal import Sequence
# from panda3d.core import Point3
 
# class MyApp(ShowBase):
#     def __init__(self):
#         ShowBase.__init__(self)
 
#         # Disable the camera trackball controls.
#         self.disableMouse()
 
#         # Load the environment model.
#         self.scene = self.loader.loadModel("models/environment")
#         # Reparent the model to render.
#         self.scene.reparentTo(self.render)
#         # Apply scale and position transforms on the model.
#         self.scene.setScale(0.25, 0.25, 0.25)
#         self.scene.setPos(-8, 42, 0)
 
#         # Add the spinCameraTask procedure to the task manager.
#         self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
#         # Load and transform the panda actor.
#         self.pandaActor = Actor("models/panda-model",
#                                 {"walk": "models/panda-walk4"})
#         self.pandaActor.setScale(0.005, 0.005, 0.005)
#         self.pandaActor.reparentTo(self.render)
#         # Loop its animation.
#         self.pandaActor.loop("walk")
 
#         # Create the four lerp intervals needed for the panda to
#         # walk back and forth.
#         pandaPosInterval1 = self.pandaActor.posInterval(13,
#                                                         Point3(0, -10, 0),
#                                                         startPos=Point3(0, 10, 0))
#         pandaPosInterval2 = self.pandaActor.posInterval(13,
#                                                         Point3(0, 10, 0),
#                                                         startPos=Point3(0, -10, 0))
#         pandaHprInterval1 = self.pandaActor.hprInterval(3,
#                                                         Point3(180, 0, 0),
#                                                         startHpr=Point3(0, 0, 0))
#         pandaHprInterval2 = self.pandaActor.hprInterval(3,
#                                                         Point3(0, 0, 0),
#                                                         startHpr=Point3(180, 0, 0))
 
#         # Create and play the sequence that coordinates the intervals.
#         self.pandaPace = Sequence(pandaPosInterval1,
#                                   pandaHprInterval1,
#                                   pandaPosInterval2,
#                                   pandaHprInterval2,
#                                   name="pandaPace")
#         self.pandaPace.loop()
 
#     # Define a procedure to move the camera.
#     def spinCameraTask(self, task):
#         angleDegrees = task.time * 6.0
#         angleRadians = angleDegrees * (pi / 180.0)
#         self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
#         self.camera.setHpr(angleDegrees, 0, 0)
#         return Task.cont
 
# app = MyApp()
# app.run()

'''
Hello World part 6
'''
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import WindowProperties
from panda3d.core import Spotlight, AmbientLight, DirectionalLight
from panda3d.core import Vec4, Vec3
from direct.task import Task
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerPusher
from panda3d.core import CollisionSphere, CollisionNode
from panda3d.core import CollisionTube

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)     

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(mainLight)
        # Turn it around by 45 degrees, and tilt it down by 45 degrees
        self.mainLightNodePath.setHpr(45, -45, 0)
        render.setLight(self.mainLightNodePath)   

        render.setShaderAuto()

        self.environment = loader.loadModel("Models/Misc/environment")
        self.environment.reparentTo(render)
        self.tempActor = Actor("Models/PandaChan/act_p3d_chan", {"walk" : "Models/PandaChan/a_p3d_chan_run"})
        self.tempActor.getChild(0).setH(180)
        self.tempActor.reparentTo(render)
        self.tempActor.setPos(0, 2, 0)
        self.tempActor.loop("walk")
        self.camera.setPos(0, 0, 32)
        self.camera.setP(-90)

        self.keyMap = {
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False,
            "shoot" : False
        }  

        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])

        self.updateTask = taskMgr.add(self.update, "update")


        # Panda should now automatically update that traverser!
        self.cTrav = CollisionTraverser()

        self.pusher = CollisionHandlerPusher() # prevents nominated solid objects from intersecting other solid objects.

        colliderNode = CollisionNode("player")
        # Add a collision-sphere centred on (0, 0, 0), and with a radius of 0.3
        colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.4))
        collider = self.tempActor.attachNewNode(colliderNode)
        collider.show()
        # The pusher wants a collider, and a NodePath that
        # should be moved by that collider's collisions.
        # In this case, we want our player-Actor to be moved.
        base.pusher.addCollider(collider, self.tempActor)
        # The traverser wants a collider, and a handler
        # that responds to that collider's collisions
        base.cTrav.addCollider(collider, self.pusher)

        self.pusher.setHorizontal(True)

        # Tubes are defined by their start-points, end-points, and radius.
        # In this first case, the tube goes from (-8, 0, 0) to (8, 0, 0),
        # and has a radius of 0.2.
        wallSolid = CollisionTube(-8.0, 0, 0, 8.0, 0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = render.attachNewNode(wallNode)
        wall.setY(8.0)

        wallSolid = CollisionTube(-8.0, 0, 0, 8.0, 0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = render.attachNewNode(wallNode)
        wall.setY(-8.0)

        wallSolid = CollisionTube(0, -8.0, 0, 0, 8.0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = render.attachNewNode(wallNode)
        wall.setX(8.0)

        wallSolid = CollisionTube(0, -8.0, 0, 0, 8.0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = render.attachNewNode(wallNode)
        wall.setX(-8.0)

    def updateKeyMap(self, controlName, controlState):
        self.keyMap[controlName] = controlState
        print (controlName, "set to", controlState)   

    def update(self, task):
        # Get the amount of time since the last update
        dt = globalClock.getDt()
        # If any movement keys are pressed, use the above time
        # to calculate how far to move the character, and apply that.
        if self.keyMap["up"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(0, 5.0*dt, 0))
        if self.keyMap["down"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(0, -5.0*dt, 0))
        if self.keyMap["left"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(-5.0*dt, 0, 0))
        if self.keyMap["right"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(5.0*dt, 0, 0))
        if self.keyMap["shoot"]:
            print ("Zap!")

        return Task.cont  

game = Game()
game.run()

