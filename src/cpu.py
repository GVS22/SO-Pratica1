
class CPU:
    def __init__(self):
        self.registers = {i: 0 for i in range(32)}  # 32 registradores
        self.pc = 0  # Program Counter

    def execute_instruction(self, instruction):
        op, dest, reg1, reg2 = instruction
        dest, reg1, reg2 = int(dest), int(reg1), int(reg2)

        if op == "ADD":
            self.registers[dest] = self.registers[reg1] + self.registers[reg2]
        elif op == "SUB":
            self.registers[dest] = self.registers[reg1] - self.registers[reg2]
        elif op == "MULT":
            self.registers[dest] = self.registers[reg1] * self.registers[reg2]
        elif op == "DIV":
            self.registers[dest] = self.registers[reg1] // self.registers[reg2] if self.registers[reg2] != 0 else 0
        elif op == "LOAD":
            self.registers[dest] = self.registers[reg1]
        elif op == "STORE":
            self.registers[reg1] = self.registers[dest]
        elif op == "BEQ":
            if self.registers[reg1] == self.registers[reg2]:
                self.pc = dest
                return  # Jump, no increment
        elif op == "JUMP":
            self.pc = dest
            return
        else:
            print(f"Unknown operation: {op}")

        self.pc += 1  # Incrementa PC se não houver salto

    def __str__(self):
        return f"PC: {self.pc}, Registers: {self.registers}"
