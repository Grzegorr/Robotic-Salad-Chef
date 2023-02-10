from BasicFunctions import *
import time

def pickup_5_1(ardu, rtde_c):
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
    posCaminus3 = [0.3915354702521135,
                   0.22361557214150346,
                   0.6101258219529017,
                   -1.5353672652521035,
                   -0.648561075587501,
                   -0.6463065222218204]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third carrot
    posCa01 = [0.3973483141700734,
               0.2097961520366089,
               0.7184890731123023,
               -1.535401410172382,
               -0.6485792030082733,
               -0.6463712891887967]
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


def pickup_5_2(ardu, rtde_c):
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
    posCaminus3 = [0.4002299252608539,
                   0.2673293910833982,
                   0.613118883834049,
                   -1.5353904046300995,
                   -0.6486249412181139,
                   -0.6462525960281501]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the second brocolli
    posCa01 = [0.4002261261337913,
               0.2673131659485176,
               0.7199333042452378,
               -1.5353725165085614,
               -0.6486692766605181,
               -0.6463274109421986]
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


def pickup_5_3(ardu, rtde_c):
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
    posCaminus3 = [0.40360577243537615,
                   0.33569002179281127,
                   0.6131335579556012,
                   -1.535350402519954,
                   -0.648644037549917,
                   -0.6462588654997419]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third orange
    posCa01 = [0.4029851430912197,
               0.3221545375412961,
               0.7177679425431716,
               -1.5353835840592502,
               -0.648686186869534,
               -0.6463126927463609]
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


def pickup_5_4(ardu, rtde_c):
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
    posCaminus2_5 = [0.405400696530754,
                     0.3703346931822074,
                     0.5907486680449593,
                     -1.5353996264999523,
                     -0.6485335059155813,
                     -0.6464090098470654]
    rtde_c.moveL(posCaminus2_5, 0.1, 0.1)
    posCaminus3 = [0.4007975041573218,
                   0.37254412048912877,
                   0.6713620232265092,
                   -1.5353096137535227,
                   -0.6486449641119878,
                   -0.6464393275264537]

    rtde_c.moveL(posCaminus3, 0.1, 0.1)
    posCaminus4 = [0.40216932219512513,
                   0.40015368800696105,
                   0.6712962822295434,
                   -1.535401771554998,
                   -0.6487068923423509,
                   -0.6461298527949874]

    rtde_c.moveL(posCaminus4, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third carrot
    posCa01 = [0.40186506948806644,
               0.39375051293505015,
               0.7187197241835823,
               -1.5353116336548376,
               -0.6486739591709859,
               -0.6463159897780291]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)

    posCaminus4 = [0.40216932219512513,
                   0.40015368800696105,
                   0.6712962822295434,
                   -1.535401771554998,
                   -0.6487068923423509,
                   -0.6461298527949874]

    rtde_c.moveL(posCaminus4, 0.1, 0.1)
    posCaminus3 = [0.4007975041573218,
                   0.37254412048912877,
                   0.6713620232265092,
                   -1.5353096137535227,
                   -0.6486449641119878,
                   -0.6464393275264537]

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