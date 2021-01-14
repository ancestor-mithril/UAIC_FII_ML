# Problema 34 / 505

 * [main.py](https://github.com/ancestor-mithril/UAIC_FII_ML/blob/master/Lab/tema_2/script_p_34/main.py) = entty point-ul

## Pregatirea mediului de lucru

`Python3.7`, folosind bibliotecile `numpy` si `scipy`
  * pot fi instalate folosind:
  ```
  conda install numpy
  conda install -c anaconda scipy
  ```
  * sau
  ```
  pip install numpy
  pip install scipy
  ```

## Rulare

In directorul curent:
```
python.exe main.py
```
 
## Input: 
 * pe primele 2 linii: `m` si `n`, iar pe a treia linii `n` perechi separate prin spatii, fiecare pereche continand `m` numere separate prin virgule intre paranteze patrate
***

  **Exemplu**
```
2
2
[2,2] [3,2]
 ```
 
## Output:
 * `root_partitions`, `root_entropy`, `partitions_entropy`, `root_conditional_entropy`, `IG_root_partitions `
***

  * `root_partitions` = radacina compasului de decizie citit
    * se insumeaza pe fiecare valoare toate partitiile citite pentru a se obtine radacina
  * `root_entropy` = entropia radacinei
    * codul comentat din `get_entropy_of_partition` reprezinta calculul entropiei dupa formula, care da acelasi rezultat (dar mai lent) ca al aplicarii `scipy.special.entropy`
  * `partitions_entropy` = entropia fiecarui din cele `n` partitii citite
  * `root_conditional_entropy` = entropia conditionala medie a radacinei
    * se calculeaza conform formulei
  * `IG_root_partitions ` = castigul de informatiei al radacinei daca stim partitiile
