import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, length=8, uppercase=False, special=False):
        self.length = length
        self.uppercase = uppercase
        self.special = special

    def generate_password(self):
        chars = string.ascii_lowercase
        if self.uppercase:
            chars += string.ascii_uppercase
        if self.special:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(self.length))

class PasswordGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Exportaciones")
        self.window.geometry("300x300")
        self.password_generator = PasswordGenerator()

        self.length_label = tk.Label(self.window, text="Longitud:")
        self.length_entry = tk.Entry(self.window)
        self.length_entry.insert(0, "8")

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbutton = tk.Checkbutton(self.window, text="Incluye mayusculas", variable=self.uppercase_var, fg="purple")

        self.special_var = tk.IntVar()
        self.special_checkbutton = tk.Checkbutton(self.window, text="Incluye caracteres especiales", variable=self.special_var, fg="purple")

        self.generate_button = tk.Button(self.window, text="Generar Contraseña", command=self.generate_password, fg="white", bg="black")

        self.password_label = tk.Label(self.window, text="Tu contraseña es:", fg="purple")
        self.password_entry = tk.Entry(self.window)

        self.length_label.pack()
        self.length_entry.pack()
        self.uppercase_checkbutton.pack()
        self.special_checkbutton.pack()
        self.generate_button.pack()
        self.password_label.pack()
        self.password_entry.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        uppercase = bool(self.uppercase_var.get())
        special = bool(self.special_var.get())
        self.password_generator = PasswordGenerator(length, uppercase, special)
        password = self.password_generator.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        tk.messagebox.showinfo("Password Generated", f"Your password is: {password}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = PasswordGUI()
    gui.run()