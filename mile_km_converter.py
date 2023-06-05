from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    killometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to killometer converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

miles_label =  Label(text="Miles")
miles_label.grid(column=3, row=1)

is_equal_label = Label(text="is equals to")
is_equal_label.grid(column=1, row=2)

killometer_result_label = Label(text="0")
killometer_result_label.grid(column=2, row=2)

killometer_label = Label(text="km")
killometer_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command = miles_to_km)
calculate_button.grid(column=2, row=3)



window.mainloop()