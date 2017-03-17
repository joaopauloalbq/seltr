Shows gnome notification with translation of currently selected text.
Translation is done with google-translate service. Needs internet access.

Seltr and tran.py scripts should be placed in the same directory.

To add a keyboard shortcut in GNOME, go to Configuration->Keyboard, add a keyboard shortcut here. Add shortcut name, add path to seltr script, add key combination. After that, selected text can be translated with the help of created keyboard shortcut.

Deps:
* xsel
* notify-send
* python


