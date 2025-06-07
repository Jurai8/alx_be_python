from datetime import datetime, timedelta

def main():

    def options():
        print("Choose an option")
        print("1. Current date and time")
        print("2. Future date")
        print("3. End")

    while True:
        options()

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print(f"Current date and time: {datetime.now()} ")
            case "2":
                number_of_days = int(input("Enter the number of days to add to the current date: "))

                future = timedelta(days=+number_of_days) + datetime.now()

                print(future.strftime("%Y-%m-%d"))
            case "3":
                return
            case _:
                print("Invalid option")



if __name__ == "__main__":
    main()