import winsound
import time
def codeMors(in_string):
    CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'}
    out_list=[" "]
    for ch in in_string.upper():
        if ch=="":
            out_list.append("")
        else:
            out_list.append(CODE[ch])
    return out_list

def PlayMorze(in_string):
    unite=100
    dot=(440, unite)
    dash=(220, 3*unite)
    for i in range(len(in_string)):
        if in_string[i] == " ":
            time.sleep(7*unite/1000)
        else:
            for ch in in_string[i]:
                if ch=="-":
                    winsound.Beep(dash[0], dash[1])
                elif ch==".":
                    winsound.Beep(dot[0], dot[1])
            time.sleep(3*unite/1000)

PlayMorze(codeMors("hey"))
