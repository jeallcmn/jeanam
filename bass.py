import mido

D = 36
E  = 38
amount = 16
def shiftUp(msg):
    m2 = msg.copy()
    m2.note = m2.note + amount
    m2.channel = 2
    return m2

events = ["90", "80"]
notes = [
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
    "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13"
]

map = {}
for e in events:
    for n in notes:
        map[f"{e} {n}"] = shiftUp

def register(midimapper):
    midimapper.add_mode("bass", map)
