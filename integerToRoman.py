# 2do Examen Parcial - 22 de Octubre del 2021
# INSTRUCCIONES: Given an integer, convert it to a roman numeral.

def integerToRoman(integer):
    dictionary = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D",
                  1000: "M"}

    divisor = 10 ** (len(str(integer)) - 1)
    romanNumeral = []

    while integer:
        number = int(integer / divisor)
        if number <= 3:
            romanNumeral.append(dictionary[divisor] * number)
        elif number == 4:
            romanNumeral.append(dictionary[divisor] + dictionary[divisor * 5])
        elif number >= 5 and number <= 8:
            romanNumeral.append(dictionary[divisor * 5] +
                                (dictionary[divisor] * (number - 5)))
        elif number == 9:
            romanNumeral.append(dictionary[divisor] +
                                dictionary[divisor * 10])
        else:
            print("Error")
        integer = integer % divisor
        divisor = divisor / 10

    return "El número romano es: " + ''.join(romanNumeral)


# Testing
print("---------------Testing---------------")
numbersToConvert = [9, 36, 445, 509, 1996, 2012]
for integer in numbersToConvert:
    print("Entrada: " + str(integer))
    print(integerToRoman(integer), end="\n \n")
