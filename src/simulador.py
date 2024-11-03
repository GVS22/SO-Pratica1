
from .cpu import CPU
from .memory import Memory
from .pipeline import Pipeline
from .utils import load_registers, load_instructions

class Simulator:
    def __init__(self, reg_file, instr_file):
        self.cpu = CPU()
        self.memory = Memory()
        self.pipeline = Pipeline()

        
        initial_registers = load_registers(reg_file)
        self.cpu.registers.update(initial_registers)

        
        self.instructions = load_instructions(instr_file)

    def run(self):
        for instruction in self.instructions:
            self.pipeline.add_instruction(instruction)
            self.pipeline.process_pipeline(self.cpu, self.memory)
            print(self.cpu)
            print(self.memory)
