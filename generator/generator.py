from data.data import Person
from faker import Faker

faker_eng = Faker(locale="en_US")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_eng.first_name() + " " + faker_eng.last_name(),
        email=faker_eng.email(),
        current_address=faker_eng.street_address(),
        permanent_address=faker_eng.street_name(),
    )

