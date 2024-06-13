class Pet:
    def __init__(self, pet_id, name, breed, age, description, adoption_status):
        self.pet_id = pet_id
        self.name = name
        self.breed = breed
        self.age = age
        self.description = description
        self.adoption_status = adoption_status

    def update_details(self, name=None, breed=None, age=None, description=None, adoption_status=None):
        if name:
            self.name = name
        if breed:
            self.breed = breed
        if age:
            self.age = age
        if description:
            self.description = description
        if adoption_status:
            self.adoption_status = adoption_status

class Adopter:
    def __init__(self, adopter_id, name, contact_details, adoption_date):
        self.adopter_id = adopter_id
        self.name = name
        self.contact_details = contact_details
        self.adoption_date = adoption_date

