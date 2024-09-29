
from effects.plugin import get_presets
from effects.plugin import get_params

class Connectable:
    def __init__(self, audio_inputs, audio_outputs, midi_inputs=[], midi_outputs=[]):
        self.audio_inputs = audio_inputs
        self.audio_outputs = audio_outputs
        self.midi_inputs = midi_inputs
        self.midi_outputs = midi_outputs
    def __str__(self):
        return f"""
    Audio Inputs:  {[x.name for x in self.audio_inputs]}
    Audio Outputs: {[x.name for x in self.audio_outputs]}
    Midi Inputs:  {[x.name for x in self.midi_inputs]}
    Midi Outputs: {[x.name for x in self.midi_outputs]}
"""

class Effect(Connectable):
    nextId = 0
    def __init__(self, host, system, uri):
        self.uri = uri
        self.host = host
        self.id = Effect.nextId
        self.system = system
        # Increment universal ID
        Effect.nextId = Effect.nextId + 1

        self.host.add(self.uri, self.id)
        self.enabled = True
        ins = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_audio=True, is_physical=False, is_input=True, is_output=False)
        outs = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_audio=True, is_physical=False, is_input=False, is_output=True)
        mins = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_midi=True, is_audio=False, is_physical=False, is_input=True, is_output=False)
        mouts = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_midi=True, is_audio=False, is_physical=False, is_input=False, is_output=True)

        super().__init__(ins, outs, mins, mouts)
        self.presets = get_presets(uri)
        self.params = get_params(uri)
    def __str__(self):
        param_str = [x['symbol'] for x in self.params]
        return f"""Effect {self.id} {self.uri} {Connectable.__str__(self)}\tparams: {param_str}"""

    def patch(self, prop, name):
        self.host.patch_set(self.id, f"{self.uri}#{prop}", name)
    def preset(self, name):
        uri = self.presets[name]
        self.host.preset_load(self.id, f"{uri}")
    def param(self, name, value):
        self.host.param_set(self.id, name, value)
    def toggle(self):
        if(self.enabled):
            self.host.bypass(self.id, 1)
            self.enabled = False
        else:
            self.host.bypass(self.id, 0)
            self.enabled = True
    