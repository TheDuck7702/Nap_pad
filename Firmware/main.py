import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

col_1 = board.GP02
col_2 = board.GP03
col_3 = board.GP04
col_4 = board.GP05
col_5 = board.GP06
col_6 = board.GP07
col_7 = board.GP08
col_8 = board.GP09


row_1 = board.GP010
row_2 = board.GP011
row_3 = board.GP012
row_4 = board.GP013
row_5 = board.GP014
row_6 = board.GP015
row_7 = board.GP016
row_8 = board.GP017


keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC],
    
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET],
    
    [KC.LCTRL, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER],
    
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT],
    
    [KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.RALT, KC.FN, KC.RGUI, KC.RCTRL]
]

#rotery enodier?


if __name__ == '__main__':
    keyboard.go()