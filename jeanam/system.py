import jack

class System:
    def __init__(self):
        self.client = jack.Client(name='Jack client', no_start_server=True)
        self.set_xrun_callback(System.print_xrun)
        self.client.activate()

        self.audio_inputs = self.get_audio_inputs()
        self.audio_outputs = self.get_audio_outputs()
        
    def connect(self, src, dst):
        self.client.connect(src, dst)
    def print_xrun(msg):
        # print(f"XRun: {msg}")
        pass
    def get_audio_inputs(self):
        return self.client.get_ports(is_audio=True, is_physical=True, is_input=True, is_output=False)
    def get_audio_outputs(self):
        return self.client.get_ports(is_audio=True, is_physical=True, is_input=False, is_output=True)    
    def cpu_load(self):
        return self.client.cpu_load()
    def set_xrun_callback(self, callback):
        return self.client.set_xrun_callback(callback)
