
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Add a new item: ")

            shopping_list.append(new_item)

        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input("Remove an new item: ")

            # check if the item is in the list
            if removed_item not in shopping_list:
                print("This item does not exist")
            else:
                for item in shopping_list:
                    if item == removed_item:
                        shopping_list.remove(item)

        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)

        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
