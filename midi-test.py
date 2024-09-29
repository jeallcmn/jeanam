# import mido
# from effects import Connectable

# mido.set_backend('mido.backends.rtmidi/UNIX_JACK')
# # port = mido.open_input('In', client_name="JEANAM", callback=self.callback)
# port = mido.open_output('Out', client_name="JEANAM")
from effects import DrumMachine
import effects.system

system = effects.system.System()
dm = DrumMachine(system)
