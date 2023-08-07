# Requires
Curses, on Linux pre-installed, on windows you need windows-curses, so you can install it with `pip install windows-curses` \
Or just add to your code:
```python
import ezztui
ezztui.check_curses() # not needed if you are using ezztui 2.0.0 or later, it will check for curses automatically
```

# Use
```
Up-Down Arrow Keys: Move cursor 
Enter: Choose current option 
Backspace: Go back 
```

# Coding

## Print text on center of console
```python
import ezztui
ezztui.center_message("Hello World!") # prints "Hello World!" on the center of the console
ezztui.center_multiline(["Hello", "multiline", "world!"]) # prints "Hello" on the center of the console, then "multiline" on the next line, then "world!" on the next line
```

## Clear console
```python
import ezztui
ezztui.cls() # clears the console with a os.system command
ezztui.softcls() # clears the console with a multiple newline
```
## Menu
### Usage
```python
import ezztui
menu = {
    'First menu':
        {'Function 1': 'ezztui_return_value', # use 'return' also from 2.0.0
         'Function 2': 'ezztui_return_value', # specify a function to be called from 4.0.0
         'Function 3': 'ezztui_return_value',
         'Function 4': 'ezztui_return_value',
         'Function 5': 'ezztui_return_value',
         'Back': 'ezztui_back_value'}, # use 'back' also from 2.0.0

    'Second menu':
        {'Submenu 1': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Function 4': 'ezztui_return_value',
            'Function 5': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 2': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Function 4': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 3': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 4': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Back': 'ezztui_back_value'},

    'No submenu function': 'ezztui_return_value',

    'Third menu':
        {'Function 1': 'ezztui_return_value',
         'Function 2': 'ezztui_return_value',
         'Function 3': 'ezztui_return_value',
         'Function 4': 'ezztui_return_value',
         'Back': 'ezztui_back_value'},

    'Exit':
        {"Exit": 'ezztui_exit_value',
         "Back": 'ezztui_back_value'} # use 'exit' also from 2.0.0
}

print(ezztui.menu(menu)) # prints the menu and returns name of function and path to it in menu, 
                         # You can process this value in your program or add while True (or something else)
```

### Returns
```
['Second menu', 'Submenu 2', 'Function 3']
```