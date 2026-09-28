import { useState } from 'react'
import { Car } from './assets/components/script.js'
import './App.css'

export default function App() {
  const [model, newModel] = useState(0);

  const handleCar = () => {
    let fuel = document.getElementById('fuel').value;
    let capacity = document.getElementById('capacity').value;
  }


  return (
    <div>
      <div id="form-contener">
        <form action="" method="post">
          <h3>Wpisz informacje o swoim aucie!</h3>

          <label htmlFor="model">Model auta: </label>
          <input type="text" name="car-model" id="car-model" /> <br />

          <label htmlFor="year">Rok auta:</label>
          <input type="number" name="car-year" id="car-year" /> <br />

          <label htmlFor="weight">Waga auta (t): </label>
          <input type="number" name="car-weight" id="car-weight" /> <br />

          <label htmlFor="fuel">Ilość paliwa (l): </label>
          <input type="number" name="fuel" id="fuel" /> <br />

          <label htmlFor="capacity">Pojemność baku (l): </label>
          <input type="number" name="capacity" id="capacity" /> <br />

          <label htmlFor="waste">Spalanie na 100km (l): </label>
          <input type="number" name="fuel-waste" id="fuel-waste" /> <br />

          <button type="submit" onClick={handleCar}>Zatwierdź!</button>
        </form>
      </div>
      <div id="tank-container">
        <ul>
          <li>Ilość paliwa: </li>
          <li>Pojemność baku: </li>
          <li><label htmlFor="tank-info">Ile chcesz zatankować?</label> <input type="number" name="tank-ammount" id="tank-ammount" /></li>
        </ul>
        
      </div>

      <div id="result-container"></div>

      <script src="./components/script.js"></script>
      
    </div>
  )
}

