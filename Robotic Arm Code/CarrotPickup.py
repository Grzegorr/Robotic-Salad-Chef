from BasicFunctions import *
import time

def pickup_4_1(ardu, rtde_c):
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
    posCaminus3 = [0.3377652169306871,
                   0.21207150849981743,
                   0.5880181102144919,
                   -1.5354280834644545,
                   -0.6486767708344444,
                   -0.6461938638842545]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third carrot
    posCa01 = [0.34296133067486934,
               0.20844247167937557,
               0.7225869779661505,
               -1.53534956349367,
               -0.6487468386849835,
               -0.6462227600914394]
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


def pickup_4_2(ardu, rtde_c):
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
    posCaminus3 = [0.3377652169306871,
                   0.21207150849981743,
                   0.5880181102144919,
                   -1.5354280834644545,
                   -0.6486767708344444,
                   -0.6461938638842545]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the second brocolli
    posCa01 = [0.3458971037364195,
               0.26788650376030115,
               0.7215419328811815,
               -1.5353032664280395,
               -0.6487315173526299,
               -0.6462349605892544]
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


def pickup_4_3(ardu, rtde_c):
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
    posCaminus3 = [0.37371554791683254,
                   0.3337584741747297,
                   0.5918990488527087,
                   -1.5354955320197092,
                   -0.6487161036453648,
                   -0.6461637620185643]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the third brocolli
    posCa01 = [0.34323792807516423,
               0.3356227269599849,
               0.7184808793630573,
               -1.5353903990277917,
               -0.6486729653386447,
               -0.6463008297048017]
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


def pickup_4_4(ardu, rtde_c):
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
    posCaminus2_5 = [0.34702997198163255,
                     0.3700829246864843,
                     0.5568647788555123,
                     -1.5352599427331115,
                     -0.6486863228691393,
                     -0.6463035935904136]
    rtde_c.moveL(posCaminus2_5, 0.1, 0.1)
    posCaminus3 = [0.34702147810865674,
                   0.3700919308588091,
                   0.6571479539217147,
                   -1.5354281912855003,
                   -0.6486244643228939,
                   -0.6462175365313766]

    rtde_c.moveL(posCaminus3, 0.1, 0.1)
    posCaminus4 = [0.34849370794406614,
                   0.3993237529337524,
                   0.6571350847095196,
                   -1.5354145555685925,
                   -0.6486335365356994,
                   -0.6461710561499663]

    rtde_c.moveL(posCaminus4, 0.1, 0.1)

    gripper_open(ardu)
    time.sleep(1)

    # 1 picking the 4th carrot
    posCa01 = [0.3484775690695411,
               0.39935524970673975,
               0.7189600159306342,
               -1.535291601554828,
               -0.6487673262724913,
               -0.6463153738323639]
    rtde_c.moveL(posCa01, 0.1, 0.1)

    gripper_close(ardu)
    time.sleep(1)


    posCaminus4 = [0.34849370794406614,
                   0.3993237529337524,
                   0.6571350847095196,
                   -1.5354145555685925,
                   -0.6486335365356994,
                   -0.6461710561499663]

    rtde_c.moveL(posCaminus4, 0.1, 0.1)

    posCaminus3 = [0.34702147810865674,
                   0.3700919308588091,
                   0.6571479539217147,
                   -1.5354281912855003,
                   -0.6486244643228939,
                   -0.6462175365313766]
    rtde_c.moveL(posCaminus3, 0.1, 0.1)

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