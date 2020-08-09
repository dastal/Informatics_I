#task 3a)
class Module(object):
    dates = []
    elements = []

    def __init__(self,ects,title,semester,grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade

    def get_important_dates_overview(self):
        for date in Module.dates:
            print(date)

    def set_grade(self, new_grade):
        self.grade = new_grade

    def add_module_element(self, class_name, date):
        new_object = class_name(self)
        new_object.add_important_date(new_object, date)
        Module.elements.append(new_object)


#task 3b)
class ModuleElement():
    def __init__(self, module):
        self.module = module

    def add_important_date(self, class_name, date):
        Module.dates.append((class_name, date))

#task 3c)
class Lesson(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def __repr__(self):
        return "Lesson"

#task 3d)
class Lab(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def __repr__(self):
        return "Lab"

#task 3e)
class Midterm(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def __repr__(self):
        return "Midterm"

#task 3f)
class FinalExam(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def __repr__(self):
        return "Final Exam"


info1 = Module(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()