# t9-cipher
A text to T9 keystrokes (and vise versa) generator.

## Requirements:
* Python

## Usage:
`>>> import t9-cipher`
`>>> t9-cipher.T9Text("Hello world").to_keystrokes() # returns '44 33 555 555 666 0 9 666 777 555 3'`
`>>> t9-cipher.T9Text("555 666 888 33").to_text() # returns 'love'`

Have fun! And feel free to contribute.
