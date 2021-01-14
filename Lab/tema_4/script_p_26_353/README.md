# Bayes Naiv

Un scurt script care calculeaza probabilitatile conditionate necesare pentru Bayes Naiv

## Pregatirea mediului de lucru
  * `python3` si biblioteca `numpy`
  
## Rulare
```
python.exe main.py
```
### Input
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
### Output
```
{'Green': {'M': 0.6, 'H': 0.2}, 'Legs': {'M': 0.4, 'H': 1.0}, 'Height': {'M': 0.4, 'H': 0.4}, 'Smelly': {'M': 0.4, 'H': 0.4}, 'Species': {'M': 0.5, 'H': 0.5}}
```
