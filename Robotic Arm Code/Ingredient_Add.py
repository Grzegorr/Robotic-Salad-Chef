#ingredient is from following {"broccoli", "carrot", "apple", "banana", "orange"}
#slots are 1-4, left to right

from FryCutterOpenClose import *
from IngredientDelivery import *

from OrangePickup import *
from BananaPickup import *
from ApplePickup import *
from CarrotPickup import *
from BroccoliPickup import *

def ingredient_add(ardu, rtde_c, ingredient, slot):
    print("only carrot implemented")
    if ingredient == "carrot":
        fry_open(ardu, rtde_c)
        pick_up_ingredient(ardu, rtde_c, ingredient, slot)
        home_to_fry_cutter(ardu, rtde_c)
        fry_close(ardu, rtde_c)



def pick_up_ingredient(ardu, rtde_c, ingredient, slot):
    if ingredient == "broccoli":
        if slot == 1:
            pickup_5_1(ardu, rtde_c)
        if slot == 2:
            pickup_5_2(ardu, rtde_c)
        if slot == 3:
            pickup_5_3(ardu, rtde_c)
        if slot == 4:
            pickup_5_4(ardu, rtde_c)

    if ingredient == "carrot":
        if slot == 1:
            pickup_4_1(ardu, rtde_c)
        if slot == 2:
            pickup_4_2(ardu, rtde_c)
        if slot == 3:
            pickup_4_3(ardu, rtde_c)
        if slot == 4:
            pickup_4_4(ardu, rtde_c)

    if ingredient == "apple":
        if slot == 1:
            pickup_3_1(ardu, rtde_c)
        if slot == 2:
            pickup_3_2(ardu, rtde_c)
        if slot == 3:
            pickup_3_3(ardu, rtde_c)
        if slot == 4:
            pickup_3_4(ardu, rtde_c)

    if ingredient == "banana":
        if slot == 1:
            pickup_2_1(ardu, rtde_c)
        if slot == 2:
            pickup_2_2(ardu, rtde_c)
        if slot == 3:
            pickup_2_3(ardu, rtde_c)
        if slot == 4:
            pickup_2_4(ardu, rtde_c)

    if ingredient == "orange":
        if slot == 1:
            pickup_1_1(ardu, rtde_c)
        if slot == 2:
            pickup_1_2(ardu, rtde_c)
        if slot == 3:
            pickup_1_3(ardu, rtde_c)
        if slot == 4:
            pickup_1_4(ardu, rtde_c)