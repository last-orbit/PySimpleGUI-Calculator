import PySimpleGUI as sg

# sg.Window(title="Calculator", layout=[[]], margins=(200, 100)).read()

# Has Number
column_layout1 = [
    [sg.Text("Let's choose 1st number:")],
    [sg.Input(key="-NUM1-")],
    [sg.Text("Let's choose 2nd number:")],
    [sg.Input(key="-NUM2-")],
]
# Has Operations
column_layout2 = [
    [
        sg.Button("+"),
        sg.Button("-"),
        sg.Button("*")
    ],
    [
        sg.Button("/"),
        sg.Button("%"),
        sg.Button("x\u00b2"),
    ],
    [
        sg.Text("Result:"),
        sg.Text(key="-RESULT-")
    ]
]

layout = [
    [
        sg.Column(column_layout1, element_justification="left"),
        sg.Column(column_layout2, element_justification="right"),
    ]
]
# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    num1 = int(values["-NUM1-"])
    num2 = int(values["-NUM2-"])

    if event == "+":
        result = num1 + num2
    elif event == "-":
        result = num1 - num2
    elif event == "*":
        result = num1 * num2
    elif event == "/":
        result = num1 / num2
    elif event == "%":
        result = num1 // num2
    elif event == "x\u00b2":
        result = num1**num2

    window["-RESULT-"].update(result)

window.close()

## This works as the terminal calculator, but not for the GUI calculator.
# print("Welcome to the calculator program!")

# num1 = int(input("Select first number:"))
# num2 = int(input("Select another number:"))

# if not int(num1 or num2):
#     print("A number needs to be selected.")

# choice = input("Please Select an operation: (add, subtract, multiply, divide, remainder, squared): ")
# if choice == "add":
#     print(num1 + num2)
# elif choice == "subtract":
#     print(num1 - num2)
# elif choice == "multiply":
#     print(num1 * num2)
# elif choice == "divide":
#     print(num1 / num2)
# elif choice == "remainder":
#     print(num1 // num2)
# elif choice == "squared":
#     print(num1 ** num2)
# else:
#     print("Invalid operation selected.")
