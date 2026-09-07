

def capitalize_first_letter(string: str) -> str:
    conver_list = string.split()
    return conver_list 
    

print(capitalize_first_letter("porque no me haces caso"))














"""Este ejercicio (kata) te pide hacer lo siguiente:

Si un número que te dan es par (es decir, divisible por 2, como 2, 4, 6, 8...), tienes que multiplicarlo por 8.

Pero si el número es impar (como 1, 3, 5, 7...), tienes que multiplicarlo por 9."""


def multiply_odd_even(number: int) -> int:
    return number * 8 if number % 2 == 0 else number * 9
















"""" Crear una función que reciba dos números:

num: el número del que quieres obtener múltiplos.

length: la cantidad de múltiplos que debe tener la lista.

La función debe devolver una lista de múltiplos de num, con exactamente length elementos."""


def multiples(num: int, length: int) -> list:
    return [num * i for i in range(1, length + 1, 1)]















"""You are given two numbers a and b. Create a function that returns the next
number greater than a and b and divisible by b.

Examples
divisible_by_b(17, 8) ➞ 24

divisible_by_b(98, 3) ➞ 99

divisible_by_b(14, 11) ➞ 22"""

def divisible_by_b(a: int, b: int) -> int:
    return b * ((a // b) + 1) if a % b != 0 else a + b









# Create a function that takes two number strings and returns their sum as a string.
# add("111", "111") ➞ "222"
# add("10", "80") ➞ "90"
# add("", "20") ➞ "Invalid Operation"

def sumNumber(Num1: str, Num2: str) -> str:
    if isinstance(Num1, str) and isinstance(Num2, str):
        return int(Num1) + int(Num2) if Num1.isdigit() and Num2.isdigit() else "Invalid Operation"
     