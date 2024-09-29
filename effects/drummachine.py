import mido
from effects import Connectable
import subprocess

mido.set_backend('mido.backends.rtmidi/UNIX_JACK')

class DrumMachine(Connectable):
    def __init__(self, system, name):
        self.system = system
        self.name = name
        self.port = mido.open_output('Out', client_name=self.name)
        mins = self.get_midi_inputs()
        mouts = self.get_midi_outputs()
        self.actions = {}
        super().__init__([], [], mins, mouts)
        
    def get_midi_inputs(self):
        return []
    def get_midi_outputs(self):
        return self.system.client.get_ports(name_pattern=self.name, is_midi=True, is_audio=False, is_input=False, is_output=True)

    def play(self):
        self.port.send(mido.Message('start'))
    def stop(self):
        self.port.send(mido.Message('stop'))
    def cont(self):
        self.port.send(mido.Message('continue'))        
    def pattern(self, i):
        self.port.send(mido.Message('program_change', program=i))
