def convertCurrency(value: float , fromcurrency: str, tocurrency:str):
    currencyBase = {
        "BRL": {"BRL": 1, "USD": 0.17, "EUR": 0.15},
        "USD": {"BRL": 5.75, "USD": 1, "EUR": 0.91},
        "EUR": {"BRL":6.26, "USD": 1.08, "EUR": 1}
    }

    conversionRate = currencyBase[fromcurrency][tocurrency]

    return float(f"{(value * conversionRate):.2f}")

def convertEnergy(value: float, fromUnit: str, toUnit: str):
    energyBase = {
        "joule": {"joule": 1, "calory": 0.2388, "kilowatt": 2.778 * (10**(-7))},
        "calory": {"joule": 4.187, "calory": 1, "kilowatt": 1.163* (10**(-6))},
        "kilowatt": {"joule": 3.6 * (10**6), "calory": 8.598 * (10**5), "kilowatt": 1}
    }   

    conversionRate = energyBase[fromUnit][toUnit]

    return float(f"{(value * conversionRate):.2f}")

def converttemperature(value: float, fromUnit: str, toUnit: str):
    temperatureBase = {
        "celsius": {"celsius": 1, "kelvin": 274.15, "fahrenheit": 33.80},
        "kelvin": {"celsius": -272.15, "kelvin": 1, "fahrenheit": -457.87},
        "fahrenheit": {"celsius": -17.22, "kelvin": 255.93, "fahrenheit": 1}
    }

    conversionRate = temperatureBase[fromUnit][toUnit]

    return float(f"{(value * conversionRate):.2f}")