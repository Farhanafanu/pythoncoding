class Myclass:
    def example(self, *args):
        if len(args) == 0:
            print("no argument")
        elif len(args) == 1:
            print(args[0])
        elif len(args) == 2:
            print(args[0] + args[1])

m = Myclass()
m.example()
m.example(10)
m.example(2, 3)
