import pytest
from main import Car

class CarTesting:
    def setup_method(self):
        self.car = Car(model = "Toyota",
                       car_year=2024,
                       car_weight=3.1,
                       fuel=10.5,
                       capacity=100.0,
                       fuel_waste=5.0,
                       is_engine_on=False,
                       are_lights_on=False,
                       speed=0,
                       is_accelerating=False,
                       is_braking=False)

    def test_turn_engine_on_with_fuel(self):
        self.car.fuel = 10.5
        self.car.turn_engine_on()
        assert self.car.turn_engine_on is True
        
    def test_turn_engine_on_without_fuel(self):
        self.car.fuel = 0
        self.car.turn_engine_on()
        assert self.car.turn_engine_on is False
        
    def test_turn_lights_on_with_engine_on(self):
        self.car.is_engine_on = True
        self.car.turn_lights_on()
        assert self.car.turn_lights_on is True

    def test_turn_lights_on_without_engine_on(self):
        self.car.is_engine_on = False
        self.car.turn_lights_on()
        assert self.car.turn_lights_on() is False

    def test_accelarate(self):
        self.car.is_engine_on = True
        self.car.are_lights_on = True
        self.car.speed = 0
        self.car.accelarate()
        assert self.car.speed == 10

    def test_brake(self):
        self.car.is_engine_on = True
        self.car.are_lights_on = True
        self.car.speed = 100
        self.car.brake()
        assert self.car.speed == 90

    def test_refuel(self):
        self.car.is_engine_on = False
        self.car.fuel = 0
        self.car.tank = 10.0
        self.car.refuel()
        assert self.car.fuel == 10.0