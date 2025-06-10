print("Convertisseur de température")
print("1. Convertir de Celsius vers Fahrenheit")
print("2. Convertir de Fahrenheit vers Celsius")

choix = input("Choisissez une option 1 ou 2: ")

if choix == '1':
    celsius = float(input("Entrez la température en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif choix == '2':
    fahrenheit = float(input("Entrez la température en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Option invalide . veuillez choisir entre 1 et 2")

