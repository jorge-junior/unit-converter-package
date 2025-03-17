# unit_converter_package

This project is the solution to the code challenge "Criando um Pacote de Processamento de Imagens com Python" from the Bootcamp Suzano - Python Developer from dio.me. The objective of the project is to learn the process of creating packages in python, it is possible to convert 3 different types of data: currencies, energy and temperature. To convert, use the function corresponding to the unit of measurement, pass the value you want to convert, the current unit of measure and the desired unit of measure.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.
```
    pip install minimal_unit_converter
```

## Usage
```
    import minimal_unit_converter.common

    # currencies: BRL, USD, EUR
    minimal_unit_converter.common.convertCurrency(value, currencyOrigin, currencyDesired)

    # unit of measure: joule, calory, kilowatt
    minimal_unit_converter.common.convertEnergy(valor, unitOrigin, unitDesired)

    # unit of measure: celsius, kelvin, fahrenheit
    minimal_unit_converter.common.convertEnergy(valor, unitOrigin, unitDesired)
```

## Author
Jorge Junior

## License
[MIT](https://choosealicense.com/licenses/mit/)