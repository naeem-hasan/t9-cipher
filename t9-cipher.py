class T9Text(object):
    _keys = {
        '2': "abc", '3': "def",
        '4': "ghi", '5': "jkl", '6': "mno",
        '7': "pqrs", '8': "tuv", '9': "wxyz",
        '0': " "
    }

    def __init__(self, text):
        assert type(text) is str, "Requires a string!"
        self.text = text.lower()

    def to_keystrokes(self, special_char=False):
        assert self._has_num(self.text), "Requires a numberless string!"
        return self._make_keypad(self.text, special_char)

    def to_text(self, special_char=False):
        return self._make_text(self.text, special_char)

    def _make_keypad(self, text, special_char):
        keypad_strokes = []
        for i in text:
            strokes = self._to_stroke(i, special_char)
            if strokes:
                keypad_strokes.append(strokes)

        return " ".join(keypad_strokes)

    def _to_stroke(self, char, special_char):
        for i in self._keys:
            if char in self._keys[i]:
                return i * (self._keys[i].find(char) + 1)
        if special_char:
            return char
        return None

    def _make_text(self, keypad_strokes, special_char):
        text = ""
        for i in keypad_strokes.split():
            char = self._to_char(i, special_char)
            if char:
                text += char

        return text

    def _to_char(self, strokes, special_char):
        try:
            return self._keys[strokes[0]][len(strokes) - 1]
        except KeyError:
            if special_char:
                return strokes
        return None

    def _has_num(self, text):
        return not any(char.isdigit() for char in text)

    def __str__(self):
        return self.text


def run_test():
    text = "Happy Valentine's Day!"
    keypad = T9Text(text)
    print "Text: %s" % text
    print "To keystrokes: %s" % keypad.to_keystrokes()
    print "To keystrokes with special characters: %s" % keypad.to_keystrokes(True)
    print ""
    strokes = "555 666 888 33 0 999 666 88"
    keypad = T9Text(strokes)
    print "Strokes: %s" % strokes
    print "To text: %s" % keypad.to_text()
    print "To text with special characters: %s" % keypad.to_text(True)

if __name__ == '__main__':
    run_test()
