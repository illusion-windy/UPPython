class CPU:
    def run(self):
        print('kaishi   cpu  yunxing')
    def stop(self):
        print('tingzhi  cpu  yunxing ')
class Disk:
    def run(self):
        print('kaishi   Disk  yunxing')

    def stop(self):
        print('tingzhi  Disk  yunxing ')

class Memory:
    def run(self):
        print('kaishi   Memory  yunxing')

    def stop(self):
        print('tingzhi  Memory  yunxing ')

# 外观
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

computer = Computer()
computer.run()








