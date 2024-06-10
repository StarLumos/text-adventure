from time import time as timestamp

class Time:
    genesis: float
    present: float
    elapsed: float
    last: float
    delta: float
    
    def __init__(self):
        self.genesis = timestamp()
        self.present = self.genesis
        self.elapsed = 0
        self.last = self.present
        self.delta = 0

    def tick(self):
        self.last = self.present
        self.present = timestamp()
        self.elapsed = self.present - self.genesis
        self.delta = self.present - self.last
