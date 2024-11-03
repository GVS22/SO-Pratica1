
class Pipeline:
    def __init__(self):
        self.stages = ["IF", "ID", "EX", "MEM", "WB"]
        self.instruction_queue = []

    def add_instruction(self, instruction):
        self.instruction_queue.append(instruction)

    def process_pipeline(self, cpu, memory):
        if not self.instruction_queue:
            print("Pipeline is empty.")
            return

        for stage in self.stages:
            if not self.instruction_queue:
                print(f"No instruction to process at stage {stage}.")
                break  # Sai do loop se não houver instruções para processar
            
            instruction = self.instruction_queue[0]  # FIFO
            print(f"{stage}: Processing {instruction}")
            if stage == "MEM":
                cpu.execute_instruction(instruction)
            
            # Remove a instrução do pipeline ao final do estágio WB
            if stage == "WB":
                self.instruction_queue.pop(0)
