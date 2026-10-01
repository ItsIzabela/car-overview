package com.example.aplikacja_mobilna

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.example.aplikacja_mobilna.ui.theme.Aplikacja_mobilnaTheme
import kotlinx.coroutines.delay

data class Car(
    val model: String,
    val year: Int,
    val weight: Double,
    var fuel: Double,
    val capacity: Double,
    val fuelWaste: Double,
    var engineOn: Boolean = false,
    var lightsOn: Boolean = false,
    var speed: Int = 0,
    var distance: Double = 0.0
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        setContent {
            Aplikacja_mobilnaTheme {
                Scaffold(
                    modifier = Modifier.fillMaxSize()
                ) { innerPadding ->
                    CarApp(
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
fun CarApp(modifier: Modifier = Modifier) {

    var car by remember { mutableStateOf<Car?>(null) }

    var driving by remember { mutableStateOf(false) }

    var message by remember { mutableStateOf("") }

    var model by remember { mutableStateOf("") }
    var year by remember { mutableStateOf("") }
    var weight by remember { mutableStateOf("") }
    var fuel by remember { mutableStateOf("") }
    var capacity by remember { mutableStateOf("") }
    var fuelWaste by remember { mutableStateOf("") }

    var refuelAmount by remember { mutableStateOf("") }

    LaunchedEffect(driving) {
        while (driving) {

            delay(100)

            val currentCar = car ?: continue

            if (currentCar.engineOn && currentCar.speed > 0) {

                val distance = currentCar.speed * (0.1 / 3600)

                currentCar.distance += distance

                val consumption = currentCar.fuelWaste
                val fuelUsed = (consumption / 100) * distance

                currentCar.fuel -= fuelUsed

                if (currentCar.fuel <= 0) {
                    currentCar.fuel = 0.0
                    currentCar.speed = 0
                    currentCar.engineOn = false
                    driving = false
                    message = "Brak paliwa! Silnik gaśnie."
                }

                car = currentCar.copy()
            }
        }
    }

    if (car == null) {

        Column(
            modifier = modifier
                .fillMaxSize()
                .padding(20.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            Text("Kontrola samochodu")

            Spacer(modifier = Modifier.height(20.dp))

            Text("Utwórz samochód")

            Spacer(modifier = Modifier.height(10.dp))

            OutlinedTextField(
                value = model,
                onValueChange = { model = it },
                label = { Text("Model") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = year,
                onValueChange = { year = it },
                label = { Text("Rok produkcji") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Number
                ),
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = weight,
                onValueChange = { weight = it },
                label = { Text("Waga (t)") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Decimal
                ),
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = fuel,
                onValueChange = { fuel = it },
                label = { Text("Paliwo (l)") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Decimal
                ),
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = capacity,
                onValueChange = { capacity = it },
                label = { Text("Pojemność baku (l)") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Decimal
                ),
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = fuelWaste,
                onValueChange = { fuelWaste = it },
                label = { Text("Spalanie (l/100 km)") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Decimal
                ),
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(10.dp))

            Button(
                onClick = {

                    val newCar = Car(
                        model = model,
                        year = year.toIntOrNull() ?: 0,
                        weight = weight.toDoubleOrNull() ?: 0.0,
                        fuel = fuel.toDoubleOrNull() ?: 0.0,
                        capacity = capacity.toDoubleOrNull() ?: 0.0,
                        fuelWaste = fuelWaste.toDoubleOrNull() ?: 0.0
                    )

                    if (newCar.model.isBlank()) {
                        message = "Podaj model auta."
                    } else if (newCar.year < 1886 || newCar.year > 2026) {
                        message = "Podaj poprawny rok produkcji."
                    } else if (newCar.weight < 0.5 || newCar.weight > 10) {
                        message = "Podaj poprawną wagę auta."
                    } else if (newCar.capacity < 10 || newCar.capacity > 200) {
                        message = "Podaj poprawną pojemność baku."
                    } else if (
                        newCar.fuel < 0 ||
                        newCar.fuel > newCar.capacity
                    ) {
                        message = "Podaj poprawną ilość paliwa."
                    } else if (
                        newCar.fuelWaste < 2 ||
                        newCar.fuelWaste > 30
                    ) {
                        message = "Podaj poprawne spalanie."
                    } else {
                        car = newCar
                        message = "Utworzono samochód!"
                    }
                }
            ) {
                Text("Utwórz samochód")
            }

            Spacer(modifier = Modifier.height(10.dp))

            Text(message)
        }

    } else {

        val currentCar = car!!

        Column(
            modifier = modifier
                .fillMaxSize()
                .padding(20.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {

            Text("Kontrola samochodu")

            Spacer(modifier = Modifier.height(10.dp))

            Text(currentCar.model)

            Spacer(modifier = Modifier.height(15.dp))

            Text("Rok: ${currentCar.year}")
            Text("Waga: ${currentCar.weight} t")
            Text("Prędkość: ${currentCar.speed} km/h")
            Text("Dystans: %.2f km".format(currentCar.distance))

            Spacer(modifier = Modifier.height(10.dp))

            Text(
                "Paliwo: %.2f / %.2f l".format(
                    currentCar.fuel,
                    currentCar.capacity
                )
            )

            LinearProgressIndicator(
                progress = {
                    (
                            currentCar.fuel /
                                    currentCar.capacity
                            ).toFloat()
                },
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(10.dp))

            Text(
                "Silnik: " +
                        if (currentCar.engineOn)
                            "Włączony"
                        else
                            "Wyłączony"
            )

            Text(
                "Światła: " +
                        if (currentCar.lightsOn)
                            "Włączone"
                        else
                            "Wyłączone"
            )

            Text(
                "Tryb jazdy: " +
                        if (driving)
                            "Włączony"
                        else
                            "Wyłączony"
            )

            Spacer(modifier = Modifier.height(15.dp))

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {

                Button(
                    onClick = {

                        if (currentCar.fuel <= 0) {
                            message = "Musisz zatankować!"
                        } else if (currentCar.engineOn) {
                            message = "Samochód już jest włączony!"
                        } else {
                            currentCar.engineOn = true
                            car = currentCar.copy()
                            message = "Włączono samochód"
                        }
                    }
                ) {
                    Text("Silnik")
                }

                Button(
                    onClick = {

                        if (!currentCar.engineOn) {
                            message = "Włącz silnik aby włączyć światła!"
                        } else {
                            currentCar.lightsOn = true
                            car = currentCar.copy()
                            message = "Włączono światła"
                        }
                    }
                ) {
                    Text("Światła")
                }
            }

            Spacer(modifier = Modifier.height(10.dp))

            Button(
                onClick = {

                    if (!currentCar.engineOn) {
                        message = "Najpierw włącz silnik!"
                    } else if (!currentCar.lightsOn) {
                        message = "Najpierw włącz światła!"
                    } else {
                        driving = true
                        message = "Uruchomiono tryb jazdy!"
                    }
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Uruchom tryb jazdy")
            }

            Button(
                onClick = {
                    driving = false
                    message = "Zatrzymano tryb jazdy."
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Zatrzymaj tryb jazdy")
            }

            Spacer(modifier = Modifier.height(10.dp))

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {

                Button(
                    onClick = {

                        if (!driving) {
                            message = "Uruchom tryb jazdy!"
                        } else if (!currentCar.engineOn) {
                            message = "Silnik jest wyłączony!"
                        } else if (currentCar.speed >= 250) {
                            message = "Ograniczono maksymalną prędkość!"
                        } else {
                            currentCar.speed += 10
                            car = currentCar.copy()
                            message = "Przyspieszono o 10 km/h"
                        }
                    }
                ) {
                    Text("Przyspiesz")
                }

                Button(
                    onClick = {

                        if (!driving) {
                            message = "Uruchom tryb jazdy!"
                        } else if (!currentCar.engineOn) {
                            message = "Silnik jest wyłączony!"
                        } else if (currentCar.speed >= 10) {
                            currentCar.speed -= 10
                            car = currentCar.copy()
                            message = "Zwolniono o 10 km/h"
                        } else {
                            currentCar.speed = 0
                            car = currentCar.copy()
                            message = "Zatrzymano pojazd!"
                        }
                    }
                ) {
                    Text("Hamuj")
                }
            }

            Spacer(modifier = Modifier.height(10.dp))

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {

                Button(
                    onClick = {

                        if (!driving) {
                            message = "Uruchom tryb jazdy!"
                        } else {
                            message = "Skręcono w lewo"
                        }
                    }
                ) {
                    Text("←")
                }

                Button(
                    onClick = {

                        if (!driving) {
                            message = "Uruchom tryb jazdy!"
                        } else {
                            message = "Skręcono w prawo"
                        }
                    }
                ) {
                    Text("→")
                }
            }

            Spacer(modifier = Modifier.height(15.dp))

            Text("Tankowanie")

            OutlinedTextField(
                value = refuelAmount,
                onValueChange = { refuelAmount = it },
                label = { Text("Ilość paliwa") },
                keyboardOptions = KeyboardOptions(
                    keyboardType = KeyboardType.Decimal
                ),
                modifier = Modifier.fillMaxWidth()
            )

            Button(
                onClick = {

                    if (driving) {
                        message = "Nie można tankować podczas jazdy!"
                        return@Button
                    }

                    val amount =
                        refuelAmount.toDoubleOrNull()

                    if (amount == null || amount <= 0) {
                        message = "Podaj dodatnią wartość."
                    } else if (
                        currentCar.fuel + amount >
                        currentCar.capacity
                    ) {
                        message = "Przekraczasz pojemność baku!"
                    } else {
                        currentCar.fuel += amount
                        car = currentCar.copy()
                        refuelAmount = ""

                        message =
                            "Zatankowano %.2f l".format(amount)
                    }
                },
                enabled = !driving,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Zatankuj")
            }

            Spacer(modifier = Modifier.height(10.dp))

            Text(message)
        }
    }
}

