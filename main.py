def text_to_morse(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v",
               "w", "x", "y", "z"]
    morse = ["·- ", "-·· ", "-·-· ", "-·· ", "· ", "··-· ", "--· ", "···· ", "·· ", "·--- ", "-·- ", "·-·· ", "-- ",
             "-· ", "--- ", "·--· ", "--·- ", "·-· ", "··· ", "- ", "··- ", "···- ", "·-- ", "-··- ", "-·-- ", "--·· "]
    morse_text = ""
    for letter in text:
        morse_index = letters.index(letter)
        morse_text += morse[morse_index]
    return morse_text


word = input("Word: ")
print(f"Morse: {text_to_morse(word.lower())}")
