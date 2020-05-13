class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id}, {self.name}'


class PersonFactory:
    id = 0


    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


team_member_1 = PersonFactory().create_person(name='long')
print(team_member_1)

