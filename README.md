<img src="https://raw.githubusercontent.com/imjamnotjelly/quick_styles/master/banner.png">

<div align="center">
  <h1>quick_styles</h1>
  <p>An unbelievably lightweight Python library for effortlessly applying ANSI escape color & style codes to Windows CMD and other ANSI-supported terminals</p>
</div>
<br>
<br>

## Description

quick_styles enhances the experience of using the current unintuitive ANSI escape code system for text styling in Python. With quick_styles, you can easily generate ANSI codes with set parameters, save styles for future use, and implement custom codes for personalized styles.

## Download

From PyPI using `pip`:

```shell
pip install quick-styles
```

## Usage

### Example program

Before we proceed to the explict info regarding the library's functionality, here's a preview of the core functions of quick_styles to get a sense of its capabilities:

```python
import quick_styles as qs

print("Hi there! I'm a boring print statement. By default, I am unable to be styled and my appearance is immutable. "
      "Womp womp!")

print("\033[34mTypically, you would have to manually surround me with ANSI escape codes. Not only is this method of "
      "styling tedious, but also makes the text less readable and does not clearly indicate what styles are being "
      "applied to the person inspecting the code.\033[0m")

qs.xprint("Well, well, what do we have here? I'm a styled print statement as well, but there are no ANSI codes "
          "visible. It's just an additional parameter!", color="blue")
ex_input = qs.xinput("This applies to inputs too!")

qs.xprint("This works for applying a text style as well.", styles="bold")
qs.xprint("Or multiple...", styles=["bold", "underline"])

# To apply a particular assortment of styles to multiple strings, you can create custom ANSI codes to apply in the future
qs.custom_codes["red_title"] = qs.create_code(color="black", bgcolor="red", styles="bold")
qs.xprint("Not only do I possess the previously listed styles", custom_code="red_title")
qs.xprint("but I do as well!", custom_code="red_title")

# There are also modifiers for the content of the string itself, such as
qs.xprint("a warning format,", modifier="warning")
# ! a warning format, !

qs.xprint("or prepending the text with the current time!", modifier="time_display")
# [14:19:21] or prepending the text with the current time!

# Default values can also be modified
qs.defaults.values["color"] = "red"
qs.defaults.values["styles"] = "bold"
qs.defaults.values["modifier"] = "warning"

# Subsequent calls without explicit values resort to default values
qs.xprint("I'm styled, yet the parameters aren't directly stated!")

# Specified values override defaults
qs.xprint("I'm still special!", color="green")

# Reset function returns defaults to initial values
qs.defaults.reset()

# Strings can also be styled without being immediately printed
styled_string = qs.style_string("You can't see me...", styles="italic")
```
