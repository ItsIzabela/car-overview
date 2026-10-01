export class Car {
  constructor({
    model = "",
    year = 0,
    weight = 0,
    fuel = 0,
    capacity = 0,
    fuelWaste = 0,
  }) {
    this.model = model;
    this.year = year;
    this.weight = weight;
    this.fuel = fuel;
    this.capacity = capacity;
    this.fuelWaste = fuelWaste;

    this.isEngineOn = false;
    this.areLightsOn = false;

    this.speed = 0;
    this.distance = 0;

    this.isAccelerating = false;
    this.isBraking = false;
  }

  validate() {
    const model = this.model.trim();

    if (!model) {
      return {
        valid: false,
        message: "Podaj model auta.",
      };
    }

    if (!Number.isInteger(this.year) || this.year < 1886 || this.year > 2026) {
      return {
        valid: false,
        message:
          "Podaj poprawny rok produkcji auta (1886-2026).",
      };
    }

    if (this.weight < 0.5 || this.weight > 10) {
      return {
        valid: false,
        message:
          "Podaj poprawną wagę auta (0.5 - 10.0 t).",
      };
    }

    if (this.capacity < 10 || this.capacity > 200) {
      return {
        valid: false,
        message:
          "Podaj poprawną pojemność baku (10 - 200 l).",
      };
    }

    if (this.fuel < 0 || this.fuel > this.capacity) {
      return {
        valid: false,
        message:
          "Podaj poprawną ilość paliwa (0 - pojemność baku).",
      };
    }

    if (this.fuelWaste < 2 || this.fuelWaste > 30) {
      return {
        valid: false,
        message:
          "Podaj poprawne spalanie na 100 km (2 - 30 l).",
      };
    }

    return {
      valid: true,
      message: "",
    };
  }

  clone() {
    const newCar = new Car({
      model: this.model,
      year: this.year,
      weight: this.weight,
      fuel: this.fuel,
      capacity: this.capacity,
      fuelWaste: this.fuelWaste,
    });

    newCar.isEngineOn = this.isEngineOn;
    newCar.areLightsOn = this.areLightsOn;
    newCar.speed = this.speed;
    newCar.distance = this.distance;
    newCar.isAccelerating = this.isAccelerating;
    newCar.isBraking = this.isBraking;

    return newCar;
  }

  turnEngineOn() {
    const car = this.clone();

    if (car.fuel <= 0) {
      return {
        car,
        message: "Musisz zatankować!",
      };
    }

    if (car.isEngineOn) {
      return {
        car,
        message:
          "Samochód już jest włączony! Nie można włączyć go drugi raz!",
      };
    }

    car.isEngineOn = true;

    return {
      car,
      message: "Włączono samochód",
    };
  }

  turnLightsOn() {
    const car = this.clone();

    if (!car.isEngineOn) {
      return {
        car,
        message:
          "Włącz silnik aby móc włączyć światła!",
      };
    }

    car.areLightsOn = true;

    return {
      car,
      message: "Włączono światła",
    };
  }

  accelerate() {
    const car = this.clone();

    if (!car.isEngineOn) {
      return {
        car,
        message: "Silnik jest wyłączony!",
      };
    }

    if (car.speed >= 250) {
      return {
        car,
        message: "Ograniczono maksymalną prędkość!",
      };
    }

    car.isAccelerating = true;
    car.speed = Math.min(car.speed + 10, 250);

    return {
      car,
      message:
        `Przyśpieszono o 10 km/h. ` +
        `Twoja prędkość: ${car.speed} km/h`,
    };
  }

  brake() {
    const car = this.clone();

    if (!car.isEngineOn) {
      return {
        car,
        message: "Silnik jest wyłączony!",
      };
    }

    car.isBraking = true;

    if (car.speed >= 10) {
      car.speed -= 10;

      return {
        car,
        message:
          `Zwolniono o 10 km/h. ` +
          `Twoja prędkość: ${car.speed} km/h`,
      };
    }

    if (car.speed > 0) {
      car.speed = 0;

      return {
        car,
        message: "Zatrzymano pojazd!",
      };
    }

    return {
      car,
      message: "Pojazd już stoi.",
    };
  }

  calculateFuelConsumption() {
    if (this.speed === 0) {
      return 0;
    }

    const baseSpeed = 50;
    const baseConsumption = this.fuelWaste;

    let consumption;

    if (this.speed <= baseSpeed) {
      const reduction =
        (baseSpeed - this.speed) * 0.03;

      consumption = baseConsumption - reduction;
    } else {
      const increase =
        (this.speed - baseSpeed) * 0.05;

      consumption = baseConsumption + increase;
    }

    return Math.max(consumption, 2);
  }

  updateDrive() {
    const car = this.clone();

    if (!car.isEngineOn || car.speed <= 0) {
      return car;
    }

    // updateDrive wykonywany co 100 ms
    const elapsedTime = 0.1;

    const distanceTraveled =
      car.speed * (elapsedTime / 3600);

    car.distance += distanceTraveled;

    const consumption =
      car.calculateFuelConsumption();

    const fuelUsed =
      (consumption / 100) * distanceTraveled;

    if (car.fuel >= fuelUsed) {
      car.fuel -= fuelUsed;

      return car;
    }

    car.fuel = 0;
    car.speed = 0;
    car.isEngineOn = false;

    car.lastMessage = "Brak paliwa! Silnik gaśnie.";

    return car;
  }

  refuel(amount) {
    const car = this.clone();

    if (!Number.isFinite(amount)) {
      return {
        car,
        success: false,
        message: "Podaj ilość paliwa.",
      };
    }

    if (amount <= 0) {
      return {
        car,
        success: false,
        message: "Podaj dodatnią wartość.",
      };
    }

    if (car.fuel + amount > car.capacity) {
      return {
        car,
        success: false,
        message: "Przekraczasz pojemność baku!",
      };
    }

    car.fuel += amount;

    return {
      car,
      success: true,
      message:
        `Zatankowano ${amount.toFixed(2)} l. ` +
        `Aktualne paliwo: ${car.fuel.toFixed(2)} l`,
    };
  }
}
