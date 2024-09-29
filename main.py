
import modhost
import effects
import effects.system
from mido import Message
system = effects.system.System()
host = modhost.Host()
host.transport_sync('midi')
host.transport(1, 4, 120)

midimapper = effects.MidiMapper(system)

amp = effects.Effect(host, system, 'http://github.com/mikeoliphant/neural-amp-modeler-lv2')
poweramp = effects.Effect(host, system, 'http://eq10q.sourceforge.net/eq/eq4qm')
cab = effects.Effect(host, system, 'http://lsp-plug.in/plugins/lv2/impulse_responses_stereo')
reverb = effects.Effect(host, system, 'urn:dragonfly:room')

drumReverb = effects.Effect(host, system, 'urn:dragonfly:room')
looper = effects.JackEffect(system, "sooperlooper", "a2j", midi_port_pattern="sooperlooper")

hydrogen = effects.JackEffect(system, "Hydrogen", "Hydrogen-midi")
bassMachine = effects.Effect(host, system, 'http://kxstudio.linuxaudio.org/plugins/FluidPlug_FluidBass')

amp.patch('model', '/home/jon/Amps/REVV 02.nam')
# amp.preset('GSP2101 Saturated')
cab.preset('V30 Stereo')
reverb.preset('VocalHall')
drumReverb.preset('VocalHall')
poweramp.preset('Poweramp')
poweramp.toggle()

system.connect_all(system, amp, mono_left=False)
system.connect_all(amp, poweramp)
system.connect_all(poweramp, cab)
system.connect_all(cab, reverb)
# system.connect_all(cab, looper)

# system.connect_all(looper, reverb)
system.connect_all(hydrogen, drumReverb)
system.connect_all(bassMachine, reverb)
system.connect_all(reverb, system)

# Connect the looper between reverb and system and only use the common audio ports
system.connect_all(reverb, looper, audio_input_pattern="common")
system.connect_all(looper, system, audio_output_pattern="common")

system.connect_all(drumReverb, system)
# Connect the Midi Mapper to the the system foot controller
system.connect_all(system, midimapper, include_midi=True, midi_output_pattern="foot_controller")

system.connect_all(midimapper, hydrogen, include_midi=True)
system.connect_all(midimapper, bassMachine, include_midi=True)
system.connect_all(midimapper, looper, include_midi=True)

import drums
import bass
import loopor

drums.register(midimapper)
bass.register(midimapper)
loopor.register(midimapper)

midimapper.set_mode('drums')
midimapper.set_mode('bass')
bassMachine.param('level', 2)
midimapper.set_mode('loopor')


# looper.preset('Basic')
# drumRhythm.preset('Rock1')

# controller.map_action(Message(type='note_on', channel=1, control=1), lambda m: poweramp.toggle())
# controller.map_action(Message(type='note_on', channel=1, control=2), lambda m: amp.toggle())
# controller.map_action(Message(type='note_on', channel=1, control=3), lambda m: cab.toggle())
# controller.map_action(Message(type='note_on', channel=1, control=4), lambda m: reverb.toggle())
# controller.map_action(Message(type='note_on', channel=1, control=6), lambda m: looper.toggle_loop(1))
# controller.map_action(Message(type='note_on', channel=1, control=7), lambda m: looper.toggle_loop(2))

