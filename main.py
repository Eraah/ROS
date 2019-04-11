from ev3dev.auto import *
import sys

m_a = LargeMotor(OUTPUT_A)
m_b = LargeMotor(OUTPUT_B)
m_c = MediumMotor(OUTPUT_C)
m_c.position = 0



def motorsReset():
    m_a.reset()
    m_b.reset()
    m_c.reset()
    print('All motors reset')

def motorsControll(command):
    if (command == 'up'):
        m_b.run_timed(time_sp=1000, speed_sp=-150, stop_action='hold')
    elif (command == 'down'):
        m_b.run_timed(time_sp=1000, speed_sp=60, stop_action='coast')
    elif (command == 'take'):
        m_c.run_timed(time_sp=450, speed_sp=250, stop_action='hold')
    elif (command == 'drop'):
        m_c.run_timed(time_sp=400, speed_sp=-250, stop_action='coast')
    elif (command == 'left'):
        m_a.run_timed(time_sp=400, speed_sp=-250, stop_action='coast')
    elif (command == 'right'):
        m_a.run_timed(time_sp=400, speed_sp=250, stop_action='coast')

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
while (1):
    pressedKey = getch()

    if pressedKey == 'a': motorsControll('left')
    if pressedKey == 'd': motorsControll('right')

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