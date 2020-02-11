def resta(x, y):
    return x - y

res = resta(5, 3)
print(res)

def divide(x, y):
    return x/y

res = divide(5, 3)
print(res)
"""print(divide(5,3))"""

def divide2(x=10, y=5):
    return x/y

print(divide2())
print(divide2(1))
print(divide2(1,2))

def cuenta(listado):
    return len(listado)

prueba = ["Pikachu", "Charizard", "Venusar", "Blastoise"]
print(cuenta(prueba))

from csv import reader

def leerFichero(pokemon):
    dataset = list()
    invalid_lines = 0
    with open(pokemon, 'r') as file:
        leido = reader(file)
        for col in leido:
            if not col:
                invalid_lines += 1
                continue
            dataset.append(col)
    return (dataset, invalid_lines)

(dataset,lineas_invalidas) = leerFichero('pokemon.csv')
print("Lineas validas: ",len(dataset))
print("Líneas inválidas",lineas_invalidas)
print(dataset)