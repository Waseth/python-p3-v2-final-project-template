import sys
from lib.database import (
    create_tables, add_adopter, add_pet, add_pet_adoption, get_all_pets,
    get_all_adopters, update_pet, delete_pet, update_adopter, delete_adopter,
    get_pet_by_id, get_adopter_by_id, update_adoption_status
)

def main():
    create_tables()

    while True:
        print("Welcome to PetPal!")
        print("1. Add Pet")
        print("2. Update Pet Details")
        print("3. Manage Adoption Status")
        print("4. Add Adopter")
        print("5. View Pet Profiles")
        print("6. View Adopter Profiles")
        print("7. Update Adopter Profile")
        print("8. Delete Pet Profile")
        print("9. Delete Adopter Profile")
        print("10. Search Pet by ID")
        print("11. Search Adopter by ID")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter pet's name: ")
            breed = input("Enter pet's breed: ")
            age = input("Enter pet's age: ")
            description = input("Enter pet's description: ")
            add_pet(name, breed, age, description)
            print("Pet added successfully!")
        elif choice == '2':
            pet_id = input("Enter pet's ID to update: ")
            name = input("Enter pet's name (press enter to keep current): ")
            breed = input("Enter pet's breed (press enter to keep current): ")
            age = input("Enter pet's age (press enter to keep current): ")
            description = input("Enter pet's description (press enter to keep current): ")
            update_pet(pet_id, name=name or None, breed=breed or None, age=age or None, description=description or None)
            print("Pet details updated successfully!")
        elif choice == '3':
            pet_id = input("Enter pet's ID to update adoption status: ")
            new_status = input("Enter new adoption status (available, pending, adopted): ")
            update_adoption_status(pet_id, new_status)
            print("Adoption status updated successfully!")
        elif choice == '4':
            name = input("Enter adopter's name: ")
            contact_details = input("Enter adopter's contact details: ")
            adoption_date = input("Enter adoption date (YYYY-MM-DD): ")
            add_adopter(name, contact_details, adoption_date)
            print("Adopter added successfully!")
        elif choice == '5':
            pets = get_all_pets()
            for pet in pets:
                print(pet)
        elif choice == '6':
            adopters = get_all_adopters()
            for adopter in adopters:
                print(adopter)
        elif choice == '7':
            adopter_id = input("Enter adopter's ID to update: ")
            name = input("Enter adopter's name (press enter to keep current): ")
            contact_details = input("Enter adopter's contact details (press enter to keep current): ")
            adoption_date = input("Enter adoption date (press enter to keep current): ")
            update_adopter(adopter_id, name=name or None, contact_details=contact_details or None, adoption_date=adoption_date or None)
            print("Adopter profile updated successfully!")
        elif choice == '8':
            pet_id = input("Enter pet's ID to delete: ")
            delete_pet(pet_id)
            print("Pet profile deleted successfully!")
        elif choice == '9':
            adopter_id = input("Enter adopter's ID to delete: ")
            delete_adopter(adopter_id)
            print("Adopter profile deleted successfully!")
        elif choice == '10':
            pet_id = input("Enter pet's ID to search: ")
            pet = get_pet_by_id(pet_id)
            if pet:
                print(pet)
            else:
                print("Pet not found.")
        elif choice == '11':
            adopter_id = input("Enter adopter's ID to search: ")
            adopter = get_adopter_by_id(adopter_id)
            if adopter:
                print(adopter)
            else:
                print("Adopter not found.")
        elif choice == '12':
            print("Exiting PetPal. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

