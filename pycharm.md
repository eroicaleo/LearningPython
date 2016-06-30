
# Emacs mode

## Search and Find
* `Double Shift`: Search anywhere.
* `Alt+F7`: find all usage of a class, method and variable in the project.

## Definition, Declaration and Documentation
* `Alt+Shift+G`：open any classes.
* `Ctrl+Q`: quick documentation.
* `Alt+Period`, `Ctrl+Alt+G`, `Ctrl+left-click`: go to declaration.

## Code Completion
* `Alt+Slash`: auto completion.
* `Alt+Slash, Alt+Slash`: complete the name of a class, and import it for you if
  not yet imported.
* `Shift+F6`: Rename classes, methods and variables across the whole project.
* `Ctrl+Alt+V`: Extract variable refactoring. Here is an example:
  ```python
  print(complex_number.real_part())
  # Highlight the code inside braket and Refractor to
  complex_number_real_part = complex_number.real_part()
  print(complex_number_real_part)
  ```
* `Alt+Shift+P`: If the cursor is between the parentheses of a method call,
  brings up a list of valid parameters. Can be used in code completion pop-up list.

## Compile and Debug
* `Ctrl+Shift+10`: run the code.

## Navigation
* `Alt+Home`: Navigation bar.
* `Ctrl+F12`: Navigate|File Structure, navigate in the currently edited file.
* `Alt+F1`: To quickly select the currently edited element (class, file, method
  or field) in any view.
* `Ctrl+Shift+Backspace`: brings you back to last edited position.
  Navigation | Last Edit Location
* `Alt+Up`, `Alt+Down`: Move between methods.

## View and Windows
* `Alt+0`: show messages.
* `Alt+1`: project tree.
* `Alt+7`：file Structure, like `Ctrl+F12`, but in the left pane.
* `Shift+left-click` or `mid-click` or `Ctrl+F4`: close tabs in the editor and the tool
  windows of IntelliJ.

## Edit
* `Ctrl+Shift+Down`, `Ctrl+Shift+Up`: move a block of codes up and down.
* `Ctrl+Shift+J`: Join two lines.
* `Ctrl+Shift+F7`: quickly highlight the usage of some variables in the current
  file, `F3` and `Shift+F3` to navigate the highlighted usages. `Escape, Escape`
  to remove highlighting. This can highlight multiple variables.
    * place the carat at the `implements` keyword in the class definition, and
      press the combination, and select the desired interface from the list.
* `Alt+Y`: cycle through the clipboard to paste. 
