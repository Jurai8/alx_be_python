def perform_operation(num1, num2, operation):
    answer = 0
    # match case for each operation
    match operation:
        case "add":
            answer = num1 + num2
            return answer
        case "subtract":
            answer = num1 - num2
            return answer
        case "multiply":
            answer = num1 * num2
            return answer
        case "divide":
            if num1 == 0 or num2 == 0:
                return "can't divide by zero" 
            elif num1 != 0 and num2 != 0:
                return num1 / num2
        case _:
            return "No operation"

