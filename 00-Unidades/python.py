import tkinter
from tkinter.simpledialog import askstring
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.title("UTN FRA")
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def input_validation(self, prompt_text, input_type, validation_condition):
        while True:
            user_input = askstring("Ingrese", prompt_text)
            try:
                user_input = input_type(user_input)
                if validation_condition(user_input):
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                pass

    def btn_mostrar_on_click(self):
        # Initialize variables
        statistics = {
            "M": {"count": 0, "sum_age": 0, "lowest_temp": float('inf'), "name_lowest_temp": ""},
            "F": {"count": 0, "sum_age": 0, "lowest_temp": float('inf'), "name_lowest_temp": ""},
            "NB": {"count": 0, "sum_age": 0, "highest_temp": float('-inf'), "name_highest_temp": ""},
            "total_fever": 0
        }
        num_adults = 0
        sum_adults_age = 0
        num_minors = 0
        sum_minors_age = 0

        for _ in range(5):
            name = askstring("Ingrese", "Ingrese nombre")
            temperature = self.input_validation("Ingrese temperatura", float, lambda x: 35 <= x <= 42)
            sex = self.input_validation("Ingrese sexo (f, m, nb)", str, lambda x: x in ["f", "m", "nb"])
            age = self.input_validation("Ingrese edad", int, lambda x: x > 0)

            # Update statistics
            statistics[sex]["count"] += 1
            statistics[sex]["sum_age"] += age

            if age >= 18:
                num_adults += 1
                sum_adults_age += age
            else:
                num_minors += 1
                sum_minors_age += age

            if temperature > 38:
                statistics["total_fever"] += 1

            if sex == "F" and temperature < statistics["F"]["lowest_temp"]:
                statistics["F"]["lowest_temp"] = temperature
                statistics["F"]["name_lowest_temp"] = name
            elif sex == "M" and temperature < statistics["M"]["lowest_temp"]:
                statistics["M"]["lowest_temp"] = temperature
                statistics["M"]["name_lowest_temp"] = name
            elif sex == "NB" and temperature > statistics["NB"]["highest_temp"]:
                statistics["NB"]["highest_temp"] = temperature
                statistics["NB"]["name_highest_temp"] = name

        # Calculate averages
        statistics["average_age_M"] = statistics["M"]["sum_age"] / statistics["M"]["count"] if statistics["M"]["count"] > 0 else 0
        statistics["average_age_NB"] = statistics["NB"]["sum_age"] / statistics["NB"]["count"] if statistics["NB"]["count"] > 0 else 0
        statistics["average_age_F"] = statistics["F"]["sum_age"] / statistics["F"]["count"] if statistics["F"]["count"] > 0 else 0
        statistics["average_adult_age"] = sum_adults_age / num_adults if num_adults > 0 else 0
        statistics["average_minor_age"] = sum_minors_age / num_minors if num_minors > 0 else 0

        # Display statistics
        print(statistics)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
