from effects import Connectable


class JackEffect(Connectable):
    """
        This is a special effect that "captures" a Jack client and treats it like a normal effect
        for connection purposes.
    """
    def __init__(self, system, audio_name, midi_name, audio_port_pattern=None, midi_port_pattern=None):
        self.system = system
        self.audio_name = audio_name
        self.midi_name = midi_name
        self.audio_port_pattern = f"{audio_name}.*{audio_port_pattern}.*" if audio_port_pattern else audio_name
        self.midi_port_pattern = f"{midi_name}.*{midi_port_pattern}.*" if midi_port_pattern else midi_name
        ins = self.get_audio_inputs()
        outs = self.get_audio_outputs()
        
        mins = self.get_midi_inputs()
        mouts = self.get_midi_outputs()
        super().__init__(ins, outs, mins, mouts)
        
    def get_audio_outputs(self):
        return self.system.client.get_ports(name_pattern=self.audio_port_pattern, is_audio=True, is_input=False, is_output=True)
    def get_audio_inputs(self):
        return self.system.client.get_ports(name_pattern=self.audio_port_pattern, is_audio=True, is_input=True, is_output=False)    
    def get_midi_inputs(self):
        return self.system.client.get_ports(name_pattern=self.midi_port_pattern, is_midi=True, is_audio=False, is_input=True, is_output=False)
    def get_midi_outputs(self):
        return self.system.client.get_ports(name_pattern=self.midi_port_pattern, is_midi=True, is_audio=False, is_input=False, is_output=True)
