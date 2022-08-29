from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s , %s , %s, %s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class GirBulider(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'build_face'

    def build_body(self):
        self.player.body = 'build_body'

    def build_arm(self):
        self.player.arm = 'build_arm'

    def build_leg(self):
        self.player.leg = 'build_leg'


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'build_Monster_face'

    def build_body(self):
        self.player.face = 'build_Monster_body'

    def build_arm(self):
        self.player.face = 'build_Monster_arm'

    def build_leg(self):
        self.player.face = 'build_Monster_leg'


class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


bulider = GirBulider()
director = PlayerDirector()
p = director.build_player(bulider)

print(p)
