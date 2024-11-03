# main.py
from src.simulador import Simulator

if __name__ == "__main__":
    reg_file = "data/setRegisters.txt"
    instr_file = "data/Instructions.txt"

    simulator = Simulator(reg_file, instr_file)
    simulator.run()
