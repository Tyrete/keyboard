import config
import ctypes


def know_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return config.layout[pf(0)]


def change_layout(letter):
    if know_layout() == "rus":
        pos = config.end_layout.find(letter)
        return config.rus_layout[pos]
    return letter


# возможно в таком маленьком проекте это не совсем оправданно,
# но он точно станет больше, поэтому нужно разделять "обязаности", чтобы потом не теряться в объемных файлах
