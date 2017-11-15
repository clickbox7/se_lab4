class StudentGenerator:
    NAMES=["Pero", "Djuro", "Marko", "Miki", "Ana", "Ivana"]
    LNAMES=["Peric", "Duric", "Markic", "Mikic", "Anic", "Ivic"]
    def __init__(self):
        pass
    def get_n(self, n):
        """returns n students in list"""
        students = []
        for i in range(n):
            name = random.choice(self.NAMES)
            lname = random.choice(self.LNAMES)
            number = random.randint(1000,10000)
            students.append(Student(name, lname, number))
        return students 


        
        

        
    
generator = StudentGenerator() 
students = generator.get_n(10)
for student in students:
    print student

pi = Course("Programsko inzenjerstvo", "SARS503")
pi2017 = pi.add_running(2017)
pi2016 = pi.add_running(2016)
mat = Course("Matematika 1", "SER101")
mat.add_running(2017)
mat.add_running(2016)

for student in students:
    student.enrol(pi2017)
    student.enrol(pi2016)
print pi2017
print pi2016
