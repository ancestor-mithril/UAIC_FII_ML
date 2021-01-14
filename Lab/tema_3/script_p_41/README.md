# Problema 41/511

## Pregatirea mediului de lucru
`Python3.7`, folosind biblioteca `math`

## Rulare
```
python main.py
```
## Cerinta
  * Avand un nod frunza dintr-un arbore de decizie, a carui output este 0 sau 1, determinati numarul de exemple clasificate gresit in functie de entropia frunzei.
## Input
  * M, numar natural, numarul de instante de antrenament asignate la nodul curemt.
  * H, entropia nodului curent, numar intre 0 si 1
## Output
  * x, numarul mediu de exemple clasificate gresit din total
## Mod de lucru
  * aproximam entropia cu functia `gini`, care apoi este transformata intr-o ecuatie de gradul 2 si determinam cele doua radacini ale ecuatiei. Radacina minima reprezinta probabilitatea aparitiei de date care pot fi clasificate gresit de frunza curenta. 
