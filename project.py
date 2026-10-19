import sys
import requests

def main():
    print("Welcome to Unit & Currency Converter")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Currency Converter")

    choice = input("Select an option (1/2/3): ").strip()

    if choice == '1':
        try:
            val = float(input("Enter Value: "))
            from_u = input("From (C, F, K): ").strip().upper()
            to_u = input("To (C, F, K): ").strip().upper()
            result = convert_temperature(val , from_u , to_u)
            print(f"Result: {result:.2f} {to_u}")
        except ValueError:
            sys.exit("Invalid Value")

    elif choice == '2':
        try:
            val = float(input("Enter value: "))
            from_u = input("From (M , KM , MILE , FOOT): ").strip().upper()
            to_u = input("To (M , KM , MILE , FOOT): ").strip().upper()
            result = convert_length(val, from_u, to_u)
            print(f"Result: {result:.4f} {to_u}")
        except ValueError :
            sys.exit("Invalid Value")
    elif choice == '3':
        try :
            val = float(input("Enter amount: "))
            from_c = input("from Currency (e.g , USD , EUR): ").strip().upper()
            to_c = input("To Currency (e.g , EUR , GBP): ").strip().upper()
            response = requests.get(f"https://v6.exchangerate-api.com/v6/b75d4512a0c018793c8446fd/latest/{from_c}")
            if response.status_code == 200:
                rates = response.json().get("conversion_rates", {})
                result = convert_currency(val ,to_c, rates)
                print(f"Result: {result:.2f} {to_c}")
            else :
                sys.exit("Error fetching exchange rates. Check your currency code.")
        except ValueError:
            sys.exit("Invalid Value")
        except requests.RequestException:
            sys.exit("Network error occurred while fetching exchange rates.")
    else :
        sys.exit("Invalid choice. Exiting!")

def convert_temperature(value , from_unit , to_unit):
    to_c = {'C': value, 'F': (value - 32) * 5/9, 'K': value - 273.15 }
    if from_unit not in to_c or to_unit not in to_c:
        raise ValueError("Invalid temperature unit")
    celsius = to_c[from_unit]
    from_c = {'C': celsius, 'F': (celsius * 9/5) + 32, 'K': celsius + 273.15}
    return float(from_c[to_unit])


def convert_length(value , from_unit , to_unit):
    conversion_to_meters = {
        'M': 1.0,
        'KM': 1000.0,
        'MILE': 1609.344,
        'FOOT': 0.3048
    }
    if from_unit not in conversion_to_meters or to_unit not in conversion_to_meters:
        raise ValueError("Invalid length unit")

    meters = value * conversion_to_meters[from_unit]
    return meters / conversion_to_meters[to_unit]

def convert_currency(amount , target_currency , rates_dict):
    if target_currency not in rates_dict:
        raise ValueError(f"Currency {target_currency} not found in exchange rates")
    return amount * rates_dict[target_currency]


if __name__ == "__main__":
    main()
