import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import time


def only_numbers(char):
    if char == "":
        return True

    try:
        float(char)
        return True
    except ValueError:
        return False


def only_letters(char):
    return char.isalpha() or char == ""


class Car:
    def __init__(
        self,
        root,
        model="",
        car_year=0,
        car_weight=0.0,
        fuel=0.0,
        capacity=0.0,
        fuel_waste=0.0,
        is_engine_on=False,
        are_lights_on=False,
        speed=0,
        is_accelerating=False,
        is_braking=False,
        distance=0,
    ):
        self.root = root

        self.vcmd_num = (root.register(only_numbers), "%P")
        self.vcmd_text = (root.register(only_letters), "%P")

        self.model_label = tk.Label(self.root, text="Model auta:")
        self.model_label.pack()

        self.model = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_text
        )
        self.model.pack()

        self.car_year_label = tk.Label(
            self.root,
            text="Rok wyprodukowania auta:"
        )
        self.car_year_label.pack()

        self.car_year = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.car_year.pack()

        self.car_weight_label = tk.Label(
            self.root,
            text="Waga auta (t):"
        )
        self.car_weight_label.pack()

        self.car_weight = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.car_weight.pack()

        self.fuel_label = tk.Label(
            self.root,
            text="Ilość paliwa:"
        )
        self.fuel_label.pack()

        self.fuel = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.fuel.pack()

        self.capacity_label = tk.Label(
            self.root,
            text="Pojemność baku:"
        )
        self.capacity_label.pack()

        self.capacity = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.capacity.pack()

        self.fuel_waste_label = tk.Label(
            self.root,
            text="Spalanie na 100km (l):"
        )
        self.fuel_waste_label.pack()

        self.fuel_waste = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.fuel_waste.pack()

        self.is_engine_on = is_engine_on
        self.are_lights_on = are_lights_on
        self.speed = speed
        self.is_accelerating = is_accelerating
        self.is_braking = is_braking

        self.distance = distance

        self.last_update_time = time.time()
        self.drive_timer = None

    def entry_view(self):
        self.model_value = self.model.get()
        self.car_year_value = self.car_year.get()
        self.car_weight_value = float(self.car_weight.get())
        self.fuel_value = float(self.fuel.get())
        self.capacity_value = float(self.capacity.get())
        self.fuel_waste_value = float(self.fuel_waste.get())

        self.model_label.forget()
        self.model.forget()

        self.car_year_label.forget()
        self.car_year.forget()

        self.car_weight_label.forget()
        self.car_weight.forget()

        self.fuel_label.forget()
        self.fuel.forget()

        self.capacity_label.forget()
        self.capacity.forget()

        self.fuel_waste_label.forget()
        self.fuel_waste.forget()

        self.submit_btn.forget()

    def validate_all(self):
        model = self.model.get().strip()

        if not model:
            self.show_error("Podaj model auta.")
            return False

        try:
            year = int(self.car_year.get())

            if not (1886 <= year <= 2026):
                raise ValueError

        except ValueError:
            self.show_error(
                "Podaj poprawny rok produkcji auta (1886-2026)."
            )
            return False

        try:
            weight = float(self.car_weight.get())

            if not (0.5 <= weight <= 10.0):
                raise ValueError

        except ValueError:
            self.show_error(
                "Podaj poprawną wagę auta (0.5 - 10.0 t)."
            )
            return False

        try:
            capacity = float(self.capacity.get())

            if not (10 <= capacity <= 200):
                raise ValueError

        except ValueError:
            self.show_error(
                "Podaj poprawną pojemność baku (10 - 200 l)."
            )
            return False

        try:
            fuel = float(self.fuel.get())

            if not (0 <= fuel <= capacity):
                raise ValueError

        except ValueError:
            self.show_error(
                "Podaj poprawną ilość paliwa (0 - pojemność baku)."
            )
            return False

        try:
            fuel_waste = float(self.fuel_waste.get())

            if not (2 <= fuel_waste <= 30):
                raise ValueError

        except ValueError:
            self.show_error(
                "Podaj poprawne spalanie na 100km (2 - 30 l)."
            )
            return False

        return True

    def show_error(self, message):
        messagebox.showerror(
            "Błąd walidacji",
            message
        )

    def turn_engine_on(self):
        if self.fuel_value <= 0:
            self.result.configure(
                text="Musisz zatankować!"
            )

        elif self.is_engine_on:
            self.result.configure(
                text="Samochód już jest włączony! "
                     "Nie można włączyć go drugi raz!"
            )

        else:
            self.is_engine_on = True
            self.last_update_time = time.time()

            self.result.configure(
                text="Włączono samochód"
            )

    def turn_lights_on(self):
        if not self.is_engine_on:
            self.result.configure(
                text="Włącz silnik aby móc włączyć światła!"
            )
        else:
            self.are_lights_on = True

            self.result.configure(
                text="Włączono światła"
            )

    def update_drive(self):
        current_time = time.time()

        elapsed_time = current_time - self.last_update_time

        self.last_update_time = current_time

        if self.is_engine_on and self.speed > 0:

            distance_traveled = (
                self.speed * (elapsed_time / 3600)
            )

            self.distance += distance_traveled

            consumption = self.calculate_fuel_consumption()

            fuel_used = (
                consumption / 100
            ) * distance_traveled

            if self.fuel_value >= fuel_used:

                self.fuel_value -= fuel_used

                if hasattr(self, "fuel_bar"):
                    self.update_fuel_display()

            else:
                # Brak paliwa
                self.fuel_value = 0
                self.speed = 0
                self.is_engine_on = False

                self.result.configure(
                    text="Brak paliwa! Silnik gaśnie."
                )

                if hasattr(self, "fuel_bar"):
                    self.update_fuel_display()

        self.drive_timer = self.root.after(
            100,
            self.update_drive
        )

    def start_drive_timer(self):
        self.last_update_time = time.time()

        self.drive_timer = self.root.after(
            100,
            self.update_drive
        )

    def accelerate(self):
        if not self.is_engine_on:
            self.result.configure(
                text="Silnik jest wyłączony!"
            )
            return

        if self.speed >= 250:
            self.result.configure(
                text="Ograniczono maksymalną prędkość!"
            )
            return

        self.is_accelerating = True

        self.speed += 10

        self.result.configure(
            text=f"Przyśpieszono o 10 km/h. "
                 f"Twoja prędkość: {self.speed} km/h"
        )

    def brake(self):
        if not self.is_engine_on:
            self.result.configure(
                text="Silnik jest wyłączony!"
            )
            return

        self.is_braking = True

        if self.speed >= 10:
            self.speed -= 10

            self.result.configure(
                text=f"Zwolniono o 10 km/h. "
                     f"Twoja prędkość: {self.speed} km/h"
            )

        elif self.speed > 0:
            self.speed = 0

            self.result.configure(
                text="Zatrzymano pojazd!"
            )

        else:
            self.result.configure(
                text="Pojazd już stoi."
            )
    def refuel_view(self):
        if hasattr(self, "refuel_drive_btn"):
            self.refuel_drive_btn.config(
                state="disabled"
            )

        self.result.configure(
            text=f"Ilość paliwa: "
                 f"{self.fuel_value:.2f} / "
                 f"{self.capacity_value:.2f} l"
        )

        self.tank = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.tank.pack(
            side="bottom",
            pady=5
        )

        self.tank_btn = tk.Button(
            self.root,
            text="Zatankuj!",
            command=self.refuel
        )
        self.tank_btn.pack(
            side="bottom",
            pady=5
        )

    def refuel(self):
        try:
            self.tank_value = float(
                self.tank.get()
            )

        except ValueError:
            self.result.configure(
                text="Podaj ilość paliwa."
            )
            return

        if self.tank_value <= 0:
            self.result.configure(
                text="Podaj dodatnią wartość."
            )
            return

        if (
            self.fuel_value + self.tank_value
            > self.capacity_value
        ):
            self.result.configure(
                text="Przekraczasz pojemność baku!"
            )
            return

        self.fuel_value += self.tank_value

        if hasattr(self, "fuel_bar"):
            self.update_fuel_display()

        self.result.configure(
            text=f"Zatankowano "
                 f"{self.tank_value:.2f} l.\n"
                 f"Aktualne paliwo: "
                 f"{self.fuel_value:.2f} l"
        )

        self.tank.destroy()
        self.tank_btn.destroy()

        if hasattr(self, "refuel_drive_btn"):
            self.refuel_drive_btn.config(
                state="normal"
            )

    def calculate_fuel_consumption(self):
        if self.speed == 0:
            return 0.0

        base_speed = 50
        base_consumption = self.fuel_waste_value

        if self.speed <= base_speed:

            reduction = (
                base_speed - self.speed
            ) * 0.03

            consumption = (
                base_consumption - reduction
            )

        else:

            increase = (
                self.speed - base_speed
            ) * 0.05

            consumption = (
                base_consumption + increase
            )

        return max(
            consumption,
            2.0
        )

    def drive_mode(self):
        self.result.configure(
            text="Włączono tryb jazdy!"
        )

        self.angle = 0

        self.quit_mode = tk.Button(
            self.root,
            text="Wyjście z drive mode",
            command=self.quit_drive_mode
        )
        self.quit_mode.pack(
            side="bottom",
            pady=5
        )

        self.refuel_drive_btn = tk.Button(
            self.root,
            text="⛽ Tankowanie",
            command=self.refuel_view
        )
        self.refuel_drive_btn.pack(
            side="bottom",
            pady=5
        )

        self.right = tk.Button(
            self.root,
            text="Skręć w prawo!",
            command=self.turn_right
        )
        self.right.pack(
            side="bottom",
            pady=5
        )

        self.left = tk.Button(
            self.root,
            text="Skręć w lewo!",
            command=self.turn_left
        )
        self.left.pack(
            side="bottom",
            pady=5
        )

        self.fuel_label = tk.Label(
            self.root,
            text=f"Paliwo: "
                 f"{self.fuel_value:.2f} / "
                 f"{self.capacity_value:.2f} l"
        )
        self.fuel_label.pack(
            side="bottom",
            pady=5
        )

        self.fuel_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=self.capacity_value
        )
        self.fuel_bar.pack(
            side="bottom",
            pady=5
        )

        self.fuel_bar["value"] = self.fuel_value

        self.car_image = Image.open(
            "./aplikacja_desktopowa/car_image.png"
        ).convert("RGBA")

        self.car_image = self.car_image.resize(
            (100, 100)
        )

        self.car_photo = ImageTk.PhotoImage(
            self.car_image
        )

        self.car_model = tk.Label(
            self.root,
            image=self.car_photo
        )
        self.car_model.pack(
            side="bottom",
            pady=5
        )

    def turn_left(self):
        self.angle = -50

        self.update_car()

        self.root.after(
            500,
            self.reset_car
        )

    def turn_right(self):
        self.angle = 50

        self.update_car()

        self.root.after(
            500,
            self.reset_car
        )

    def reset_car(self):
        self.angle = 0

        self.update_car()

    def update_car(self):
        rotated = self.car_image.rotate(
            self.angle,
            expand=True
        )

        self.car_photo = ImageTk.PhotoImage(
            rotated
        )

        self.car_model.configure(
            image=self.car_photo
        )

        self.car_model.image = self.car_photo

    def update_fuel_display(self):
        if not hasattr(self, "fuel_bar"):
            return

        self.fuel_bar["value"] = self.fuel_value

        self.fuel_label.configure(
            text=f"Paliwo: "
                 f"{self.fuel_value:.2f} / "
                 f"{self.capacity_value:.2f} l"
        )

    def quit_drive_mode(self):
        self.car_model.destroy()
        self.left.destroy()
        self.right.destroy()
        self.quit_mode.destroy()

        self.fuel_label.destroy()
        self.fuel_bar.destroy()
        self.refuel_drive_btn.destroy()

    def choice(self):
        action_num = self.action.get()

        if action_num == "1":

            self.result.configure(
                text=(
                    f"--- Status pojazdu ---\n"
                    f"Model auta: {self.model_value}\n"
                    f"Rok auta: {self.car_year_value}\n"
                    f"Waga auta: {self.car_weight_value} t\n"
                    f"Ilość paliwa: {self.fuel_value:.2f} l\n"
                    f"Pojemność baku: {self.capacity_value:.2f} l\n"
                    f"Czy silnik jest włączony: "
                    f"{self.is_engine_on}\n"
                    f"Czy światła są włączone: "
                    f"{self.are_lights_on}\n"
                    f"Prędkość auta: "
                    f"{self.speed} km/h\n"
                    f"Przejechany dystans: "
                    f"{self.distance:.2f} km\n"
                    f"Szacowane zużycie paliwa: "
                    f"{self.calculate_fuel_consumption():.2f} "
                    f"l/100km\n"
                    f"--- Status pojazdu ---"
                )
            )

        elif action_num == "2":
            self.turn_engine_on()

        elif action_num == "3":
            self.turn_lights_on()

        elif action_num == "4":
            self.accelerate()

        elif action_num == "5":
            self.brake()

        elif action_num == "6":
            self.refuel_view()

        elif action_num == "7":

            if (
                not self.is_engine_on
                or not self.are_lights_on
            ):
                self.show_error(
                    "Musisz włączyć silnik i światła "
                    "aby móc wejść w tryb jazdy!"
                )

            else:
                self.drive_mode()

        elif action_num == "0":
            self.root.destroy()

    def change_view(self):
        if self.validate_all():
            self.entry_view()
            self.start_drive_timer()

            self.menu()

    def menu(self):
        tk.Label(
            self.root,
            text=(
                "--- Menu ---\n"
                "1. Pokaż status auta\n"
                "2. Włącz silnik\n"
                "3. Włącz światła\n"
                "4. Przyśpiesz\n"
                "5. Hamuj\n"
                "6. Zatankuj\n"
                "7. Tryb jazdy\n"
                "0. Wyjście\n"
                "--- Menu ---"
            )
        ).pack()

        self.action = tk.Entry(
            self.root,
            validate="key",
            validatecommand=self.vcmd_num
        )
        self.action.pack()

        self.action_btn = tk.Button(
            self.root,
            text="Ok!",
            command=self.choice
        )
        self.action_btn.pack()

        self.result = tk.Label(
            self.root,
            text=""
        )
        self.result.pack()

    def view(self):
        self.submit_btn = tk.Button(
            self.root,
            text="Zatwierdź!",
            command=self.change_view
        )
        self.submit_btn.pack()

    def run(self):
        self.view()

        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x900")
    root.title(
        "Aplikacja obsługi samochodu"
    )

    app = Car(root)
    app.run()
