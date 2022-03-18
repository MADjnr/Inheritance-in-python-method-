class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"welcome to class!, I'm your teacher. My name is {self.full_name}")


class ScienceTeacher(Teacher):
    pass
'''
The lesson here is overriding, when the method below is commented out,
it is seen that the welcome_student above gets called but when it the comment is
removed, it is seen that the method below overrides the welcome_student above.
'''
'''

    def welcome_students(self):
        print(f"Science is amazing")
        print(f"Welcome to class. I'm your teacher: {self.full_name}")

'''
my_science_teacher = ScienceTeacher("EMily Smith", "S355A213")
my_science_teacher.welcome_students()



## The Backpack class

class Backpack:
    
    def __init__(self):
        self.items = []
        
    ###here i will add a method called add_snack
    def add_snack(self, snack):
        print("Adding a snack to this backpack")
        self.items.append(snack)
        print(f"{snack.capitalize()} was added to the backpack successfully")
        
        
class SchoolBackpack(Backpack):
        
        def add_snack(self, snack):
            print("It is time to go to school. Lets add a snack")
            Backpack.add_snack(self, snack)
            print("Now you backpack has these items:", self.items)

'''
my_backpack = SchoolBackpack()
for item in my_backpack.items:
    my_backpack.add_snack("efknekfn")

print(my_backpack)
    ### Ask christwin ---- how do i add multiple list at once
'''

my_backpack = SchoolBackpack()
my_backpack.add_snack("candy")




            


