import tkinter as tk
from tkinter import messagebox
import sympy as sp
def compute_derivative():
    """
    Computes the derivative of the expression entered in the entry fields.
    """
    expr = expression_entry.get()
    var = variable_entry.get()
    
    try:
        # Define the variable
        variable = sp.symbols(var)
        
        # Parse the expression
        expression = sp.sympify(expr)
        
        # Compute the derivative
        derivative = sp.diff(expression, variable)
        
        # Display the result
        result_label.config(text=f"The derivative of {expr} with respect to {var} is: {derivative}")
    except Exception as e:
        # Display error message
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Derivative Calculator")

# Create and place the expression label and entry
expression_label = tk.Label(root, text="Expression:")
expression_label.pack()
expression_entry = tk.Entry(root, width=50)
expression_entry.pack()

# Create and place the variable label and entry
variable_label = tk.Label(root, text="Variable:")
variable_label.pack()
variable_entry = tk.Entry(root, width=50)
variable_entry.pack()

# Create and place the compute button
compute_button = tk.Button(root, text="Compute Derivative", command=compute_derivative)
compute_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
