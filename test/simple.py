import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

result_label = sg.Text("", size=(20, 1))

layout = [[feet_label, feet_input],
          [inches_label, inches_input],
          [button],
          [result_label]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Convert":
        feet = float(values[0])
        inches = float(values[1])
        total_inches = feet * 12 + inches
        result_label.update(f"Total inches: {total_inches}")

window.close()