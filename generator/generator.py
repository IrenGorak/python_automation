import random

from data.data import Person
from faker import Faker

faker_eng = Faker(locale="en_US")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_eng.first_name() + " " + faker_eng.last_name(),
        first_name=faker_eng.first_name(),
        last_name=faker_eng.first_name(),
        age=random.randint(18, 80),
        department=faker_eng.job(),
        salary=random.randint(1500, 3000),
        email=faker_eng.email(),
        current_address=faker_eng.street_address(),
        permanent_address=faker_eng.street_name(),
        phone=faker_eng.phone_number(),
    )


def generated_file():
    path = f'/Users/ira/python_automation/filetest{random.randint(0, 99)}.txt'
    file = open(path, 'w+')
    file.write(f"Hello {random.randint(0, 100)}")
    file.close()
    return file.name, path
