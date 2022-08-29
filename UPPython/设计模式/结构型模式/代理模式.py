from abc import ABCMeta,abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self,content):
        pass

class RealSubject(Subject):
    def __init__(self,filename):
        self.filename = filename
        f = open(filename,'r',encoding='utf-8')
        print('读取文件内容')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self,content):
        f = open(self.filename,'w',encoding='utf-8')
        f.write(content)
        f.close()

# subj = RealSubject('test.txt')


class VirtualProxy(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None



    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()
    def set_content(self,content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class protectProxy(Subject):
    def __init__(self,filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self,content):

        return '没有权限'

# subj = RealSubject('test.txt')
subj = VirtualProxy('test.txt')
print(subj.get_content())