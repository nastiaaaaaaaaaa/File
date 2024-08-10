import time

class Pupil:          # обєкт людина з полями      
    def __init__(self, surname, name, mark):
        self.Surname = surname
        self.Name = name
        self.Mark = mark

pupils = []

def print_class(pupils): # виводить всіх зі списку
    for pupil in pupils:
        print(pupil.Surname,pupil.Name, " - ",pupil.Mark)
    print("\n")

with open("pupils.txt", "r", encoding="UTF-8") as file:
    for line in file:
        data = line.split(" ")# розділяєм пробілом
        pupil = Pupil(data[0], data[1], int(data[2]))
        pupils.append(pupil)

print_class(pupils)