class Home:
    def room(self):
        width=100
        highet=100
        print("area of room is",width*highet)
    def kitchen(self):
        width=150
        highet=200
        print("area of kitchen is",width*highet)
class Firsthome(Home):
    def studyroom(self):
        width=100
        highet=160
        print("area of study room",width*highet)
class Secondhome(Home):
    def workarea(self):
        width=200
        highet=300
        print("area of work area",width*highet)

f=Firsthome()
s=Secondhome()
f.room()
f.kitchen()
f.studyroom()
s.room()
s.kitchen()
s.workarea()