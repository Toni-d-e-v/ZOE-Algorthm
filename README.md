# ZOE encryption algorthm

## Introduction
    
ZOE is a algorthm for encrypting and decrypting strings.
Made by special algorithm that use letter maps.
And letter maps are randomized, then we get cordinates of every letter in the map.
Then we can encrypt and decrypt files. by using special json keys which are letter maps.
Example of letter map key:
```
{"lower": 
{"a": "f", "b": "j", "c": "m", "d": "p", "e": "o", "f": "h", "g": "r", "h": "w", "i": "b", "j": "x", "k": "z", "l": "y", "m": "d", "n": "v", "o": "q", "p": "s", "q": "i", "r": "l", "s": "c", "t": "k", "u": "g", "v": "u", "w": "n", "x": "a", "y": "e", "z": "t"
}, 
"upper": {"A": "E", "B": "A", "C": "F", "D": "Y", "E": "K", "F": "T", "G": "B", "H": "C", "I": "W", "J": "I", "K": "G", "L": "S", "M": "X", "N": "N", "O": "R", "P": "D", "Q": "Q", "R": "V", "S": "J", "T": "L", "U": "O", "V": "M", "W": "U", "X": "Z", "Y": "P", "Z": "H"}
}
```
Example of cordinates without encryption:
```
{'H': [0], 'E': [1], 'L': [2, 3], 'O': [4]}
```
And with:
So with key map H = C:
```
{'C': [0], 'K': [1], 'U': [2, 3], 'R': [4]}
```
How is cordinate convert to string?
First cordinate is decoded with key.json after that we will get a pure cordinate like ```{'H': [0], 'E': [1], 'L': [2, 3], 'O': [4]}```
Each letters key present a letter cordinate.
Then we will get a string like ```"HELLO"```
## Usage
This is pure encryption in python you dont need to install anything.
### encrypt
```
python3 main.py -i test -o test.txt -k json.json -e  
```
### decrypt
```
python3 main.py -i test.txt -o test1.txt -k json.json -d ```
