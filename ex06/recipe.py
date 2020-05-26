cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
        },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60"
    },
    "salad": {
        "ingredients": ["avocado", "aragula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15"
    }
}


def print_recipe(recipe_name):
    print("Recipe of ", recipe_name)
    print("Ingrédients:")
    for ing in cookbook[recipe_name]["ingredients"]:
        print(ing)
    print("\nWhen ?", cookbook[recipe_name]["meal"])
    print("\ntime :", cookbook[recipe_name]["prep_time"])


def add_recipe(name, meal, prep, ingredients):
    cookbook[name] = \
        {"ingredients": ingredients, "meal": meal, "prep_time": prep}


def choice_menu():
    print("1 Add recipe\n2 Delete Recipe\n\
3 Print Recipe\n4 Print cookbook\n5 Quit")
    hub(input())


def hub(choice):
    if (choice == "1"):
        name = input("\nName of recipe ? ")
        meal = input("\nmeal type ? ")
        prep = input("\nprep_time ? ")
        ingredients = input("\nIngredients ? ").split()
        add_recipe(name, meal, prep, ingredients)
        choice_menu()
    if choice == "3":
        arg = input("Recipe ?")
        if arg in cookbook:
            print_recipe(arg)
            choice_menu()
        else:
            print("this recipe doesn't exist")
            choice_menu()
    if choice == "2":
        arg = input("Recipe to erase?")
        if arg in cookbook:
            del cookbook[arg]
            print(arg, "Erased\n")
            choice_menu()
        else:
            print("this recipe doesn't exist")
            choice_menu()
    if choice == "4":
        for name in cookbook:
            print_recipe(name)
        choice_menu()
    elif choice == "5":
        print("Cookbook closed")
        exit(0)
    else:
        choice_menu()


choice_menu()
