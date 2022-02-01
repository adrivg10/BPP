import random
import pdb
#pdb.set_trace() -> descomentar para pdb
list1 = [[(j+1)*random.randint(-10, 10) for j in range(random.randint(3, 6))] for i in range(random.randint(4, 7))]
resultado1 = [max(i) for i in list1]
print(f"los numeros maximos de la lista {list1} son: {resultado1}")


list2 = [(i+1)*random.randint(1, 100) for i in range(random.randint(5, 15))]


def es_primo(n):
    primo = True
    for i in range(2, n):
        if (n % i == 0):
            primo = False
    return primo


resultado2 = list(filter(es_primo, list2))
if (len(resultado2) < 1):
    print("No hay numeros primos en: ", list2)
else:
    print(f"Los números primos de la lista: {list2} son: {resultado2}")
