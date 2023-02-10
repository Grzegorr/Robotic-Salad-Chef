from BasicFunctions import *
import time

from BasicFunctions import *

def pickup_1_1(ardu, rtde_c):
    home_position(rtde_c)

    posCaminus1 = [0.18258539135209367,
                   0.34237949883831,
                   0.5118164080334295,
                   -1.4564707803249504,
                   0.6975415335895895,
                   0.5703154832114745]
    rtde_c.moveL(posCaminus1, 0.1, 0.1)

    posCaminus2 = [0.146120374241993,
                   0.2947705615654465,
                   0.5561010885422959,
                   -1.5317463418365234,
                   -0.6669416675807128,
                   -0.5551648224932388]
    rtde_c.moveL(posCaminus2, 0.1, 0.1)
    posCaminus2j = [1.3919613361358643,
                    -1.178955380116598,
                    -2.0018580595599573,
                    -0.031080071126119435,
                    1.7977150678634644,
                    -0.7892864386187952]
    rtde_c.moveJ(posCaminus2j)

    posCaminus3 = [0.14611138964738846,
                   0.1997279761011389,
                   0.5561075018995623,
                   -1.5316924424712637,
                   -0.6669913692885129,
                   -0.5551953873574271]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the first carrot
    posCa01 = [0.15683071783164027,
               0.2199795226052555,
               0.7154318021398568,
               -1.4853169482818682,
               -0.6780230921572378,
               -0.6350040881275962]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)

    posCa02 = [0.1568316876978241,
               0.2199067639991236,
               0.5234951803941564,
               -1.4851164489085167,
               -0.677919238739707,
               -0.635198014607513]
    rtde_c.moveL(posCa02, 0.1, 0.1)
    posCa03 = [0.21139567855487623,
               0.2706275099445283,
               0.5438238597184026,
               -1.535369400769388,
               -0.6486672057417355,
               -0.6462199428337463]

    rtde_c.moveL(posCa03, 0.1, 0.1)
    # posCa04 = [0.05861901235436705,
    #  0.33075461915989246,
    #  0.6085464350818507,
    #  -1.3172383484031485,
    #  0.6800713986777788,
    #  0.7826348789754748]

    # rtde_c.moveL(posCa04, 0.1, 0.1)
    home_position(rtde_c)

def pickup_1_2(ardu, rtde_c):
    home_position(rtde_c)

    posCaminus1 = [0.18258539135209367,
                   0.34237949883831,
                   0.5118164080334295,
                   -1.4564707803249504,
                   0.6975415335895895,
                   0.5703154832114745]
    rtde_c.moveL(posCaminus1, 0.1, 0.1)

    posCaminus2 = [0.146120374241993,
                   0.2947705615654465,
                   0.5561010885422959,
                   -1.5317463418365234,
                   -0.6669416675807128,
                   -0.5551648224932388]
    rtde_c.moveL(posCaminus2, 0.1, 0.1)
    posCaminus2j = [1.3919613361358643,
                    -1.178955380116598,
                    -2.0018580595599573,
                    -0.031080071126119435,
                    1.7977150678634644,
                    -0.7892864386187952]
    rtde_c.moveJ(posCaminus2j)

    gripper_open(ardu)
    time.sleep(1)

    posCa02 = [0.15260587821980823,
               0.2739946962791212,
               0.7125673847142447,
               -1.4168769178443494,
               -0.6584822250460454,
               -0.5905115210283044]
    rtde_c.moveL(posCa02, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)

    posCa03 = [0.1568316876978241,
               0.2199067639991236,
               0.5234951803941564,
               -1.4851164489085167,
               -0.677919238739707,
               -0.635198014607513]
    rtde_c.moveL(posCa03, 0.1, 0.1)
    posCa04 = [0.21139567855487623,
               0.2706275099445283,
               0.5438238597184026,
               -1.535369400769388,
               -0.6486672057417355,
               -0.6462199428337463]
    rtde_c.moveL(posCa04, 0.1, 0.1)

    home_position(rtde_c)



def pickup_1_3(ardu,rtde_c):
    home_position(rtde_c)

    posCaminus1 = [0.18258539135209367,
                   0.34237949883831,
                   0.5118164080334295,
                   -1.4564707803249504,
                   0.6975415335895895,
                   0.5703154832114745]
    rtde_c.moveL(posCaminus1, 0.1, 0.1)

    posCaminus2 = [0.146120374241993,
                   0.2947705615654465,
                   0.5561010885422959,
                   -1.5317463418365234,
                   -0.6669416675807128,
                   -0.5551648224932388]
    rtde_c.moveL(posCaminus2, 0.1, 0.1)
    posCaminus2j = [1.3919613361358643,
                    -1.178955380116598,
                    -2.0018580595599573,
                    -0.031080071126119435,
                    1.7977150678634644,
                    -0.7892864386187952]
    rtde_c.moveJ(posCaminus2j)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third carrot
    posCa01 = [0.14622640717288993,
               0.32255336441593346,
               0.7163293428336078,
               -1.5253846466889336,
               -0.6774004011965016,
               -0.542659266683178]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)

    posCa03 = [0.1568316876978241,
               0.2199067639991236,
               0.5234951803941564,
               -1.4851164489085167,
               -0.677919238739707,
               -0.635198014607513]
    rtde_c.moveL(posCa03, 0.1, 0.1)

    posCa04 = [0.21139567855487623,
               0.2706275099445283,
               0.5438238597184026,
               -1.535369400769388,
               -0.6486672057417355,
               -0.6462199428337463]

    rtde_c.moveL(posCa04, 0.1, 0.1)

    home_position(rtde_c)


def pickup_1_4(ardu, rtde_c):
    home_position(rtde_c)

    posCaminus1 = [0.18258539135209367,
                   0.34237949883831,
                   0.5118164080334295,
                   -1.4564707803249504,
                   0.6975415335895895,
                   0.5703154832114745]
    rtde_c.moveL(posCaminus1, 0.1, 0.1)

    posCaminus2 = [0.146120374241993,
                   0.2947705615654465,
                   0.5561010885422959,
                   -1.5317463418365234,
                   -0.6669416675807128,
                   -0.5551648224932388]
    rtde_c.moveL(posCaminus2, 0.1, 0.1)
    posCaminus2j = [1.3919613361358643,
                    -1.178955380116598,
                    -2.0018580595599573,
                    -0.031080071126119435,
                    1.7977150678634644,
                    -0.7892864386187952]
    rtde_c.moveJ(posCaminus2j)

    gripper_open(ardu)
    # 1 picking the forth carrot
    posCa01 = [0.1554158418529502,
               0.377974946588332,
               0.7172337680544484,
               -1.5317379643434768,
               -0.6668989706792583,
               -0.5550929816136247]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)

    posCa03 = [0.1568316876978241,
               0.2199067639991236,
               0.5234951803941564,
               -1.4851164489085167,
               -0.677919238739707,
               -0.635198014607513]
    rtde_c.moveL(posCa03, 0.1, 0.1)
    posCa04 = [0.21139567855487623,
               0.2706275099445283,
               0.5438238597184026,
               -1.535369400769388,
               -0.6486672057417355,
               -0.6462199428337463]

    rtde_c.moveL(posCa04, 0.1, 0.1)

    home_position(rtde_c)



