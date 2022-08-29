from abc import abstractmethod, ABCMeta


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        pass


class BigShell(PhoneShell):
    def show_shell(self):
        pass


class AppleShell(PhoneShell):
    def show_shell(self):
        pass


class SnapDragonCPU(CPU):
    def show_cpu(self):
        pass


class MediaTekCPU(CPU):
    def show_cpu(self):
        pass


class AppleCPU(CPU):
    def show_cpu(self):
        pass


class Android(OS):
    def show_os(self):
        pass


class IOS(OS):
    def show_os(self):
        pass


class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()

# class Phone:
#     def __init__(self,cpu,os,shell):
#         self.cpu = cpu
#         self.os = os
#         self.shell = shell
#     def show_info(self):
#         print('shoujixinxi')
#         self.cpu.show_cpu()
#         self.os.show_os()
#         self.shell.show_shell()
#
# def make_phone(factory):
#     cpu = factory.make_cpu()
#     os = factory.make_os()
#     shell = factory.make_shell()
#     return Phone(cpu,os,shell)

class Phone:
    def __init__(self,objs):
        self.cpu = objs.make_cpu()
        self.os = objs.make_os()
        self.shell = objs.make_shell()
    def show_info(self):
        print('shoujixinxi')
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()
#

p1 = Phone(MiFactory())
p1.show_info()


