import serial
import rtde_receive
import rtde_control

pos = None
pos1 = None
rtde_c = None
rtde_r = None
ardu = None

#Connections to the robot
rtde_c = rtde_control.RTDEControlInterface("169.254.141.189")
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.141.189")

#Connection to the Arduino
ardu = serial.Serial('COM7', 9600)

#get a position in JOINT SPACE
pos_j = rtde_r.getActualQ()

#Move in joint position
rtde_c.moveJ(pos_j)






