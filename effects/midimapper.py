import mido
from effects import Connectable

mido.set_backend('mido.backends.rtmidi/UNIX_JACK')

class MidiMapper(Connectable):
    def __init__(self, system):
        self.system = system
        self.mode = "Default"
        # Map of hex to hex midi messages for mapping one to another
        self.modes = {}
        self.input_port = mido.open_input('In', client_name="MidiMapper-In", callback=self.callback)
        self.output_port = mido.open_output('Out', client_name="MidiMapper-Out")
        mins = self.get_midi_inputs()
        mouts = self.get_midi_outputs()
        self.actions = {}
        super().__init__([], [], mins, mouts)
    
    def set_mode(self, m):
        self.mode = m
    def add_mode(self, m, map):
        self.modes[m] = map
    def get_midi_inputs(self):
        return self.system.client.get_ports(name_pattern="MidiMapper-In", is_midi=True, is_audio=False, is_input=True, is_output=False)
    def get_midi_outputs(self):
        return self.system.client.get_ports(name_pattern="MidiMapper-Out", is_midi=True, is_audio=False, is_input=False, is_output=True)
    def callback(self, msg):
        # use first 2 bytes as key
        k = self._key(msg)
        # Check if mode exists
        if self.mode in self.modes:
            mode = self.modes[self.mode]
            # map the message if it's there
            if( k in mode):
                m = mode[k](msg)
                print(f"Sending: {m}")
                self.output_port.send(m.copy())
            else:
                self.output_port.send(msg.copy())
            
        else:
            self.output_port.send(msg.copy())

    def _key(self, msg):
        return msg.hex().rsplit(' ', 1)[0]
