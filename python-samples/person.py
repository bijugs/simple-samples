class Person(object):

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return self.name

class Student(Person):

  def __init__(self, name, age, school):
    super().__init__(name, age)
    self.school = school

  def __str__(self):
    return super().__str__() + " " + self.school

if __name__ == "__main__":
  p = Person("Abhi", 10)
  print(p)
  s = Student("Ashi", 10, "Donolan")
  print(s)
