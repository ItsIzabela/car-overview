import { useEffect, useState } from 'react';
import { Car } from './assets/components/script.js';
import carImage from './assets/car_image.png';
import './App.css';

function App() {
  const [car, setCar] = useState(null);
  const [isDriving, setIsDriving] = useState(false);
  const [message, setMessage] = useState('');
  const [angle, setAngle] = useState(0);

  const [form, setForm] = useState({
    model: '',
    year: '',
    weight: '',
    fuel: '',
    capacity: '',
    fuelWaste: '',
  });

  const [refuelAmount, setRefuelAmount] = useState('');

  useEffect(() => {
    if (!isDriving || !car) return;

    const interval = setInterval(() => {
      setCar((previousCar) => {
        const newCar = previousCar.updateDrive();

        if (newCar.lastMessage) {
          setMessage(newCar.lastMessage);
        }

        return newCar;
      });
    }, 100);

    return () => clearInterval(interval);
  }, [isDriving, car]);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const createCar = (e) => {
    e.preventDefault();

    const newCar = new Car({
      model: form.model,
      year: Number(form.year),
      weight: Number(form.weight),
      fuel: Number(form.fuel),
      capacity: Number(form.capacity),
      fuelWaste: Number(form.fuelWaste),
    });

    const validation = newCar.validate();

    if (!validation.valid) {
      setMessage(validation.message);
      return;
    }

    setCar(newCar);
    setIsDriving(false);
    setMessage('Utworzono samochód!');
  };

  const action = (method) => {
    if (!car) return;

    if (
      !isDriving &&
      (method === 'accelerate' || method === 'brake')
    ) {
      setMessage('Uruchom tryb jazdy!');
      return;
    }

    const result = car[method]();

    setCar(result.car);
    setMessage(result.message);
  };

  const startDriving = () => {
    if (!car) return;

    if (!car.isEngineOn) {
      setMessage('Najpierw włącz silnik!');
      return;
    }

    if (!car.areLightsOn) {
      setMessage('Najpierw włącz światła!');
      return;
    }

    setIsDriving(true);
    setMessage('Uruchomiono tryb jazdy!');
  };

  const stopDriving = () => {
    setIsDriving(false);
    setMessage('Zatrzymano tryb jazdy.');
  };

  const turn = (direction) => {
    if (!car) return;

    if (!isDriving) {
      setMessage('Uruchom tryb jazdy!');
      return;
    }

    setAngle(direction === 'left' ? -50 : 50);

    setTimeout(() => {
      setAngle(0);
    }, 500);

    setMessage(
      direction === 'left'
        ? 'Skręcono w lewo.'
        : 'Skręcono w prawo.'
    );
  };

  const refuel = () => {
    if (!car) return;

    if (isDriving) {
      setMessage('Nie można tankować podczas jazdy!');
      return;
    }

    const amount = Number(refuelAmount);

    const result = car.refuel(amount);

    setCar(result.car);
    setMessage(result.message);
    setRefuelAmount('');
  };

  const fuelPercent = car
    ? (car.fuel / car.capacity) * 100
    : 0;

  return (
    <div className="app">
      <header>
        <h1>Kontrola samochodu</h1>
      </header>

      {!car && (
        <main>
          <h2>Utwórz samochód</h2>

          <form onSubmit={createCar}>
            <p>
              <label>Model:</label>
              <br />
              <input
                name="model"
                value={form.model}
                onChange={handleChange}
              />
            </p>

            <p>
              <label>Rok produkcji:</label>
              <br />
              <input
                type="number"
                name="year"
                value={form.year}
                onChange={handleChange}
              />
            </p>

            <p>
              <label>Waga (t):</label>
              <br />
              <input
                type="number"
                step="0.1"
                name="weight"
                value={form.weight}
                onChange={handleChange}
              />
            </p>

            <p>
              <label>Paliwo (l):</label>
              <br />
              <input
                type="number"
                step="0.1"
                name="fuel"
                value={form.fuel}
                onChange={handleChange}
              />
            </p>

            <p>
              <label>Pojemność baku (l):</label>
              <br />
              <input
                type="number"
                step="0.1"
                name="capacity"
                value={form.capacity}
                onChange={handleChange}
              />
            </p>

            <p>
              <label>Spalanie (l/100 km):</label>
              <br />
              <input
                type="number"
                step="0.1"
                name="fuelWaste"
                value={form.fuelWaste}
                onChange={handleChange}
              />
            </p>

            <button type="submit">
              Utwórz samochód
            </button>
          </form>

          {message && <p>{message}</p>}
        </main>
      )}

      {car && (
        <main>
          <h2>{car.model}</h2>

          <img
            src={carImage}
            alt="Samochód"
            width="300"
            style={{
              transform: `rotate(${angle}deg)`,
            }}
          />

          <p>Rok: {car.year}</p>
          <p>Waga: {car.weight} t</p>
          <p>Prędkość: {car.speed} km/h</p>
          <p>Dystans: {car.distance.toFixed(2)} km</p>

          <p>
            Paliwo: {car.fuel.toFixed(2)} / {car.capacity} l
          </p>

          <progress
            value={fuelPercent}
            max="100"
          />

          <p>
            Silnik:{' '}
            {car.isEngineOn ? 'Włączony' : 'Wyłączony'}
          </p>

          <p>
            Światła:{' '}
            {car.areLightsOn ? 'Włączone' : 'Wyłączone'}
          </p>

          <p>
            Tryb jazdy:{' '}
            {isDriving ? 'Włączony' : 'Wyłączony'}
          </p>

          <section>
            <h3>Samochód</h3>

            <button onClick={() => action('turnEngineOn')}>
              Włącz silnik
            </button>

            <button onClick={() => action('turnLightsOn')}>
              Włącz światła
            </button>

            <button onClick={startDriving}>
              Uruchom tryb jazdy
            </button>

            <button onClick={stopDriving}>
              Zatrzymaj tryb jazdy
            </button>
          </section>

          <section>
            <h3>Jazda</h3>

            <button onClick={() => action('accelerate')}>
              Przyspiesz
            </button>

            <button onClick={() => action('brake')}>
              Hamuj
            </button>

            <button onClick={() => turn('left')}>
              Skręć w lewo
            </button>

            <button onClick={() => turn('right')}>
              Skręć w prawo
            </button>
          </section>

          <section>
            <h3>Tankowanie</h3>

            <input
              type="number"
              step="0.1"
              value={refuelAmount}
              onChange={(e) => setRefuelAmount(e.target.value)}
              placeholder="Ilość paliwa"
            />

            <button
              onClick={refuel}
              disabled={isDriving}
            >
              Zatankuj
            </button>

            {isDriving && (
              <p>Nie można tankować podczas jazdy.</p>
            )}
          </section>

          {message && <p>{message}</p>}
        </main>
      )}
    </div>
  );
}

export default App;
