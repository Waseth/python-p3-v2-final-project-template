import sqlite3

DATABASE_FILE = 'petpal.db'

def create_tables():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Adopters (
            AdopterID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            ContactDetails TEXT NOT NULL,
            AdoptionDate DATE NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pets (
            PetID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Breed TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Description TEXT NOT NULL,
            AdoptionStatus TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PetAdoptions (
            AdoptionID INTEGER PRIMARY KEY AUTOINCREMENT,
            PetID INTEGER NOT NULL,
            AdopterID INTEGER NOT NULL,
            AdoptionDate DATE NOT NULL,
            FOREIGN KEY (PetID) REFERENCES Pets (PetID),
            FOREIGN KEY (AdopterID) REFERENCES Adopters (AdopterID)
        )
        """)
        conn.commit()

def add_pet(name, breed, age, description):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pets (Name, Breed, Age, Description, AdoptionStatus) VALUES (?, ?, ?, ?, 'available')",
                       (name, breed, age, description))
        conn.commit()

def add_adopter(name, contact_details, adoption_date):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Adopters (Name, ContactDetails, AdoptionDate) VALUES (?, ?, ?)",
                       (name, contact_details, adoption_date))
        conn.commit()

def add_pet_adoption(pet_id, adopter_id, adoption_date):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PetAdoptions (PetID, AdopterID, AdoptionDate) VALUES (?, ?, ?)",
                       (pet_id, adopter_id, adoption_date))
        conn.commit()

def get_all_pets():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pets")
        pets = cursor.fetchall()
        return pets

def get_all_adopters():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Adopters")
        adopters = cursor.fetchall()
        return adopters

def update_pet(pet_id, **kwargs):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        set_clause = ', '.join(f"{key} = ?" for key in kwargs if kwargs[key] is not None)
        parameters = tuple(value for value in kwargs.values() if value is not None) + (pet_id,)
        cursor.execute(f"UPDATE Pets SET {set_clause} WHERE PetID = ?", parameters)
        conn.commit()

def update_adopter(adopter_id, **kwargs):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        kwargs = {('ContactDetails' if key == 'contact_details' else 'AdoptionDate' if key == 'adoption_date' else key): value for key, value in kwargs.items()}
        set_clause = ', '.join(f"{key} = ?" for key in kwargs if kwargs[key] is not None)
        parameters = tuple(value for value in kwargs.values() if value is not None) + (adopter_id,)
        cursor.execute(f"UPDATE Adopters SET {set_clause} WHERE AdopterID = ?", parameters)
        conn.commit()

def delete_pet(pet_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pets WHERE PetID = ?", (pet_id,))
        conn.commit()

def delete_adopter(adopter_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Adopters WHERE AdopterID = ?", (adopter_id,))
        conn.commit()

def get_pet_by_id(pet_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pets WHERE PetID = ?", (pet_id,))
        pet = cursor.fetchone()
        return pet

def get_adopter_by_id(adopter_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Adopters WHERE AdopterID = ?", (adopter_id,))
        adopter = cursor.fetchone()
        return adopter

def update_adoption_status(pet_id, new_status):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Pets SET AdoptionStatus = ? WHERE PetID = ?", (new_status, pet_id))
        conn.commit()

