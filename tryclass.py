class animal(object):

    dic = {
            "oil" : 4,
            "gas" : 67,
            "water" : 0,
          }




apple = animal()

print(apple.dic['oil'])


class dog(animal):

    def bark(self):
        print("FUCK you ")

gabe = dog()
print(gabe.dic["gas"])
