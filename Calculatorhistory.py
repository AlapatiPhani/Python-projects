#file handling or file operations
#to show the history of calculations
HISTORY_FILE="history.txt"

def show_history():
    file=open(HISTORY_FILE, "r")
    lines=file.readlines()
    if len(lines)==0:
        print("No history found.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

#clear history
def clear_history():
    file=open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")
#save to history
def save_to_history(equation, result):
    file=open(HISTORY_FILE, "a")
    file.write(f"{equation} = {result}\n")
    file.close()
#perform calculations
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid input format. Please use: number operator number")
        return
    num1 = float(parts[0])
    op =parts[1]
    num2 = float(parts[2])
    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if num2==0:
            print("Error: Division by zero.")
            return
        result=num1/num2
    else:
        print("Unsupported operator. Please use +, -, *, or /.")
        return
    print(f"Result: {result}")
    save_to_history(user_input, result)

#main function for user interaction and loop
def main():
    print('--- Simple Calculator (type history,clear,exit) ---')
    while True:
        user_input=input("Enter calculation: ")
        if user_input.lower()=='exit':
            print("Exiting calculator.")
            break
        elif user_input.lower()=='history':
            show_history()
        elif user_input.lower()=='clear':
            clear_history()
        else:
            calculate(user_input)
main()
#simple calculator with addition, subtraction, multiplication, and division
