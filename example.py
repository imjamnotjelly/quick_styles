import quick_styles as qs

print("Hi there! I'm a boring print statement. By default, I am unable to be styled and my appearance is immutable. "
      "Womp womp!")

print("\033[34mTypically, you would have to manually surround me with ANSI escape codes. Not only is this method of "
      "styling tedious, but also makes the text less readable and does not clearly indicate what styles are being "
      "applied to the person inspecting the code.\033[0m")

qs.cprint("Well, well, what do we have here? I'm a styled print statement as well, but there are no ANSI codes "
          "visible. It's just an additional parameter!", color="blue")

qs.cprint("This works for applying a text style as well!", styles="bold")
qs.cprint("Or multiple...", styles=["bold", "underline"])

qs.cprint("There are also modifiers for the content of the string itself, such as")

qs.cprint("a warning format,", modifier="warning")
# ! a warning format, !

qs.cprint("or prepending the text with the current time!", modifier="time_display")
# [14:19:21] or prepending the text with the current time!
