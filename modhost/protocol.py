class ProtocolParser:
    def add(self, uri, id):
        return f"add {uri} {id}"
    def remove(self, id):
        return f"remove {id}"
    def connect(self, src, dst):
        return f"connect {src} {dst}"
    def disconnect(self, src, dst):
        return f"disconnnect {src} {dst}"
    def set_bpm(self, num):
        return f"set_bpm {num}"
    def set_bpb(self, num):
        return f"set_bpb {num}"        
    def transport(self, rolling, bpb, bpm):
        return 'transport {} {} {}'.format(rolling, bpb, bpm)
    def transport_sync(self, mode):
        return 'transport_sync {}'.format(mode)
    def preset_load(self, id, uri):
        return 'preset_load {} {}'.format(id, uri);
    def preset_save(self, id, name, dir, uri):
        return 'preset_save {} {} {} {}'.format(id, name, dir, uri)
    def preset_show(self, id, uri):
        return 'preset_show {} {}'.format(id, uri)
    def param_set(self, id, symbol, value):
        return 'param_set {} {} {}'.format(id, symbol, value)
    def param_get(self, id, symbol):
        return 'param_get {} {}'.format(id, symbol)
    def param_monitor():
        pass
    def patch_set(self, id, uri, value):
        return 'patch_set {} {} "{}"'.format(id, uri, value)  
    def monitor():
        pass
    def midi_learn(self, plugin, param):
        pass
    def midi_map(self,plugin, param, midi_chanel, midi_cc):
        pass
    def midi_unmap(self,plugin, param):
        pass
    def bypass(self, id, active):
        return 'bypass {} {}'.format( id,
            1 if active else 0
        )
    def load(self, filename):
        return 'load {}'.format(filename)
    def save(self, filename):
        return 'save {}'.format(filename)
    def help(self):
        return 'help'
    def quit(self):
        return 'quit'

