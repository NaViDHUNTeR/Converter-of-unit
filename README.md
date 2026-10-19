# Unit & Currency Converter
#### Video Demo: < https://youtu.be/QaN302aFa-g >
#### Description:

## Where the Idea Came From
The idea for the "Unit & Currency Converter" came from a common, everyday need: having a fast, reliable, and distraction-free tool for standard conversions. Whether you are following a cooking recipe that uses Fahrenheit, working on an assignment that requires metric units, or planning a trip and needing to check exchange rates, you often have to open a web browser. I wanted to build a lightweight Command Line Interface (CLI) application that does all of this instantly, right from the terminal, without the need for an internet connection (except for live currencies).

## How It Works
The program is built entirely in Python. When you run `Converter_Of_Unit.py`, a simple text-based menu appears on the screen, asking you to choose one of three main options:

1. **Temperature Converter:** Allows you to convert temperatures between Celsius, Fahrenheit, and Kelvin. It takes your input, converts it to a base unit (Celsius), and then calculates the final requested unit.
2. **Length Converter:** Converts distances between Meters, Kilometers, Miles, and Feet. It uses a mathematical dictionary to reliably map out all conversion rates.
3. **Currency Converter:** This is the most dynamic part of the program. It uses the `requests` library to communicate with a free online API. It fetches the latest, real-time exchange rates and accurately converts your money from one currency to another.

### Code Structure
To follow best programming practices, the core logic is separated from the user interface. The `main()` function is only responsible for taking user input, displaying menus, and fetching API data. The actual calculations happen inside three independent functions: `convert_temperature`, `convert_length`, and `convert_currency`.

Because these functions are isolated and return specific values instead of just printing them, we can easily and automatically test them. The `test_Converter_Of_Unit.py` file uses `pytest` to check these functions under various conditions, ensuring our math and logic are always 100% correct.
