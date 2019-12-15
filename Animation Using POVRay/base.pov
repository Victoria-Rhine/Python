#include "colors.inc"
#include "textures.inc"
#declare Cam = camera { perspective angle 55 location < 0.0 , 4.0 , 8.0 > look_at < 0.0 , 0.0 , 0.0 > }
camera { Cam }
light_source { < 1500 , 2500 , -2500 > color rgb < 1 , 0.9 ,0.8 > }
sphere { < 0 , 0 , 0 > , 1 hollow
       texture { pigment { gradient < 0 , 1 , 0 >
                       color_map { [ 0.0 color White ]
                                 [ 0.3 color SkyBlue ]
                                 [ 1.0 color NavyBlue ] }
                       quick_color White } } scale 10000 }

#declare Canoe_Position = transform { rotate < 0 , 30 , 0 > translate < 0 , 0 , 1 > }

#declare Canoe_outside=
sphere { < 0 , 0 , 0 > , 1 scale < 3 , 1.5 , 1 > rotate < 0 , 0 , 0 > translate < 0 , 0.5 , 0 > }

#declare Canoe =
union {
intersection {
 object { Canoe_outside }
 object{ Canoe_outside scale < 0.98 , 0.95 , 0.94 > inverse }
 sphere { < 0 , 0 , 0 > , 1 scale < 2.5 , 1 , 20 > rotate < 0 , 0 , 0 > translate < 0 , 1.3 , 0 >  inverse }
       texture { pigment { color White * 1.1 }
                finish { phong 1 } } } 

 intersection {
  object { Canoe_outside
          texture { pigment { color White * 1.1 }
                   finish { phong 1 } } }
 union{
  box { <-0.20 ,0 , -1 > , <0.20 , 0.05 ,1 > rotate <0 , 0 , 0 > translate < 0.0 , 0.21 , 0 > }
  box { <-0.20 ,0 , -1 > , <0.20 , 0.05 ,1 > rotate <0 , 0 , -10 > translate < -2.0 , 0.40 , 0 > }
  box { <-0.20 ,0 , -1 > , <0.20 , 0.05 ,1 > rotate <0 , 0 , 10 > translate < 2.0 , 0.40 , 0 > }
  texture { pigment { color MediumWood }
           finish { phong 1 } } } } }

object { Canoe transform Canoe_Position }

difference {
plane { < 0 , 1 , 0 > , 0 }
object { Canoe_outside transform Canoe_Position }
   texture { Polished_Chrome
                    normal { crackle 1 scale 5
                            turbulence 1 translate <0,0,5> }
                    finish { diffuse 0.5 reflection 0.30 } } }