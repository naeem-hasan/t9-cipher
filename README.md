# t9-cipher
A text to T9 keystrokes (and vise versa) generator created with Python.

## Requirements:
* Python

## Usage:
```python
from t9_cipher import T9Text
mytext = T9Text("Hello world")
print mytext.to_keystrokes()
# prints '44 33 555 555 666 0 9 666 777 555 3'

strokes = T9Text("7 2 22 555 666 0 33 7777 222 666 22 2 777")
print keypad.to_text()
# prints 'pablo escobar'
```
Have fun! And feel free to contribute.
