from modhost.connection import Connection
from modhost.protocol import ProtocolParser
import atexit
import signal

class Host:
    def __init__(self):
        self.effects = []
        self.connection = Connection()
        self.protocol = ProtocolParser()
        
        # register shutdown hooks
        @atexit.register
        def cleanup():
            self.remove_all()
        def terminate(arg1, arg2):
            self.remove_all()
        signal.signal(signal.SIGTERM, terminate)

    def add(self, uri, id):
        self.effects.append(id)
        return self.connection.send(self.protocol.add(uri, id))
    def remove(self, id):
        return self.connection.send(self.protocol.remove(id))
    def connect(self, src, dst):
        return self.connection.send(self.protocol.connect(src, dst))
    def disconnect(self, src, dst):
        return self.connection.send(self.protocol.disconnect(src, dst))
    def set_bpm(self, num):
        return self.connection.send(self.protocol.set_bpm(num))
    def set_bpb(self, num):
        return self.connection.send(self.protocol.set_bpb(num))
    def transport(self, rolling, bpb, bpm):
        return self.connection.send(self.protocol.transport(rolling, bpb, bpm))
    def transport_sync(self, mode):
        return self.connection.send(self.protocol.transport_sync(mode))
    def preset_load(self, id, uri):
        return self.connection.send(self.protocol.preset_load(id, uri))
    def preset_save(self, id, name, dir, uri):
        return self.connection.send(self.protocol.preset_save(id, name, dir, uri))
    def preset_show(self, id, uri):
        return self.connection.send(self.protocol.preset_show(id, uri))
    def param_set(self, id, symbol, value):
        return self.connection.send(self.protocol.param_set(id, symbol, value))
    def param_get(self, id, symbol):
        return self.connection.send(self.protocol.param_get(id, symbol))
    def param_monitor(self):
        return self.connection.send(self.protocol.param_monitor(id))
    def patch_set(self, id,  uri, value):
        return self.connection.send(self.protocol.patch_set(id, uri, value))
    def monitor(self):
        return self.connection.send(self.protocol.monitor())
    def midi_learn(self, id, param):
        return self.connection.send(self.protocol.midi_learn(id, param))
    def midi_map(self,id, param, midi_channel, midi_cc):
        return self.connection.send(self.protocol.midi_map(id, param, midi_channel, midi_cc))
    def midi_unmap(self,id, param):
        return self.connection.send(self.protocol.midi_unmap(id, param))
    def bypass(self, id, active):
        return self.connection.send(self.protocol.bypass(id, active))
    def load(self, filename):
        return self.connection.send(self.protocol.load(filename))
    def save(self, filename):
        return self.connection.send(self.protocol.save(filename))
    def help(self):
        return self.connection.send(self.protocol.help())
    def quit(self):
        return self.connection.send(self.protocol.quit())
    def remove_all(self):
        for i in self.effects:
            self.remove(i)
