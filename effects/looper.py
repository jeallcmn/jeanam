from effects import Effect

class Looper(Effect):
    activeLoops = [False, False, False, False, False, False]
    def __init__(self, host, system, uri):
        super().__init__(host,system, uri)

    def toggle_loop(self, i):
        print(f"Loop{i}:dd")
        self.activeLoops[i] = not self.activeLoops[i]
        x = 1 if self.activeLoops[i] else 0
        self.param(f'loop{i}', x)
        print(f"Loop{i}:{x}")
