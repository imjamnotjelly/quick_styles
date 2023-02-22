from os import system
from time import strftime

system("")

color_codes = {
    # color:(fg, bg)
    "black": (30, 40),
    "red": (31, 41),
    "green": (32, 42),
    "yellow": (33, 43),
    "blue": (34, 44),
    "magenta": (35, 45),
    "cyan": (36, 46),
    "lightgray": (37, 47),
    "gray": (90, 100),
    "lightred": (91, 101),
    "lightgreen": (92, 102),
    "lightyellow": (93, 43),
    "lightblue": (94, 104),
    "lightmagenta": (95, 105),
    "lightcyan": (96, 106),
    "white": (97, 107),
}

style_codes = {
    "bold": 1,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "strikethrough": 9,
}

modifiers = {

}

custom_codes = {

}


def create_code(str, **kwargs):
    values = []

    # foreground colors
    try:
        color = kwargs["color"]
    except KeyError:
        pass
    else:
        values.append(color_codes[color][0])

    # background colors
    try:
        bgcolor = kwargs["bgcolor"]
    except KeyError:
        pass
    else:
        values.append(color_codes[bgcolor][1])

    # text styles
    try:
        styles = kwargs["styles"]
    except KeyError:
        pass
    else:
        if isinstance(styles, str):
            styles = [styles]
        styles = list(map(lambda x: style_codes[x], styles))
        values.extend(styles)

    values = list(map(lambda x: str(x), values))
    ansi_code = f"\033[{';'.join(sorted(values))}mLorem ipsum dolor sit amet"
    return ansi_code


print(create_code())
