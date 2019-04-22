from ev3dev.auto import *
import sys
import math

m_a = LargeMotor(OUTPUT_A)
m_b = LargeMotor(OUTPUT_B)
m_c = MediumMotor(OUTPUT_C)
controller = TouchSensor(INPUT_1)
m_c.position = 0
m_a.position = 0
ctPos = 0



def motorsReset():
    m_a.reset()
    m_b.reset()
    m_c.reset()
    print('All motors reset')

def motorsControll(command):
    if (command == 'up'):
        m_b.run_timed(time_sp=1000, speed_sp=-350, stop_action='hold')
    elif (command == 'down'):
        m_b.run_timed(time_sp=1000, speed_sp=250, stop_action='coast')
    elif (command == 'take'):
        m_c.run_timed(time_sp=450, speed_sp=250, stop_action='hold')
    elif (command == 'drop'):
        m_c.run_timed(time_sp=400, speed_sp=-250, stop_action='coast')
    elif (command == 'left'):
        m_a.run_timed(time_sp=400, speed_sp=-250, stop_action='hold')
    elif (command == 'right'):
        m_a.run_timed(time_sp=400, speed_sp=250, stop_action='hold')
    elif(command == 'calibration'):
        motorsControll('up')
        m_b.wait_while('running')
        if (m_b.is_holding):
            while(1):
                m_a.run_timed(time_sp=100, speed_sp=100, stop_action='coast')
                m_a.wait_while('running' )
                if (controller.is_pressed):
                    break
            if not (m_a.is_running):
                print('Calibration was successful')

def pointControll(fPos):
    key = int(fPos - ctPos)
    speed = (1 if key > 0 else -1) * 250
    key = abs(key)
    while(key):
        m_a.run_timed(time_sp=400, speed_sp=speed, stop_action='hold')
        m_a.wait_while('running')
        if not (m_a.is_running):
            key = key - 1



def getch():
    #Returns a single character from standard input
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch




motorsReset()
log = 0
motorsControll('calibration')
while (1):
    pressedKey = getch()
    if pressedKey == '1': pointControll(1)
    if pressedKey == '2': pointControll(2)
    if pressedKey == '3': pointControll(3)
    if pressedKey == '4': pointControll(4)
    if pressedKey == '5': pointControll(-1)
    if pressedKey == '6': pointControll(-2)
    if pressedKey == '7': pointControll(-3)
    if pressedKey == '8': pointControll(-4)


    if pressedKey == 'w': motorsControll('up')
    if pressedKey == 's': motorsControll('down')
    if pressedKey == ' ':
        if (log == 0):
            motorsControll('take')
            log = 1
        else:
            motorsControll('drop')
            log = 0
    if pressedKey == 'q': break

motorsReset()