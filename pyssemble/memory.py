class Memory:
    def __init__(self, memory_size=100):
        self.memory = {}
        self.size = 0
    def __getitem__(self, address):
        return self.memory[address]
    def __setitem__(self, address, value):
        self.memory[address] = value