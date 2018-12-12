# coding=utf-8


def particionar_texto(texto, n):
    palabras = texto.split()
    cant_caracteres = [len(i) + 1 for i in palabras]
    cant_caracteres[0] -= 1


particionar_texto("el viajar es un placer que nos suele suceder", 10)
