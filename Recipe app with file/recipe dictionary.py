#this is the requirement for the Recipe App
#Recipe App :
#Write a python Application for the Recipe Management Where User can Add, Update, Delete and View their recipes.
#Prompt User for the choices
#1: Add Recipe
#2: Update Recipe
#3: Delete Recipe
#4: View Recipes
#5: Exit
#Recipe Structure:  {id, name, type, description}  using dictionary to store the recipes.


class RecipeApp:
    def __init__(self):
        # Initialized once per object
        self.dict_recipes = {}


    def validate_new_id(self, recipe_id):
        if not recipe_id.isdigit():
            return False, None

        recipe_id = int(recipe_id)

        if recipe_id not in self.dict_recipes:
            return True, None

        used_ids = set(self.dict_recipes.keys())
        suggested_id = 1

        while suggested_id in used_ids:
            suggested_id += 1

        return False, suggested_id

    def validate_existing_id(self, recipe_id):
        if not recipe_id.isdigit():
            return False
        return int(recipe_id) in self.dict_recipes



    def add_recipe(self):
        while True:
            recipe_id = input("Enter Recipe ID: ")
            valid, suggestion = self.validate_new_id(recipe_id)

            if valid:
                recipe_id = int(recipe_id)
                break

            if suggestion:
                print(f"Recipe ID already exists. {suggestion} is available.")
            else:
                print("Recipe ID must be an integer.")

        name = input("Enter Recipe Name: ")
        r_type = input("Enter Recipe Type: ")
        description = input("Enter Recipe Description: ")

        self.dict_recipes[recipe_id] = {
            "name": name,
            "type": r_type,
            "description": description
        }

        print("Recipe added successfully!\n")

    def update_recipe(self):
        if not self.dict_recipes:
            print("No recipes available to update.\n")
            return

        while True:
            recipe_id = input("Enter Recipe ID to update: ")

            if self.validate_existing_id(recipe_id):
                recipe_id = int(recipe_id)
                break

            print("Recipe ID not found. Available IDs:",
                  sorted(self.dict_recipes.keys()))

        name = input("Enter new Recipe Name: ")
        r_type = input("Enter new Recipe Type: ")
        description = input("Enter new Recipe Description: ")

        self.dict_recipes[recipe_id] = {
            "name": name,
            "type": r_type,
            "description": description
        }

        print("Recipe updated successfully!\n")

    def delete_recipe(self):
        if not self.dict_recipes:
            print("No recipes available to delete.\n")
            return

        while True:
            recipe_id = input("Enter Recipe ID to delete: ")

            if self.validate_existing_id(recipe_id):
                recipe_id = int(recipe_id)
                break

            print("Recipe ID not found. Available IDs:")

        del self.dict_recipes[recipe_id]
        print("Recipe deleted successfully!\n")

    def view_recipes(self):
        if not self.dict_recipes:
            print("No recipes found.\n")
            return

        print("\n--- Recipes ---\n")
        for recipe_id, details in self.dict_recipes.items():
            print(f"Recipe ID: {recipe_id}")
            print(f"Name: {details['name']}")
            print(f"Type: {details['type']}")
            print(f"Description: {details['description']}\n")



    def main_menu(self):
        while True:
            print("Recipe Management Application")
            print("1. Add Recipe")
            print("2. Update Recipe")
            print("3. Delete Recipe")
            print("4. View Recipes")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_recipe()
            elif choice == "2":
                self.update_recipe()
            elif choice == "3":
                self.delete_recipe()
            elif choice == "4":
                self.view_recipes()
            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.\n")


# ---------- MAIN FUNCTION ----------

def main():
    app = RecipeApp()   # OBJECT CREATED HERE
    app.main_menu()     # METHOD CALL


# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    main()
