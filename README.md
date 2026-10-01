# Sterowanie samochodem

**Tytuł:** dokumentacja aplikacji do sterowania samochodem

**Imię i nazwisko zdającego:** XYZ

**Numer PESEL:** XYZ

**Data wykonania:** 01.10.2026

---

### Spis treści

[Sterowanie samochodem](#sterowanie-samochodem)
- [1. Opis działania aplikacji](#1-opis-działania-aplikacji)
- [2. Funkcje aplikacji](#2-funkcje-aplikacji)
- [3. Uruchamianie aplikacji](#3-uruchamianie-aplikacji)
  - [3.1 Aplikacja konsolowa](#31-aplikacja-konsolowa)
  - [3.2 Aplikacja desktopowa](#32-aplikacja-desktopowa)
  - [3.3 Aplikacja webowa](#33-aplikacja-webowa)
  - [3.4 Aplikacja mobilna](#34-aplikacja-mobilna)
- [4. Zasady działania](#4-zasady-działania)
- [5. Testy](#5-testy)


## 1. Opis działania aplikacji

Aplikacja służy do symulowania podstawowego sterowania samochodem.

Użytkownik może utworzyć samochód, podając jego model, rok produkcji, wagę, ilość paliwa, pojemność baku oraz spalanie.

Aplikacja posiada kilka wersji:

- aplikacja konsolowa została napisana w języku Python,
- aplikacja desktopowa została napisana w języku Python z użyciem biblioteki Tkinter,
- aplikacja webowa została napisana w React + Vite + JavaScript,
- aplikacja mobilna została napisana w języku Kotlin z użyciem Jetpack Compose w Android Studio.


## 2. Funkcje aplikacji

Aplikacja pozwala na:

1. Utworzenie samochodu.

2. Podanie podstawowych informacji o samochodzie:
   - model,
   - rok produkcji,
   - waga,
   - ilość paliwa,
   - pojemność baku,
   - spalanie.

3. Włączenie silnika.

4. Włączenie świateł.

5. Uruchomienie trybu jazdy.

6. Przyspieszanie samochodu.

7. Hamowanie samochodu.

8. Skręcanie w lewo i w prawo.

9. Obliczanie przejechanego dystansu.

10. Obliczanie zużycia paliwa.

11. Tankowanie samochodu.

12. Wyświetlanie aktualnej ilości paliwa.

13. Zatrzymanie trybu jazdy.


## 3. Uruchamianie aplikacji


## 3.1 Aplikacja konsolowa

Aby uruchomić aplikację konsolową należy wejść w edytor, np. Visual Studio Code.

Następnie należy wejść do folderu:

```bash
aplikacja_konsolowa
````

Wybrać plik odpowiedzialny za aplikację i uruchomić go przyciskiem **Run** lub klawiszem **F5**.

## 3.2 Aplikacja desktopowa

Aby uruchomić aplikację desktopową należy wejść w edytor, np. Visual Studio Code.

Następnie należy wejść do folderu:

```bash
aplikacja_desktopowa
```

Wybrać plik aplikacji i uruchomić go przyciskiem **Run** lub klawiszem **F5**.

## 3.3 Aplikacja webowa

Aby uruchomić aplikację webową należy wejść do katalogu:

```bash
aplikacja_webowa
```

Następnie należy wpisać w terminalu:

```bash
npm install
```

Po zainstalowaniu wymaganych paczek należy uruchomić aplikację:

```bash
npm run dev
```

Po uruchomieniu pojawi się adres localhost.

Należy kliknąć w podany link przytrzymując klawisz **Ctrl** lub skopiować adres i wkleić go do przeglądarki.

## 3.4 Aplikacja mobilna

Aby uruchomić aplikację mobilną należy otworzyć projekt w programie **Android Studio**.

Następnie należy uruchomić emulator Androida.

Po uruchomieniu emulatora należy odnaleźć plik:

```text
MainActivity.kt
```

i uruchomić aplikację przyciskiem **Run**.

Aplikacja zostanie uruchomiona na emulatorze.

## 4. Zasady działania

Aby rozpocząć jazdę samochodem należy najpierw:

1. Utworzyć samochód.

2. Włączyć silnik.

3. Włączyć światła.

4. Uruchomić tryb jazdy.

Dopiero po uruchomieniu trybu jazdy można:

* zwiększać prędkość,
* hamować,
* skręcać.

Bez uruchomionego trybu jazdy aplikacja wyświetla odpowiedni komunikat.

Tankowanie samochodu jest możliwe tylko wtedy, gdy samochód nie znajduje się w trybie jazdy.

Jeżeli zabraknie paliwa podczas jazdy, samochód zatrzymuje się, a silnik zostaje wyłączony.

Samochód posiada maksymalną prędkość 250 km/h.

## 5. Testy

Testy zostały wykonane w celu sprawdzenia poprawnego działania najważniejszych funkcji aplikacji.

Sprawdzono między innymi:

* tworzenie samochodu,
* sprawdzanie poprawności danych,
* włączanie silnika,
* włączanie świateł,
* uruchamianie trybu jazdy,
* przyspieszanie,
* hamowanie,
* skręcanie,
* zużywanie paliwa podczas jazdy,
* zatrzymanie samochodu po skończeniu paliwa,
* tankowanie samochodu,
* blokadę tankowania podczas jazdy,
* blokadę przyspieszania bez uruchomionego trybu jazdy,
* blokadę hamowania bez uruchomionego trybu jazdy,
* blokadę skręcania bez uruchomionego trybu jazdy.

```
