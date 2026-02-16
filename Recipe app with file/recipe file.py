
import os

RECIPE_FILE = "recipes.txt"

def add_recipe():
    # Add a new recipe to the file
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma separated): ")
    steps = input("Enter preparation steps: ")

    with open(RECIPE_FILE, "a") as file:
        file.write(f"Recipe Name: {name}\n")
        file.write(f"Ingredients: {ingredients}\n")
        file.write(f"Steps: {steps}\n")
        file.write("-" * 40 + "\n")

    print("Recipe added successfully!\n")


def view_recipes():

    # Display all recipes from the file
    if not os.path.exists(RECIPE_FILE):
        print("No recipes found. Please add some recipes first.\n")
        return

    with open(RECIPE_FILE, "r") as file:
        content = file.read()

        if content.strip() == "":
            print("No recipes found. Please add some recipes first.\n")
        else:
            print("\n--- Recipes ---\n")
            print(content)

def search_recipe():
    # Search for a recipe by name
    if not os.path.exists(RECIPE_FILE):
        print("No recipes found. Please add some recipes first.\n")
        return

    search_name = input("Enter the recipe name to search: ")
    found = False

    with open(RECIPE_FILE, "r") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].startswith("Recipe Name:"):
                if search_name.lower() in lines[i].lower():
                    print("\nRecipe found!\n")
                    print(lines[i].strip())
                    print(lines[i + 1].strip())
                    print(lines[i + 2].strip())
                    print(lines[i + 3].strip())
                    found = True
                    break

    if not found:
        print("Recipe not found.\n")



def main_menu():
    # Main menu of the application
    while True:
        print("Recipe Management Application")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    main_menu()
