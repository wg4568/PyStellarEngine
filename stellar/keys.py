import pygame

def pushed_check(pushed, events):
	for index in range(0, len(pushed)-1):
		pushed[index]=False
	for event in events:
		if event.type == pygame.KEYDOWN:
			pushed[event.key] = True

	mouse = [False] * 3
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse[0] = True
			if event.button == 3:
				mouse[1] = True
			if event.button == 2:
				mouse[2] = True
			
	pushed[M_1]=mouse[0]
	pushed[M_2]=mouse[1]
	pushed[M_3]=mouse[2]
	return pushed

def released_check(released, events):
	for index in range(0,len(released)-1):
		released[index]=False
	for event in events:
		if event.type == pygame.KEYUP:
			released[event.key] = True
	mouse = [False] * 3
	for event in events:
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				mouse[0] = True
			if event.button == 3:
				mouse[1] = True
			if event.button == 2:
				mouse[2] = True

	released[M_1] = mouse[0]
	released[M_2] = mouse[1]
	released[M_3] = mouse[2]  
	return released

def held_check(held, released, pushed):
	for index in range(0,len(held)-1):
		if not held[index]:
			if pushed[index]:
				held[index] = True
		else:
			if released[index]:
				held[index] = False
	return held
			
			
def control_check(held, pushed, released,events):
	pushed = pushed_check(pushed,events)
	released = released_check(released,events)
	held = held_check(held,released,pushed)
	return [held, pushed, released]

S_HELD = 0
S_PUSHED = 1
S_RELEASED = 2

K_BACKSPACE = 8
K_TAB = 9
K_CLEAR = 12
K_RETURN = 13
K_PAUSE = 19
K_ESCAPE = 27
K_SPACE = 32
K_EXCLAIM = 33
K_QUOTEDBL = 34
K_HASH = 35
K_DOLLAR = 36
K_AMPERSAND = 38
K_QUOTE = 39
K_LEFTPAREN = 40
K_RIGHTPAREN = 41
K_ASTERISK = 42
K_PLUS = 43
K_COMMA = 44
K_MINUS = 45
K_PERIOD = 46
K_SLASH = 47
K_0 = 48
K_1 = 49
K_2 = 50
K_3 = 51
K_4 = 52
K_5 = 53
K_6 = 54
K_7 = 55
K_8 = 56
K_9 = 57
K_COLON = 58
K_SEMICOLON = 59
K_LESS = 60
K_EQUALS = 61
K_GREATER = 62
K_QUESTION = 63
K_AT = 64
K_LEFTBRACKET = 91
K_BACKSLASH = 92
K_RIGHTBRACKET = 93
K_CARET = 94
K_UNDERSCORE = 95
K_BACKQUOTE = 96
K_a = 97
K_b = 98
K_c = 99
K_d = 100
K_e = 101
K_f = 102
K_g = 103
K_h = 104
K_i = 105
K_j = 106
K_k = 107
K_l = 108
K_m = 109
K_n = 110
K_o = 111
K_p = 112
K_q = 113
K_r = 114
K_s = 115
K_t = 116
K_u = 117
K_v = 118
K_w = 119
K_x = 120
K_y = 121
K_z = 122
K_DELETE = 127
K_KP0 = 256
K_KP1 = 257
K_KP2 = 258
K_KP3 = 259
K_KP4 = 260
K_KP5 = 261
K_KP6 = 262
K_KP7 = 263
K_KP8 = 264
K_KP9 = 265
K_KP_PERIOD = 266
K_KP_DIVIDE = 267
K_KP_MULTIPLY = 268
K_KP_MINUS = 269
K_KP_PLUS = 270
K_KP_ENTER = 271
K_KP_EQUALS = 272
K_UP = 273
K_DOWN = 274
K_RIGHT = 275
K_LEFT = 276
K_INSERT = 277
K_HOME = 278
K_END = 279
K_PAGEUP = 280
K_PAGEDOWN = 281
K_F1 = 282
K_F2 = 283
K_F3 = 284
K_F4 = 285
K_F5 = 286
K_F6 = 287
K_F7 = 288
K_F8 = 289
K_F9 = 290
K_F10 = 291
K_F11 = 292
K_F12 = 293
K_F13 = 294
K_F14 = 295
K_F15 = 296
K_NUMLOCK = 300
K_CAPSLOCK = 301
K_SCROLLOCK = 302
K_RSHIFT = 303
K_LSHIFT = 304
K_RCTRL = 305
K_LCTRL = 306
K_RALT = 307
K_LALT = 308
K_RMETA = 309
K_LMETA = 310
K_LSUPER = 311
K_RSUPER = 312
K_MODE = 313
K_HELP = 315
K_PRINT = 316
K_SYSREQ = 317
K_BREAK = 318
K_MENU = 319
K_POWER = 320
K_EURO = 321
M_1 = 323
M_2 = 324
M_3 = 325
