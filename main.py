# import mido
# mido.set_backend('mido.backends.rtmidi/UNIX_JACK')

# def callback(msg):
#     print(msg)

# in_port = mido.open_input('In', client_name="JEANAM-In", callback=callback)

import modhost
import effects
import jeanam.system

system = jeanam.system.System()
host = modhost.Host()

amp = effects.Effect(host, system, 'http://github.com/mikeoliphant/neural-amp-modeler-lv2')
cab = effects.Effect(host, system, 'http://lsp-plug.in/plugins/lv2/impulse_responses_stereo')
reverb = effects.Effect(host, system, 'urn:dragonfly:room')
poweramp = effects.Effect(host, system, 'http://eq10q.sourceforge.net/eq/eq4qm')

# print (amp)
# print (cab)
# print (reverb)
# 

# amp.patch('model', '/home/jon/Amps/REVV 02.nam')
amp.preset('GSP2101 Saturated')
cab.preset('V30 Stereo')
reverb.preset('VocalHall')

system.connect(system.audio_outputs[1], amp.audio_inputs[0])
system.connect(amp.audio_outputs[0], poweramp.audio_inputs[0])

system.connect(poweramp.audio_outputs[0], cab.audio_inputs[0])
system.connect(poweramp.audio_outputs[0], cab.audio_inputs[1])
system.connect(cab.audio_outputs[0], reverb.audio_inputs[0])
system.connect(cab.audio_outputs[1], reverb.audio_inputs[1])
system.connect(reverb.audio_outputs[0], system.audio_inputs[0])
system.connect(reverb.audio_outputs[1], system.audio_inputs[1])

# Resonance
poweramp.param('filter2_enable', 1)
poweramp.param('filter2_gain', 6)
poweramp.param('filter2_freq',95)
poweramp.param('filter2_q', 2.0)
poweramp.param('filter2_type', 11)
# Presence
poweramp.param('filter4_enable',1)
poweramp.param('filter4_gain', 6)
poweramp.param('filter4_freq',10000)
poweramp.param('filter4_q', 0.2)
poweramp.param('filter4_type',11)


# print ("System Inputs:", system.inputs)
# print ("System Outputs:", system.outputs)

# print(client.get_ports(is_audio=True, is_physical=True, is_input=True))
# print()
    # def audio_outputs(self):
    #     return self.client.get_ports(is_audio=True, is_physical=True, is_output=True)
    # def midi_inputs(self):
    #     return self.client.get_ports(is_midi=True, is_physical=True, is_input=True)
    # def midi_outputs(self):
    #     return self.client.get_ports(is_midi=True, is_physical=True, is_output=True)


