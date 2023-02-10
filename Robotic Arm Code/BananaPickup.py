from BasicFunctions import *
import time

def pickup_2_1(ardu, rtde_c):
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

    # 1 picking the first Apple
    posCa01 = [0.22328792939324446,
               0.2195648530157714,
               0.7185321029019914,
               -1.5353252574987593,
               -0.6487770313338376,
               -0.6462232297144029]
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


def pickup_2_2(ardu, rtde_c):
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

    # 1 picking the second apple
    posCa01 = [0.21601364693602765,
               0.2698816637900554,
               0.7202811338415102,
               -1.5353730594920678,
               -0.6486630860571535,
               -0.6461438035114184]
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


def pickup_2_3(ardu, rtde_c):
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

    # 1 picking the third apple
    posCa01 = [0.21883318392659795,
               0.32635674873798365,
               0.7179546644514946,
               -1.535260003663283,
               -0.6487154719975169,
               -0.6463075703876497]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)

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


def pickup_2_4(ardu, rtde_c):
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

    posCaminus3 = [0.22159530199184727,
                   0.38193931380884877,
                   0.6914031363159648,
                   -1.5352923620544692,
                   -0.6487368187104895,
                   -0.6462995924905934]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    posCaminus4 = [0.22272111268709724,
                   0.40437899564234003,
                   0.691406698795108,
                   -1.5353919412441477,
                   -0.6486411084504022,
                   -0.6461144257287125]
    rtde_c.moveL(posCaminus4, 0.1, 0.1)

    # 1 picking the forth Appel
    posCa01 = [0.22255621499509426,
               0.40070518588350656,
               0.7186461710616404,
               -1.5354263033870132,
               -0.6486637628081579,
               -0.6461953926757017]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)

    posCaminus4 = [0.22272111268709724,
                   0.40437899564234003,
                   0.691406698795108,
                   -1.5353919412441477,
                   -0.6486411084504022,
                   -0.6461144257287125]
    rtde_c.moveL(posCaminus4, 0.1, 0.1)

    posCaminus3 = [0.22159530199184727,
                   0.38193931380884877,
                   0.6914031363159648,
                   -1.5352923620544692,
                   -0.6487368187104895,
                   -0.6462995924905934]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

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

