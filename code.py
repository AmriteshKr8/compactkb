import board
import keypad
import time
from adafruit_hid.keyboard import Keyboard
import usb_hid
from adafruit_hid.keycode import Keycode
import digitalio

k = keypad.KeyMatrix(
    row_pins=(board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20),
    column_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12),
)
kbd = Keyboard(usb_hid.devices)

layout = [
    Keycode.ESCAPE,Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12,
    Keycode.GRAVE_ACCENT,Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS,
    Keycode.TAB,Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P,Keycode.BACKSPACE,
    Keycode.CAPS_LOCK ,Keycode.CAPS_LOCK ,Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H, Keycode.J, Keycode.K, Keycode.L,Keycode.DELETE,Keycode.ENTER,
    Keycode.SHIFT,Keycode.SHIFT,Keycode.SHIFT,Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N, Keycode.M,Keycode.LEFT_BRACKET,Keycode.RIGHT_BRACKET,Keycode.UP_ARROW,Keycode.BACKSLASH,
    Keycode.CONTROL,Keycode.GUI,Keycode.ALT,Keycode.COMMA,Keycode.PERIOD,Keycode.SPACE,Keycode.SPACE,Keycode.FORWARD_SLASH,Keycode.SEMICOLON,Keycode.QUOTE,Keycode.LEFT_ARROW,Keycode.DOWN_ARROW,Keycode.RIGHT_ARROW
]

while True:
    key_event = k.events.get()
    if key_event:
            if key_event.pressed:
                kbd.press(layout[key_event.key_number])
            else:
                kbd.release(layout[key_event.key_number])

