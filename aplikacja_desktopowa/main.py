import tkinter as tk

def only_numbers(char):
     return char.isdigit() or char == ""

def only_letters(char):
     return char.isalpha() or char == ""

class Car:
    def __init__(self, root, model="", car_year=0, car_weight=0.0, fuel=0.0, capacity=0.0, fuel_waste=0.0,
                     is_engine_on=False, are_lights_on=False, speed=0, is_accelerating=False, is_braking=False):
            self.root = root

            self.vcmd_num = (root.register(only_numbers), '%P')
            self.vcmd_text = (root.register(only_letters), '%P')

            self.model_label = tk.Label(self.root, text="Model auta:")
            self.model_label.pack()
            self.model = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_text)
            self.model.pack()

            self.car_year_label = tk.Label(self.root, text="Rok wyprodukowania auta:")
            self.car_year_label.pack()
            self.car_year = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_num)
            self.car_year.pack()

            self.car_weight_label = tk.Label(self.root, text="Waga auta (t):")
            self.car_weight_label.pack()
            self.car_weight = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_num)
            self.car_weight.pack()

            self.fuel_label = tk.Label(self.root, text="Ilość paliwa:")
            self.fuel_label.pack()
            self.fuel = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_num)
            self.fuel.pack()

            self.capacity_label = tk.Label(self.root, text="Pojemność baku:")
            self.capacity_label.pack()
            self.capacity = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_num)
            self.capacity.pack()

            self.fuel_waste = fuel_waste # spalanie na 100km 
            self.is_engine_on = is_engine_on
            self.are_lights_on = are_lights_on
            self.speed = speed
            self.is_accelerating = is_accelerating
            self.is_braking = is_braking

            self.result = tk.Label(self.root, text="")
            self.result.pack()

    def entry_view(self):
         model_value = self.model.get()
         car_year_value = self.car_year.get()
         car_weight_value = self.car_weight.get()
         fuel_value = self.fuel.get()
         capacity_value = self.capacity.get()

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

         self.submit_btn.forget()

    def choice(self):
        self.action.get()
        if self.action == "1":
                self.result.config(text="1")
                
    def change_view(self):
         self.entry_view()
         self.menu()

    def menu(self):
         tk.Label(self.root, text="--- Menu --- \n 1. Pokaż status auta \n 2. Włącz silnik \n 3. Włącz światła \n 4. Przyśpiesz \n 5. Hamuj \n 6. Zatankuj \n 0. Wyjście \n --- Menu ---").pack()

         self.action = tk.Entry(self.root, validate='key', validatecommand=self.vcmd_num)
         self.action.pack()
         

         self.action_btn = tk.Button(self.root, text="Ok!", command=self.choice)
         self.action_btn.pack()         

    def view(self):
        self.submit_btn = tk.Button(self.root, text="Zatwierdź!", command=self.change_view)
        self.submit_btn.pack()

    def run(self):
        self.view()
        self.root.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Aplikacja obsługi samochodu")
    app = Car(root)
    app.run()