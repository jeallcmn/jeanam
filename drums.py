import mido

map = { 
    "90 01" : lambda m: mido.Message('start'),
    "90 02" : lambda m: mido.Message('stop'),
    "90 03" : lambda m: mido.Message('continue')
}

def register(midimapper):
    midimapper.add_mode("drum-machine", map)
