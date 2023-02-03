def gripper_open(ardu):
    command = "120\n"   # query servo position
    # write position to serial port
    print("Sending position command to the gripper.")
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    print("Waiting for answer from arduino.")
    reachedPos = str(ardu.readline())
    print("Reached Position: " + str(reachedPos))

def gripper_grab(ardu):
    command = "90\n"   # query servo position
    # write position to serial port
    print("Sending position command to the gripper.")
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    print("Waiting for answer from arduino.")
    reachedPos = str(ardu.readline())
    print("Reached Position: " + str(reachedPos))

def gripper_close(ardu):
    command = "90\n"   # query servo position
    # write position to serial port
    print("Sending position command to the gripper.")
    ardu.write(command.encode())
    # read serial port for arduino echo
    print("Waiting for answer from arduino.")
    reachedPos = str(ardu.readline())
    print(reachedPos)

def home_position(rtde_c):
    PosH = [0.3228078180879545,
            0.4075408368142595,
            0.47817282408694783,
            -1.437686088994754,
            0.47144575808011246,
            0.6379876392044342]
    rtde_c.moveL(PosH, 0.1, 0.1)

    PosHj = [1.0196882486343384,
             -1.7856414953814905,
             -1.6905539671527308,
             0.4508479833602905,
             2.2006947994232178,
             0.7832316756248474]

    # Move in joint position
    rtde_c.moveJ(PosHj)