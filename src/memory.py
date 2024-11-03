
class Memory:
    def __init__(self, size=1024):
        self.memory = [0] * size  # Simula a memória principal

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value

    def __str__(self):
        return f"Memory: {self.memory[:10]} ..."  
