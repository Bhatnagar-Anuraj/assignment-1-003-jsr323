"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

#imports maya's python commands module
import maya.cmds as cmds

#Clears the scene
cmds.file(new=True, force=True)

#create a 1x1 poly plane named planeFloor with 1 face
cmds.polyPlane(name="planeFloor",width=1, height=1, subdivisionsX=1, subdivisionsY=1)
#scales the plane by 32 in X, Y, and Z directions
cmds.scale(32, 32, 32)

#creates a 1x1x1 cube named towerOne
cmds.polyCube(name="towerOne", width=1, height=1, depth=1)
#scales the cube
cmds.scale(2, 9, 2)
#moves the cube
cmds.move(-10.2, 4, 0)

#creates a 1x1x1 cube named towerTwo
cmds.polyCube(name="towerTwo", width=1, height=1, depth=1)
#scales the cube
cmds.scale(2, 9, 2)
#moves the cube
cmds.move(10.2, 4, 0)

#creates a 1x1x1 cube named towerWall
cmds.polyCube(name="towerWall", width=1, height=1, depth=1)
#scales the cube
cmds.scale(2, 18.5, 2)
#moves the cube
cmds.move(0, 0.5, 0)
#rotates the cube
cmds.rotate(0, 0, -90)

#creates a cone with radius of 1, height of 1, and 20 subdivisions, named towerConeOne
cmds.polyCone(name="towerConeOne", radius=1, height=1, subdivisionsX=20)
#scales the cube
cmds.scale(2.6, 5.6, 2.6)
#moves the cube
cmds.move(10.2, 11, 0)

#creates a cone with radius of 1, height of 1, and 20 subdivisions, named towerConeTwo
cmds.polyCone(name="towerConeOne", radius=1, height=1, subdivisionsX=20)
#scales the cube
cmds.scale(2.6, 5.6, 2.6)
#moves the cube
cmds.move(-10.2, 11, 0)

#creat 8 cubes
object_count = 8
#each cube a size of 1 unit
cube_size = 1
#cubes with be 2.5 units apart
spacing_x = 2.5
#cubes will be lifted 1 unit up on the Y-axis
y_offset = 1

#number of gaps between cubes, total width of all gaps, divide by 2 to center row around the orgin, and starts the first cube on the left
start_x = -(object_count - 1) * spacing_x / 2.0

#loops 8 times
for i in range(object_count):
    #names each cube uniquely
    tinyTower = f"tinyTower_{i}"
    #creates a cube size
    cmds.polyCube(name=tinyTower, width=cube_size, height=cube_size, depth=cube_size)
    #places each cube spaced along the X-axis and keeping the row centered
    x_position = start_x + i * spacing_x
    #sets the height of each cube on the Y-axis
    y_position = cube_size / 1 + y_offset
    #moves the cube to the calculated position
    cmds.move(x_position, y_position, 0, tinyTower)

#prints a message confirming the cubes were created
print(f"Created {object_count} cubes spread on X and moved up on Y")

cmds.viewFit(allObjects=True)
print("Scene built successfully!")
