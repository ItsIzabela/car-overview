import subprocess
import platform
import time

def clear_console():
    system_name = platform.system()
    if system_name == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


class Car:
    def __init__(
        self,
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
        is_braking=False
    ):
        self.model = model
        self.car_year = car_year
        self.car_weight = car_weight
        self.fuel = fuel
        self.capacity = capacity
        self.fuel_waste = fuel_waste
        self.is_engine_on = is_engine_on
        self.are_lights_on = are_lights_on
        self.speed = speed
        self.is_accelerating = is_accelerating
        self.is_braking = is_braking
        self.distance = 0.0
        self.last_update_time = None

    def show_car_status(self):
        self.update_drive()

        print("--- Status pojazdu ---")
        print(f"Model auta: {self.model}")
        print(f"Rok auta: {self.car_year}")
        print(f"Waga auta: {self.car_weight} t")
        print(f"Ilość paliwa: {self.fuel:.2f} l")
        print(f"Pojemność baku: {self.capacity} l")
        print(f"Czy silnik jest włączony: {self.is_engine_on}")
        print(f"Czy światła są włączone: {self.are_lights_on}")
        print(f"Prędkość auta: {self.speed} km/h")
        print(f"Przejechany dystans: {self.distance:.3f} km")
        print(
            f"Szacowane zużycie paliwa: "
            f"{self.calculate_fuel_consumption():.2f} l/100km"
        )
        print("---")

    def turn_engine_on(self):
        if self.fuel <= 0:
            print("Musisz zatankować!")
        elif self.is_engine_on:
            print("Samochód już jest włączony! Nie można włączyć go drugi raz!")
        else:
            self.is_engine_on = True
            self.last_update_time = time.time()
            print("Włączono samochód")

    def turn_lights_on(self):
        if not self.is_engine_on:
            print("Włącz silnik aby móc włączyć światła!")
        else:
            self.are_lights_on = True
            print("Włączono światła")

    def update_drive(self):
        if self.last_update_time is None:
            self.last_update_time = time.time()
            return

        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        self.last_update_time = current_time

        if not self.is_engine_on or self.speed <= 0:
            return

        distance_traveled = self.speed * (elapsed_time / 3600)

        consumption = self.calculate_fuel_consumption()
        fuel_used = (consumption / 100) * distance_traveled

        if self.fuel >= fuel_used:
            self.distance += distance_traveled
            self.fuel -= fuel_used
        else:
            if consumption > 0:
                possible_distance = (self.fuel / consumption) * 100
                self.distance += possible_distance

            self.fuel = 0
            self.speed = 0
            self.is_engine_on = False
            print("Brak paliwa! Silnik gaśnie.")

    def accelerate(self):
        self.update_drive()

        if not self.is_engine_on:
            print("Silnik jest wyłączony!")
            return

        if self.speed >= 250:
            print("Ograniczono maksymalną prędkość!")
            return

        self.is_accelerating = True
        self.is_braking = False

        self.speed += 10

        print(
            f"Przyśpieszono o 10 km/h. "
            f"Twoja prędkość: {self.speed} km/h"
        )

    def brake(self):
        self.update_drive()

        if not self.is_engine_on:
            print("Silnik jest wyłączony!")
            return

        self.is_braking = True
        self.is_accelerating = False

        if self.speed >= 10:
            self.speed -= 10
            print(
                f"Zwolniono o 10 km/h. "
                f"Twoja prędkość: {self.speed} km/h"
            )
        elif self.speed > 0:
            self.speed = 0
            print("Zatrzymano pojazd!")
        else:
            print("Pojazd już stoi.")

    def refuel(self):
        self.update_drive()

        print(f"Ilość paliwa teraz: {self.fuel:.2f} l")
        print(f"Maksymalna pojemność baku: {self.capacity} l")

        while True:
            try:
                tank = float(input("Ile chcesz zatankować (l): "))

                if tank <= 0:
                    print("Podaj dodatnią wartość.")
                    continue

                if self.fuel + tank <= self.capacity:
                    self.fuel += tank
                    print(f"Zatankowano {tank:.2f} l paliwa.")
                    print(f"Aktualna ilość paliwa: {self.fuel:.2f} l")
                    break
                else:
                    print("Przekraczasz pojemność baku! Spróbuj ponownie.")

            except ValueError:
                print("Podaj poprawną liczbę.")

    def calculate_fuel_consumption(self):
        if self.speed == 0:
            return 0.0

        base_speed = 50
        base_consumption = self.fuel_waste

        if self.speed <= base_speed:
            reduction = (base_speed - self.speed) * 0.03
            consumption = base_consumption - reduction
        else:
            increase = (self.speed - base_speed) * 0.05
            consumption = base_consumption + increase

        return max(consumption, 2.0)

    def run(self):
        print("--- Wprowadź dane swojego pojazdu! ---")

        self.model = self.get_nonempty_string("Model auta: ")
        self.car_year = self.get_valid_int(
            "Rok wyprodukowania auta: ",
            1886,
            2026
        )
        self.car_weight = self.get_valid_float(
            "Waga auta (t): ",
            0.5,
            10.0
        )
        self.capacity = self.get_valid_float(
            "Pojemność baku (l): ",
            10,
            200
        )
        self.fuel = self.get_valid_float(
            "Ile jest teraz paliwa (l): ",
            0,
            self.capacity
        )
        self.fuel_waste = self.get_valid_float(
            "Spalanie na 100km (l): ",
            2,
            30
        )

        print("---")

        while True:
            self.update_drive()

            print("--- MENU ---")
            print("1. Pokaż stan samochodu")
            print("2. Uruchom silnik")
            print("3. Włącz światła")
            print("4. Przyspiesz")
            print("5. Hamuj")
            print("6. Tankuj")
            print("0. Zakończ program")
            print("---")

            action = input("Co chcesz zrobić? : ")

            self.update_drive()
            clear_console()

            if action == "1":
                self.show_car_status()
            elif action == "2":
                self.turn_engine_on()
            elif action == "3":
                self.turn_lights_on()
            elif action == "4":
                self.accelerate()
            elif action == "5":
                self.brake()
            elif action == "6":
                self.refuel()
            elif action == "0":
                print("byebye!")
                break
            else:
                print("Nieprawidłowa opcja")

    def get_nonempty_string(self, prompt):
        while True:
            s = input(prompt).strip()

            if s:
                return s

            print("To pole nie może być puste.")

    def get_valid_int(self, prompt, min_val, max_val):
        while True:
            try:
                val = int(input(prompt))

                if min_val <= val <= max_val:
                    return val

                print(
                    f"Wprowadź liczbę z zakresu "
                    f"{min_val} - {max_val}."
                )

            except ValueError:
                print("Wprowadź poprawną liczbę całkowitą.")

    def get_valid_float(self, prompt, min_val, max_val):
        while True:
            try:
                val = float(input(prompt))

                if min_val <= val <= max_val:
                    return val

                print(
                    f"Wprowadź liczbę z zakresu "
                    f"{min_val} - {max_val}."
                )

            except ValueError:
                print("Wprowadź poprawną liczbę.")


if __name__ == "__main__":
    app = Car()
    app.run()
