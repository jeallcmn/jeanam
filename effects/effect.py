
from presets import get_presets

class Effect:
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
        self.audio_inputs = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_audio=True, is_physical=False, is_input=True, is_output=False);
        self.audio_outputs = self.system.client.get_ports(name_pattern=f"effect_{self.id}.*", is_audio=True, is_physical=False, is_input=False, is_output=True);
        self.presets = get_presets(uri)
    def __str__(self):
        return f"""Effect {self.uri}
    Audio Inputs:  {[x.name for x in self.audio_inputs]}
    Audio Outputs: {[x.name for x in self.audio_outputs]}"""

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
    