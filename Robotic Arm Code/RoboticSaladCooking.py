from pyfirmata import Arduino,SERVO, util
import serial
from subprocess import call
import numpy as np
import rtde_receive
import rtde_control
from time import sleep
import time
import pyfirmata
pos = None
pos1 = None
rtde_c = None
rtde_r = None
ardu = None

   

rtde_c = rtde_control.RTDEControlInterface("169.254.141.189")
# import serial library
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.141.189")

ardu = serial.Serial('COM7', 9600)




   
# pos=rtde_r.getActualTCPPose()
#get a position in JOINT SPACE
# pos_j = rtde_r.getActualQ()
# rtde_c.moveJ(PosHj)

# The Home Position for the robot

def Home_pos():
    PosH =[0.3228078180879545,
     0.4075408368142595,
     0.47817282408694783,
     -1.437686088994754,
     0.47144575808011246,
     0.6379876392044342]
    rtde_c.moveL(PosH, 0.1, 0.1)
    
    PosHj=[1.0196882486343384,
     -1.7856414953814905,
     -1.6905539671527308,
     0.4508479833602905,
     2.2006947994232178,
     0.7832316756248474]
    

    #Move in joint position
    rtde_c.moveJ(PosHj)
    
def open_griper():
    command =120    # query servo position
    # write position to serial port
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    reachedPos = str(ardu.readline())
    print(reachedPos)
def close_griper():
    command =60    # query servo position
    # write position to serial port
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    reachedPos = str(ardu.readline())
    print(reachedPos)
    
    


# --------------------------------------------------------------
# -------------------Opening the FryCutter ----------------------
# ..................................................................
def Fry_Open():
    Home_pos()
    
    pospf00 =[0.32563449264740296,
     0.4053858882485881,
     0.6384206822950311,
     -1.3775113959478176,
     0.5965277532220965,
     0.5805400745204232]

    rtde_c.moveL(pospf00, 0.1, 0.1)

    # 1.
    pospf01 = [0.333434796062715,
     0.440411635865945,
     0.6351295265176796,
     -1.5778553554037251,
     0.20519826733169616,
     0.9464417155857552]

    rtde_c.moveL(pospf01, 0.1, 0.1)

# 2.

    pospf02 =[0.3334367952838217,
     0.4403892072948594,
     0.5031593368009996,
     -1.5778012807021435,
     0.2052640326665511,
     0.9464860325733067]

    rtde_c.moveL(pospf02, 0.1, 0.1)


# 3.

    pospf03 = [0.26415420272021084,
     0.42914385054203497,
     0.5351308836899269,
     -1.649787380346543,
     0.0007451857423465452,
     1.117648679135792]

    rtde_c.moveL(pospf03, 0.1, 0.1)

# 4.

    pospf04 =[0.2641426030793591,
     0.4291682346213929,
     0.42832109439242766,
     -1.6498659378271576,
     0.0007447050244307755,
     1.1177671221659948]

    rtde_c.moveL(pospf04, 0.1, 0.1)


# 5.

    pospf05 =[0.2809409918670357,
     0.45490278482119967,
     0.45152376952459045,
     -1.7551650750230496,
     0.005188844162390683,
     1.2740517651343415]
    rtde_c.moveL(pospf05, 0.1, 0.1)

# 6.

    pospf06 = [0.06980985036429335,
     0.4534832356502383,
     0.4515706585472972,
     -1.75512160952841,
     0.005128681772177666,
     1.2739806500487767]

    rtde_c.moveL(pospf06, 0.1, 0.1)

# 7.

    pospf07 =[0.0697903677489854,
     0.4534908648578175,
     0.533742927790795,
     -1.7551321400647864,
     0.0051723877297357775,
     1.2740525577754878]
    rtde_c.moveL(pospf07, 0.1, 0.1)

# 8.

    pospf08 =[0.06981738887835182,
     0.453487606953564,
     0.39692115767105385,
     -1.755250523845164,
     0.0053354687432710345,
     1.2740306639029888]
    rtde_c.moveL(pospf08, 0.1, 0.1)

# 9.

    pospf09 = [0.25701667889649404,
     0.38512086550615365,
     0.3968569830122436,
     -1.623535583192222,
     0.4104112209044474,
     0.9116281937881283]
    rtde_c.moveL(pospf09, 0.1, 0.1)


# # 10.

#     pospf10 = [0.041297632048866106,
#      0.48428803680908766,
#      0.5238892354684417,
#      1.6485273334987736,
#      1.1128007466418584,
#      1.946837792040326]
#     rtde_c.moveL(pospf10, 0.1, 0.1)

# # 11.

#     pospf11 =[0.04131574903947861,
#      0.48428794564891753,
#      0.410547447567321,
#      1.64859799373051,
#      1.1127265584212203,
#      1.9469435487749733]
#     rtde_c.moveL(pospf11, 0.1, 0.1)

# # 12.

#     pospf12 = [0.19899361870810178,
#      0.371670321782027,
#      0.45797346181962884,
#      1.7370868556495112,
#      0.7376804791741653,
#      1.7589223933143268]
#     rtde_c.moveL(pospf12, 0.1, 0.1)

    Home_pos()

# --------------------------------------------------------------
# ------------------ Closing  the FryCutter ----------------------
# ..................................................................

def Fry_close():
    # close_griper()
    Home_pos()
    
    # -1.

    poscf0_1 =[0.07363422046751336,
     0.30945342816021876,
     0.5845030583843931,
     -1.5709322545266298,
     0.09831211947987406,
     1.0447391302723958]
    rtde_c.moveL(poscf0_1, 0.1, 0.1)
# 0.

    poscf00 =[0.0840221539045191,
     0.3979826934336227,
     0.6740917984256257,
     -1.6624237703690488,
     -0.12520975785584595,
     1.247022333667785]
    rtde_c.moveL(poscf00, 0.1, 0.1)


# 1.

    poscf01 =[0.06366290373788336,
     0.5105507092469657,
     0.6204055441043393,
     -1.7598049037509162,
     -0.10550659379085298,
     1.3282169465645222]
    rtde_c.moveL(poscf01, 0.1, 0.1)


# 2.

    poscf02 =[0.06880087552135175,
     0.504281179372786,
     0.5161540202607664,
     -1.7182286412839902,
     -0.13334918877813792,
     1.3063480412759672]
    rtde_c.moveL(poscf02, 0.1, 0.1)


# 3.

    poscf03 = [0.2000403039702242,
     0.4932136840643457,
     0.4755467617323064,
     -1.7878184354242992,
     -0.11716028235960387,
     1.2810358257872658]
    rtde_c.moveL(poscf03, 0.1, 0.1)


# 4.

    poscf04 =[0.04711572471845529,
     0.49895057745210447,
     0.446282725482377,
     -1.8088107501426316,
     -0.4016519750152498,
     1.4800784879249507]
    rtde_c.moveL(poscf04, 0.1, 0.1)

# 5.

    poscf05 = [0.021976691051834127,
     0.5901870164105257,
     0.4249832080771825,
     -1.8873913448019022,
     -0.37965105517165737,
     1.557742209824812]
    rtde_c.moveL(poscf05, 0.1, 0.1)

# 6.

    poscf06 =[0.1510190496592031,
     0.5922739392870862,
     0.4350305230533722,
     -1.8287341112805882,
     -0.26412515783712426,
     1.4517417882972379]
    rtde_c.moveL(poscf06, 0.1, 0.1)

# 7.

    poscf07 =[0.2622223696853836,
     0.5755998231462929,
     0.4574286618132777,
     -1.7595830876543146,
     -0.16162989899053287,
     1.2787807467486991]
    rtde_c.moveL(poscf07, 0.1, 0.1)

# 8.

    poscf08 = [0.3068958144802971,
     0.5801505283072038,
     0.5475069588439021,
     -1.7528228876905723,
     -0.10108474070503509,
     1.2349152426448136]
    rtde_c.moveL(poscf08, 0.1, 0.1)
# 9.

    poscf09 = [0.2344437427575636,
     0.37996522035111646,
     0.45489012624864317,
     -1.7904345181688337,
     0.014366632186935057,
     1.2590017722998332]
    rtde_c.moveL(poscf09, 0.1, 0.1)
# # 10.

#     poscf10 =[0.2893510555089456,
#      0.417847048782917,
#      0.4657058702478322,
#      1.3928657964106061,
#      1.0247373259745165,
#      1.1223704828968226]
#     rtde_c.moveL(poscf10, 0.1, 0.1)
# # 11.

#     poscf11 =[0.2984919812330183,
#      0.38164959960880745,
#      0.520655223632495,
#      1.6511272222140212,
#      0.6856100556590978,
#      1.4013468916313456]
#     rtde_c.moveL(poscf11, 0.1, 0.1)
    Home_pos()

def ing_delivary():
    posD01 = [0.24490629655137514,
     0.548428810490081,
     0.4006335106168221,
     -1.6715873471236302,
     0.8168989758234155,
     -1.9130056256272403]
    rtde_c.moveL(posD01, 0.1, 0.1)
    
    posD02 =[0.21462867782488143,
     0.5534235349106671,
     0.4563451131925963,
     -1.6291266090936931,
     0.8203488381579122,
     -1.8292749541410491]
    rtde_c.moveL(posD02, 0.1, 0.1)
    
    open_griper()
    
    posD03 = [0.2922202506157643,
     0.40281992118106213,
     0.40224629950428,
     -1.6491503965614656,
     0.9837880143663791,
     -1.9508065221266504]
    rtde_c.moveL(posD03, 0.1, 0.1)
    
    
     

#  Carrot picking
def First_Carrot_picking_1_1():
    
    #0
    
    
    posCaminus1 =  [0.15259306874630196,
     0.2628014118363295,
     0.46225485781199555,
     -1.80470256629448,
     0.5916533258727816,
     -1.6315713652371373]
    rtde_c.moveL(posCaminus1, 0.1, 0.1)
  
    
    
    open_griper()
    #1 picking the first carrot
    posCa01 = [-0.24766236378363862,
     -0.20070583756851207,
     0.6700391343851001,
     0.9329823804139694,
     -1.7347264182279218,
     1.7209087975102504]
    rtde_c.moveL(posCa01, 0.1, 0.1)
    
    close_griper()
    
    posCa02 = [-0.24765085722884256,
     -0.2006715675131316,
     0.5416518744917878,
     0.933048150430117,
     -1.7346561350780505,
     1.7209780183166001]
    rtde_c.moveL(posCa02, 0.1, 0.1)
    
    posCa03 = [-0.2083130476310146,
     -0.25869170483365356,
     0.4897825002819879,
     -0.6056643336535551,
     -1.515148801314544,
     0.7150208495155058]
    
    rtde_c.moveL(posCa03, 0.1, 0.1)
    ing_delivary()
    
   
    
def Second_Carrot_picking_1_2():
       
       posCaminus1 =  [-0.336234891594495,
        -0.21226787886393889,
        0.5219556305322177,
        0.891562689386263,
        -1.7093246703659977,
        1.8237317984580248]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.33622353496919477,
        -0.21225065886602087,
        0.6697416846893806,
        0.8916900677664332,
        -1.7091699788035828,
        1.8237205195418305]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()
       
       
def Third_Carrot_picking():
       
       posCaminus1 =  [-0.40946690468364194,
        -0.2122597511594027,
        0.5187564063679583,
        0.8914295341248326,
        -1.7095029976650826,
        1.8237350975173408]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.3540494214143006,
        -0.2560103478872642,
        0.6693293866209735,
        -0.5636807759566101,
        -1.5290129861639425,
        0.6256004583812227]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()
       
        
def First_Appel_picking():
       
       posCaminus1 =  [0.13622724581017567,
        0.2379988134736593,
        0.4518504254832432,
        -1.6909430694890812,
        0.5423653610041956,
        -1.7353626691849386]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the first Appel
       posCa01 = [0.09362679679778793,
        0.264536060100632,
        0.7065929085919198,
        -1.6595581660895438,
        0.6379472452841989,
        -1.8469386510045478]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [0.09361833245982604,
        0.26452399846578883,
        0.4857743298373148,
        -1.6595955254156618,
        0.6378057568306437,
        -1.8470367108986652]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [0.19443851739913676,
        0.35846743140861775,
        0.46329869094798465,
        -1.6671371169833928,
        0.6253473459637443,
        -1.8905589569059649]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary() 
def Second_Appel_picking():
       
       posCaminus1 =  [-0.34322235633280734,
        -0.28957913880821085,
        0.5365909422258927,
        0.790480647534006,
        -1.6956996495430186,
        1.806295202804724]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second Appel
       posCa01 = [-0.3333920835041708,
        -0.2879919109133574,
        0.6647426813794077,
        0.8102632889573637,
        -1.657783115715506,
        1.8167057277842682]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()  
        
       posCaminus1 =  [-0.40380947947219015,
        -0.2895532657819093,
        0.5446187511292365,
        0.7903237262003264,
        -1.6956739834931465,
        1.8062156068648687]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.4037612435985397,
        -0.28958508982476994,
        0.6670233322214016,
        0.7904110579730345,
        -1.6956292149903458,
        1.8063102130743203]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()  
        
    
def First_Bannana_picking():
       
       posCaminus1 =  [-0.22699770960605947,
        -0.3799320558717814,
        0.5690242375416242,
        -0.4991294993795321,
        -1.5382713251629299,
        0.6470485826083119]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.19348448493233583,
        -0.3746945735450818,
        0.6717832757252628,
        -0.47737663111492085,
        -1.545753119638913,
        0.672942466240558]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()  

def Second_Bannana_picking():
       
       posCaminus1 =  [-0.27388635831371133,
        -0.3747463231976781,
        0.5637683004195567,
        -0.47725737468681256,
        -1.5457732319123891,
        0.6727889746943493]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.27378754117173737,
        -0.37425430772595225,
        0.668718713523517,
        -0.4691853505377986,
        -1.5520019009960775,
        0.6622376464308183]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary()
def Third_Bannana_picking():
       
       posCaminus1 =  [-0.36861420016794233,
        -0.38383602064774824,
        0.5614136509519088,
        -0.4691014513382586,
        -1.5520339310336853,
        0.6621929431126866]
       rtde_c.moveL(posCaminus1, 0.1, 0.1)
     
       
       
       open_griper()
       #1 picking the second carrot
       posCa01 = [-0.3596944224417364,
        -0.3799099649685061,
        0.6678485466919352,
        -0.4912527495359406,
        -1.519848135368884,
        0.7135943878780115]
       rtde_c.moveL(posCa01, 0.1, 0.1)
       
       close_griper()
       
       posCa02 = [-0.24765085722884256,
        -0.2006715675131316,
        0.5416518744917878,
        0.933048150430117,
        -1.7346561350780505,
        1.7209780183166001]
       rtde_c.moveL(posCa02, 0.1, 0.1)
       
       posCa03 = [-0.2083130476310146,
        -0.25869170483365356,
        0.4897825002819879,
        -0.6056643336535551,
        -1.515148801314544,
        0.7150208495155058]
       
       rtde_c.moveL(posCa03, 0.1, 0.1)
       ing_delivary() 
    
    


if __name__=='__main__':
    
      Home_pos()
      # Fry_Open()
      # First_Carrot_picking()
      # Fry_close()
      # Fry_Open()
      # Second_Carrot_picking()
      # Fry_close()
      # Fry_Open()
      # Third_Carrot_picking()
      # Fry_close()
      # Fry_Open()
      # First_Appel_picking()
      # Fry_close()
      # Fry_Open()
      # Second_Appel_picking()
      # Fry_close()
      # Fry_Open()
      # Third_Appel_picking()
      # Fry_close()
      # Fry_Open()
      # First_Bannana_picking()
      # Fry_close()
      # Fry_Open()
      # Second_Bannana_picking()
      # Fry_close()
      # Fry_Open()
      # Third_Bannana_picking()
      # Fry_close()

    # Fry_close()s
    #Carrot_picking()
    # close_grioer()
      # open_griper()
    
    
    


