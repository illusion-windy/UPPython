from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day < 10:
            print('总经理准假%d天' % day)
        else:
            print('辞职')


class DepartmentManage(Handler):
    def __init__(self):
        self.next = GeneralManager()
    def handle_leave(self, day):
        if day<=5:
            print('DepartmentManage准'+str(day))
        else:
            print('DepartmentManage权限不足'+str(day))
            self.next.handle_leave(day)



class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManage()

    def handle_leave(self, day):
        if day<=1:
            print('ProjectDirector准'+str(day))
        else:
            print('ProjectDirector权限不足'+str(day))
            self.next.handle_leave(day)





