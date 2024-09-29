import jack
from effects.effect import Connectable

class System(Connectable):
    def __init__(self):
        self.client = jack.Client(name='Jack client', no_start_server=True)
        self.set_xrun_callback(System.print_xrun)
        self.client.activate()

        ins = self.get_audio_inputs()
        outs = self.get_audio_outputs()
        mins = self.get_midi_inputs()
        mouts = self.get_midi_outputs()

        super().__init__(ins, outs, mins, mouts)

    def connect(self, src, dst):
        try:
            print(f"Connecting: {src.name} -> {dst.name}")
            self.client.connect(src, dst)
        except jack.JackErrorCode as e:
            print(f"Connecting Error: {e}")
    def print_xrun(msg):
        # print(f"XRun: {msg}")
        pass
    def get_audio_inputs(self):
        return self.client.get_ports(name_pattern="system:.*", is_audio=True, is_physical=True, is_input=True, is_output=False)
    def get_audio_outputs(self):
        return self.client.get_ports(name_pattern="system:.*", is_audio=True, is_physical=True, is_input=False, is_output=True)    
    def get_midi_inputs(self):
        return self.client.get_ports(name_pattern="a2j:.*", is_audio=False, is_input=True, is_output=False)
    def get_midi_outputs(self):
        return self.client.get_ports(name_pattern="a2j:.*", is_audio=False, is_input=False, is_output=True)
    def cpu_load(self):
        return self.client.cpu_load()
    def set_xrun_callback(self, callback):
        return self.client.set_xrun_callback(callback)

    def __str__(self):
        return f"""System {Connectable.__str__(self)}"""
    
    def __filter_ports(self, ports, pattern):
        if pattern:
            return [x for x in ports if pattern in x.name]
        else:
            return ports
    # Tries to smartly connect
    def connect_all(self, src, dst, mono_left=True, include_midi=False, 
                    audio_input_pattern=None, 
                    audio_output_pattern=None, 
                    midi_input_pattern=None, 
                    midi_output_pattern=None, ):
        pairs = [
            (
                self.__filter_ports(src.audio_outputs, audio_output_pattern), 
                self.__filter_ports(dst.audio_inputs, audio_input_pattern)
            )
        ]
        if include_midi:
            pairs.append((
                self.__filter_ports(src.midi_outputs, midi_output_pattern),
                self.__filter_ports(dst.midi_inputs, midi_input_pattern)
            ))
            
        for outputs, inputs in pairs:
            # Ins/Outs match up
            if len(outputs) == len(inputs):
                for i in range(len(outputs)):
                    self.connect(outputs[i], inputs[i])
            elif len(outputs) == 2 and len(inputs) == 1:
                # more outputs than inputs, connect the preferred channel
                channel = 0 if (mono_left) else 1
                self.connect(outputs[channel], inputs[0])
            elif len(inputs) == 2 and len(outputs) == 1:
                # More inputs than outputs, connect single to all
                for i in range(len(inputs)):
                    self.connect(outputs[0], inputs[i])
            else:
                # 0 inputs somewhere
                pass