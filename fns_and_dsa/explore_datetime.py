from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')} ")

    return

def calculate_future_date(number_of_days):
    future_date = timedelta(days=+number_of_days) + datetime.now()

    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

    return

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
                display_current_datetime()
            case "2":
                number_of_days = int(input("Enter the number of days to add to the current date: "))

                calculate_future_date(number_of_days)          
            case "3":
                return
            case _:
                print("Invalid option")



if __name__ == "__main__":
    main()