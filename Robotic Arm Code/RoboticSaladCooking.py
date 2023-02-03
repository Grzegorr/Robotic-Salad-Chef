import serial
import rtde_receive
import rtde_control
import time

#### MOST BASIC FUNCTIONS ######
#gripper_open(ardu)                                    TESTED
#gripper_close(ardu)                                   TESTED
#home_position(rtde_c)                                 TESTED
from BasicFunctions import *

##### FRY CUTTER OPERATION FUNCTIONS ####
#fry_open(ardu, rtde_c)                                TESTED
#fry_close(ardu, rtde_c)                               TESTED
from FryCutterOpenClose import *

#### INGREDIENT PICKUP ####
#numbering from down to up
#oposiit to recipe

#ORANGE PICKUP
#pickup_1_1(ardu, rtde_c)                              TESTED
#pickup_1_2(ardu, rtde_c)
#pickup_1_3(ardu, rtde_c)
#pickup_1_4(ardu, rtde_c)
from OrangePickup import *

#BANANA PICKUP
#pickup_2_1(ardu)
#pickup_2_2(ardu)
#pickup_2_3(ardu)
#pickup_2_4(ardu)
from BananaPickup import *

#APPLE PICKUP
#pickup_3_1(ardu)
#pickup_3_2(ardu)
#pickup_3_3(ardu)
#pickup_3_4(ardu)
from ApplePickup import *

#CARROT PICKUP
#pickup_4_1(ardu, rtde_c)
#pickup_4_2(ardu, rtde_c)
#pickup_4_3(ardu, rtde_c)
#pickup_4_4(ardu, rtde_c)
from CarrotPickup import *

#BROCOLLI PICKUP
#pickup_5_1(ardu)
#pickup_5_2(ardu)
#pickup_5_3(ardu)
#pickup_5_4(ardu)
from BroccoliPickup import *

#### INGREDIENT DELIVERY ####
#home_to_fry_cutter(ardu)                       TESTED
# MISSING: home_to_the_bowl(ardu)
from IngredientDelivery import *

#### INGREDIENT ADDING ####
#def ingredient_add(ardu, rtde_c, ingredient, slot):
#def pick_up_ingredient(ardu, rtde_c, ingredient, slot):
from Ingredient_Add import *

#### RECIPE LEVEL COOKING ####

#EXPERIMENTAL
from RecipesExperimentation import *

#THE COOKBOOK
from Cookbook import *



#Connect to the arm
rtde_c = rtde_control.RTDEControlInterface("169.254.141.189")
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.141.189")

#connect to the arduino
ardu = serial.Serial('COM7', 9600)

time.sleep(5)


#get position in TASK SPACE:
# pos=rtde_r.getActualTCPPose()

# get a position in JOINT SPACE:
# pos_j = rtde_r.getActualQ()

#moveing in JOINT SPACE
# rtde_c.moveJ(PosHj)






if __name__ == '__main__':
    for n in range(1):
        gripper_close(ardu)
        time.sleep(2)
        gripper_open(ardu)
        time.sleep(2)






ingredient_add(ardu, rtde_c, "carrot", 1)