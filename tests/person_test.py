import pytest


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_human = True

    def introduce_self(self):
        return f'Hi! My name is {self.first_name} {self.last_name}'

    def give_high_five(self, other):
        return f'{self.first_name} gives {other.first_name} a high five!'


@pytest.mark.person
class TestPersonClass:
    @pytest.fixture
    def person(self):
        return Person('Marc', 'Clinedinst', 32)

    def test_person_object_has_correct_first_name(self, person):
        assert person.first_name == 'Marc'

    def test_person_object_has_correct_last_name(self, person):
        assert person.last_name == 'Clinedinst'

    def test_person_object_has_correct_age(self, person):
        assert person.age == 32

    def test_person_object_is_human(self, person):
        assert person.is_human

    def test_person_can_introduce_self(self):
        person = Person('Marc', 'Clinedinst', 32)

        assert person.introduce_self() == 'Hi! My name is Marc Clinedinst'

    def test_person_can_give_another_person_a_high_five(self, person):
        other_person = Person('Tem', 'Assefa', 26)

        assert person.give_high_five(other_person) == 'Marc gives Tem a high five!'
