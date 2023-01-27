def open_griper(ardu):
    command =120    # query servo position
    # write position to serial port
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    reachedPos = str(ardu.readline())
    print(reachedPos)

def close_griper(ardu):
    command =60    # query servo position
    # write position to serial port
    ardu.write(str(command).encode())
    # read serial port for arduino echo
    reachedPos = str(ardu.readline())
    print(reachedPos)