
import os

def load_registers(file_path):
    registers = {}
    with open(file_path, "r") as file:
        for line in file:
            reg, value = map(int, line.strip().split(","))
            registers[reg] = value
    return registers

def load_instructions(file_path):
    instructions = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            instructions.append(parts)
    return instructions
