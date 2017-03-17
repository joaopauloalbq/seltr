# Seltr

## Description

Shows GNOME notification window with translation of currently selected text.
Translation is performed using Google-translate service, hence Seltr needs Internet access.

## Seltr script position arguments:

* first <br />
  Language the phrase will be translated to (e.g. ru, en, ja). Default - ru
* second <br />
  Language the phrase will be translated from (or 'auto' if text language should be automatically determined). Default - auto

## Setup

Copy files *seltr* and *seltr.py* to the same directory.

To add a keyboard shortcut in GNOME, go to Configuration->Keyboard. Add new keyboard shortcut here:
* add shortcut name
* add path to seltr script, specify Seltr arguments if necessary
* add desired keyboard shortcut

After these steps, notification window with translation of the selected text should appear when you press defined keyboard shortcut.

## Dependencies

xsel


