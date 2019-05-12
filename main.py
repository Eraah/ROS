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
step = 90

ki = 0.01
kd = 0.01
kp = 2


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
                m_a.run_timed(time_sp=100, speed_sp=100, stop_action='hold')
                m_a.wait_while('running' )
                if (controller.is_pressed):
                    m_a.stop(stop_action='coast')
                    break
            if not (m_a.is_running):
                m_a.position = 0
                print('Calibration was successful')

def pointControll(fPos):
    global ctPos
    key = int(fPos - ctPos)
    sign = (1 if key > 0 else -1)
    key = abs(key)
    ctPos = ctPos + fPos
    while(key):
        i = 0
        fAng = step * sign + m_a.position
        dPr = 0
        while (1):
            e = fAng - m_a.position
            i = i + ki * e
            d = kd * (e - dPr)
            u = (kp * e + i + d)
            if (u > 40):
                u = 40
            if (u < -40):
                u = -40
            if (u > 1 and u < 7):
                u = 7
            if (u > -7 and u < -1):
                u = -7
            m_a.run_direct(duty_cycle_sp=u)
            dPr = e
            time.sleep(0.01)
            print(m_a.position)
            if ((m_a.position - fAng < 3) and ((m_a.position - fAng > -3))):
                m_a.stop(stop_action='hold')
                break
        print('finish')
        key = key - 1
        time.sleep(1)
    print(ctPos)


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
    # pressedKey = getch()
    pressedKey = input()
    if pressedKey == '1': pointControll(-1)
    if pressedKey == '2': pointControll(-2)
    if pressedKey == '3': pointControll(-3)
    if pressedKey == '4': pointControll(-4)
    if pressedKey == '5': pointControll(-5)
    if pressedKey == '6': pointControll(-6)
    if pressedKey == '0': pointControll(0)


    if pressedKey == 'w': motorsControll('up')
    if pressedKey == 's': motorsControll('down')
    if pressedKey == ' ':
        if (log == 0):
            motorsControll('take')
            log = 1
        else:
            motorsControll('drop')
            log = 0
    if pressedKey == 'q':
        pointControll(0)
        break



motorsReset()