import serial
import rtde_receive
import rtde_control

#### MOST BASIC FUNCTIONS ######
#gripper_open(ardu)
#gripper_close(ardu)
#home_position()
from BasicFunctions import *

##### FRY CUTTER OPERATION FUNCTIONS ####
#fry_open(ardu)
#fry_close(ardu)
from FryCutterOpenClose import *

#### INGREDIENT PICKUP ####

#CARROT PICKUP
#pickup_1_1(ardu)
#pickup_1_2(ardu)
#pickup_1_3(ardu)
#pickup_1_4(ardu)
from CarrotPickup import *

#APPLE PICKUP
#pickup_2_1(ardu)
#pickup_2_2(ardu)
#pickup_2_3(ardu)
#pickup_2_4(ardu)
from ApplePickup import *

#BANANA PICKUP
#pickup_3_1(ardu)
#pickup_3_2(ardu)
#pickup_3_3(ardu)
#pickup_3_4(ardu)
from BananaPickup import *

#BROCCOLI PICKUP
#pickup_4_1(ardu)
#pickup_4_2(ardu)
#pickup_4_3(ardu)
#pickup_4_4(ardu)
from BroccoliPickup import *

#ORANGE PICKUP
#pickup_5_1(ardu)
#pickup_5_2(ardu)
#pickup_5_3(ardu)
#pickup_5_4(ardu)
from OrangePickup import *

#### INGREDIENT DELIVERY ####
#home_to_fry_cutter(ardu)
# MISSING: home_to_the_bowl(ardu)
from IngredientDelivery import *

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


#get position in TASK SPACE:
# pos=rtde_r.getActualTCPPose()

# get a position in JOINT SPACE:
# pos_j = rtde_r.getActualQ()

#moveing in JOINT SPACE
# rtde_c.moveJ(PosHj)






if __name__ == '__main__':
    home_position()
    fry_close()