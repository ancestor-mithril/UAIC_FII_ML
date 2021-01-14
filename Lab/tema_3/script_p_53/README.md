# Problema 53/522
Implementare a algoritmului `ID3`

## Pregatirea mediului de lucru
`Python3.7`, folosind bibliotecile `typing`, `numpy`, `scipy`, `pygraphviz`, `PIL`, `subprocess`
  * instalare `numpy` si `scipy`
    * recomandat:
    ```
    conda install numpy
    conda install -c anaconda scipy
    ```
    * sau:
    ```
    pip install numpy
    pip install scipy
    ```
  * `PIL` :
    ```
    conda install -c anaconda pillow
    ```
    ```
    pip install Pillow
    ```
  * `pygraphviz`:
    * instalare (exista si alte variante):
    ```
    conda install -c alubbock pygraphviz
    ```
    * Calea catre fisierul "`dot.exe`" trebuie inclusa in `PATH`
    * in terminalul de Conda al mediului de lucru curent (sau in CMD), trebuie rulata comanda: [(sursa)](https://stackoverflow.com/a/60147201)
    ```
    dot -c
    ```
    
## Rulare
In directorul curent
```
python.exe main.py
```


## Input
In fisierul [train.txt](https://github.com/ancestor-mithril/UAIC_FII_ML/blob/master/Lab/tema_3/script_p_53/train.txt) se afla pe prima linie numele atributelor in format SSV, iar pe urmatoarele randuri cate o instanta de antrenament pe linie, tot in format SSV. Pe ultima coloana se afla intotdeauna atributul de iesire.

### Exemplu
```
Green Legs Height Smelly Species
N 3 S Y M
Y 2 T N M
Y 3 T N M
N 2 S Y M
Y 3 T N M
N 2 T Y H
N 2 S N H
N 2 T N H
Y 2 S N H
N 2 T Y H
```

## Output
Imaginea [decision_tree.png](https://github.com/ancestor-mithril/UAIC_FII_ML/blob/master/Lab/tema_3/script_p_53/img/decision_tree.png), reprezentand arborele de decizie obtinut in urma antrenarii.

### Exemplu
![](https://github.com/ancestor-mithril/UAIC_FII_ML/blob/master/Lab/tema_3/script_p_53/img/decision_tree.png)
***
## Limitatii
  * In varianta actuala, algoritmul nu accepta un input care sa contina valori continue ale atributelor
  * Nu este inca adaptat pentru atribute discrete cu mai multe aparitii (counts)

## Imbunatatiri

Se pot aduce mai multe imbunatatiri algoritmului, avandu-se in vedere un modul pentru parsarea datelor de intrare cu atribute discrete cu mai multe aparitii, introducerea unui modul de testare si predictie pentru valori de test si eventual adaptarea algoritmului pentru a clasifica valori atribute cu valori continue.
