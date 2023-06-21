from tkinter import *
from tkinter import ttk

wn = Tk()
wn.title("BMI Calculator")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14, "normal"))
style.configure("TButton", font=("Arial", 12, "bold"))

# Labels
lbl_w = ttk.Label(text="Enter Your Weight (kg)")
lbl_h = ttk.Label(text="Enter Your Height (cm)")
lbl_calculation = ttk.Label()

# Entries
entry_w = ttk.Entry(width=20)
entry_h = ttk.Entry(width=20)

# Grid Placement
lbl_w.grid(row=0, column=0, padx=10, pady=10)
entry_w.grid(row=1, column=0, padx=10, pady=5)
lbl_h.grid(row=2, column=0, padx=10, pady=10)
entry_h.grid(row=3, column=0, padx=10, pady=5)

def bmi_rate():
    weight_num = entry_w.get()
    height_num = entry_h.get()
    if weight_num == "" or height_num == "":
        lbl_calculation.config(text="Please enter your stats!")
    else:
        try:
            bmi_index = float(weight_num) / ((float(height_num) / 100) ** 2)
            result_bmi = calculation_stats(bmi_index)
            lbl_calculation.config(text=result_bmi)
        except:
            lbl_calculation.config(text="Enter a valid number!")

def calculation_stats(bmi_index):
    result_bmi = f"Your BMI Index is {round(bmi_index, 2)}. You are"
    if bmi_index <= 18.5:
        result_bmi += " underweight"
    elif 18.5 < bmi_index <= 24.9:
        result_bmi += " normal weight"
    elif 25 < bmi_index <= 29.9:
        result_bmi += " overweight"
    elif 30 < bmi_index <= 34.9:
        result_bmi += " obesity (class 1)"
    elif 35 < bmi_index <= 39.9:
        result_bmi += " obesity (class 2)"
    else:
        result_bmi += " extreme obesity"
    return result_bmi

# Button
calculate_button = ttk.Button(text="Calculate", command=bmi_rate)
calculate_button.grid(row=4, column=0, padx=10, pady=10)

# Place lbl_calculation label
lbl_calculation.grid(row=5, column=0, padx=10, pady=10)

wn.mainloop()
