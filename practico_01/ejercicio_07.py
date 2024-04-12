"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    
    palabra = palabra.lower()
    reverse = palabra[::-1]
    return palabra == reverse
    
# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    longitud = len(palabra)
    if longitud % 2 ==  0:
       return palabra[0:longitud //  2]
    else:
        return palabra[0:(longitud + 1) // 2]

# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
