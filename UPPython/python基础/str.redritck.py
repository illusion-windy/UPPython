class Father():
    pass


class Mother():
    pass


class Children(Father, Mother):
    eye = "bule"
    weight = "100"

    def eat(self):
        print("eat ")

    def drink(self):
        print("drink...")

    def __serect(self):
        print("__serect")

c_obj = Children()


res = getattr(c_obj,"weight")

setattr(c_obj,"weight",50)

res = getattr(c_obj,"weight")
print(res)

c2_obj = Children()
print(c_obj.weight)
print(c2_obj.weight)
