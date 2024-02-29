import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Lautaro
apellido:Llusa
---
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

Porcentaje de dinero en función de cada juego

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.ganadores = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            nombre = prompt("UTN", "Nombre del ganador (o 'fin' para terminar):")
            if nombre == None:
                break
            importe = float(prompt("UTN", "Importe ganado (mayor o igual a $1000):"))
            if importe < 1000:
                alert("UTN", "El importe debe ser mayor o igual a $1000.")
                continue
            genero = prompt("UTN", "Género (Femenino/Masculino/Otro):")
            juego = prompt("UTN", "Juego (Ruleta/Poker/Tragamonedas):")

            ganador = (nombre, importe, genero, juego)
            self.ganadores.append(ganador)

    def btn_mostrar_estadisticas_on_click(self):
        if not self.ganadores:
            alert("No hay datos ingresados.")
            return

        ganador_max = max(self.ganadores, key=lambda x: x[1])
        alert("UTN", f"La persona que más ganó es {ganador_max[0]} ({ganador_max[2]}) con un importe de ${ganador_max[1]}")

        total_ruleta = sum(g[1] for g in self.ganadores if g[3] == "Ruleta")
        cantidad_ruleta = sum(1 for g in self.ganadores if g[3] == "Ruleta")
        promedio_ruleta = total_ruleta / cantidad_ruleta if cantidad_ruleta else 0
        alert("UTN", f"El promedio de dinero ganado en Ruleta es ${promedio_ruleta}")

        cantidad_tragamonedas = sum(1 for g in self.ganadores if g[3] == "Tragamonedas")
        porcentaje_tragamonedas = (cantidad_tragamonedas / len(self.ganadores)) * 100
        alert("UTN", f"El porcentaje de personas que jugaron en Tragamonedas es {porcentaje_tragamonedas}%")

        juegos = {"Ruleta": 0, "Poker": 0, "Tragamonedas": 0}
        total_dinero = 0
        for g in self.ganadores:
            juegos[g[3]] += 1
            total_dinero += g[1]
        juego_menos_elegido = min(juegos, key=juegos.get)
        alert("UTN", f"El juego menos elegido por los ganadores es {juego_menos_elegido}")

        total_importe_no_poker = sum(g[1] for g in self.ganadores if g[3] != "Poker" and g[1] > 15000)
        cantidad_no_poker = sum(1 for g in self.ganadores if g[3] != "Poker" and g[1] > 15000)
        promedio_importe_no_poker = total_importe_no_poker / cantidad_no_poker if cantidad_no_poker else 0
        alert("UTN", f"El promedio de importe ganado de las personas que NO jugaron Poker y ganaron más de $15000 es ${promedio_importe_no_poker}")

        porcentaje_ruleta = (total_ruleta / total_dinero) * 100 if total_dinero else 0
        porcentaje_poker = (juegos["Poker"] / total_dinero) * 100 if total_dinero else 0
        porcentaje_tragamonedas = (cantidad_tragamonedas / total_dinero) * 100 if total_dinero else 0

        alert("UTN", f"Porcentaje de dinero en Ruleta: {porcentaje_ruleta}%")
        alert("UTN", f"Porcentaje de dinero en Poker: {porcentaje_poker}%")
        alert("UTN", f"Porcentaje de dinero en Tragamonedas: {porcentaje_tragamonedas}%")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
