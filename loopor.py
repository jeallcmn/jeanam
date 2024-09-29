import mido


def shiftUp(msg):
    print("shifting")
    m2 = msg.copy()
    m2.channel = 2
    return m2

map = { 
    "90 01" : shiftUp,
    "90 02" : shiftUp,
    "90 03" : shiftUp,
    "90 04" : shiftUp,
    "90 05" : shiftUp,
    "90 06" : shiftUp,
    "90 07" : shiftUp,
    "90 08" : shiftUp,
    "90 09" : shiftUp,
    "90 0A" : shiftUp,
    "80 01" : shiftUp,
    "80 02" : shiftUp,
    "80 03" : shiftUp,
    "80 04" : shiftUp,
    "80 05" : shiftUp,
    "80 06" : shiftUp,
    "80 07" : shiftUp,
    "80 08" : shiftUp,
    "80 09" : shiftUp,
    "80 0A" : shiftUp,
}

def register(midimapper):
    midimapper.add_mode("loopor", map)
