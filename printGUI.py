# gui_utils.py
def gui_print(message):
    print(message)  # default (CLI mode)

def set_gui_callback(callback):
    global gui_print
    gui_print = callback
