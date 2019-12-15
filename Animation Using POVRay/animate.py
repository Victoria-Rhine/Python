# @author Victoria Rhine
import os
import re
import fileinput
import math

# Opens and reads static image scene into a string
# base.pov code is modified from tutorial found on www.f-lohmueller.de
# Webpage with tutorial here: www.f-lohmueller.de/pov_tut/x_sam/tec_550e.htm
fin = open('base.pov')
sdlString = fin.read()
fin.close()


# Creating class for various shapes
class Shape:
    __style = ""
    __x_location = 0
    __z_location = 0
    __size = 0
    __color = ""
    __finish = ""
    __phong = 0

# Creating a class that creates an object
# Constructor with keyword arguments
    def __init__(self, style='sphere', x_location=-9, z_location=-1.5, size=0.4,
                 color='Red', finish='phong', phong=1.0):
        self.__style = style
        self.__x_location = x_location
        self.__z_location = z_location
        self.__size = size
        self.__color = color
        self.__finish = finish
        self.__phong = phong

    def set_style(self, style):
        self.__style = style

    def get_style(self):
        return self.__style

    def set_x_location(self, x_location):
        self.__x_location = x_location

    def get_x_location(self):
        return self.__x_location

    def set_z_location(self, z_location):
        self.__z_location = z_location

    def get_z_location(self):
        return self.__z_location

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_finish(self, finish):
        self.__finish = finish

    def get_finish(self):
        return self.__finish

    def set_phong(self, phong):
        self.__phong = phong

    def get_phong(self):
        return self.__phong


# Function converts a string to a list
def string_to_list(string):
    li = list(string.split())
    return li


# Creating dictionary to print beginning and end of movie
project_movie = {'Start': 'Creating movie with static boat, moving sphere, and moving torus...',
                 'End': 'Ending movie, ready to watch'}

# Creating tuples for object labels so they won't be changed
shape_1_labels = ('sphere', 'Red', 'texture', 'pigment', 'color', 'finish')
shape_2_labels = ('torus', 'Blue', 'texture', 'pigment', 'color', 'finish', 'scale', 'translate')

# Making objects to insert into scene
sphere_object = Shape()
torus_object = Shape(style='torus', x_location=3.8, z_location=10, size=0, color='Green', finish='phong', phong=1.0)

# Converting sdlString to a list to easily find needed locations
sdlList = string_to_list(sdlString)

# Finding index of camera location coordinates x, y, z
camStart = sdlList.index('location')
xLoc = camStart + 2
yLoc = xLoc + 2
zLoc = yLoc + 2

# Initial values x, y, z for starting location of camera and counter for loop
count = 0
x_cam = 0
y_cam = 10
z_cam = 10
# Starting x and y coordinate for objects that will change with each loop
sphere_x = sphere_object.get_x_location()
torus_z = torus_object.get_z_location()

# Using dictionary to signal start of movie loop
print(project_movie['Start'])

# Loop to move camera
while count < 550:
    # Creates a new file to write to
    outfile = 'temp.pov'
    fout = open(outfile, 'w')

    # Insert coordinates for camera to create helix effect
    sdlList[xLoc] = 2*math.cos(x_cam)*(math.pi/180)
    sdlList[yLoc] = y_cam
    sdlList[zLoc] = 2*math.sin(z_cam)*(math.pi/180)

    # Putting information together for sphere using object class and truple
    sphere_object_info = [sphere_object.get_style(), '{', '<', sphere_object.get_x_location(), ',', -0.001, ',',
                          -4, '>', ',', sphere_object.get_size(), shape_1_labels[2], '{', shape_1_labels[3], '{',
                          shape_1_labels[4], sphere_object.get_color(), '}', shape_1_labels[5],
                          '{', sphere_object.get_finish(), sphere_object.get_phong(), '}', '}', '}']

    # Increment values for camera so it's in a different position next loop
    x_cam += 0.015
    y_cam += 0.03
    z_cam += 0.015
    count += 1

    # Changes and sets x coordinate of sphere so it will move next loop
    sphere_x += 0.035
    sphere_object.set_x_location(sphere_x)

    # Putting information together for torus using object class and truple
    torus_object_info = torus_object.get_style(), '{', 0.9, 0.35, shape_2_labels[2], '{', shape_2_labels[3], \
                        '{', shape_2_labels[4], torus_object.get_color(), '}', shape_2_labels[5], '{', \
                        torus_object.get_finish(), torus_object.get_phong(), '}', '}', shape_2_labels[6], \
                        '<', 0.8, ',', 0.8, ',', 0.8, '>', shape_2_labels[7], '<', 5, ',', -0.001, ',', \
                        torus_object.get_z_location(), '>', '}'

    # Changes and sets z coordinate of torus so it will move next loop
    torus_z -= 0.03
    torus_object.set_z_location(torus_z)

    # Changing the lists into strings
    sdl = ' '.join(map(str, sdlList))
    sphere_object_str = ' '.join(map(str, sphere_object_info))
    torus_object_str = ' '.join(map(str, torus_object_info))
    # Putting the strings together
    sdl = sdl + sphere_object_str + torus_object_str
    # Writing out to file
    fout.write(sdl)
    fout.close()

    # This creates a new image for every loop
    pov_cmd = 'pvengine.exe +I%s +O%s -D -V +A +H600 +W800 /exit'
    cmd = pov_cmd % ('temp.pov', "temp" + str(count).zfill(4) + ".png")
    os.system(cmd)

# Images encoded in movie
os.system('mencoder.exe mf://temp*.png -mf type=png:fps=25 -ovc lavc -lavcopts '
          'vcodec=msmpeg4:vbitrate=2160000:keyint=5:vhq -o Animation.avi ')

# Using dictionary to signal program is finished
print(project_movie['End'])
