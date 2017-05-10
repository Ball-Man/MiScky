# UICONTROLLER  
_This documentation is made by Giacomo Aloisi_

### BEFORE YOU READ
---
There are some configurations that needs to be made in order to
use this module.  
I'm going to describe them in the following lines.

### X SERVER
---
You'll need `xorg-server` installed to run this module since it's
a graphic module based on **X**.

You need to run your module that uses this module with an **X** server running.
To do that you need to run:

`startx`

If you want to run your module just after the X server, you'll need to edit
the file `/home/yourUserName/.xinitrc` and add the following line:

`exec python (absolutePathOfYourModule)`

If you want to have no cursors displayed, you need to run:

`startx -- -nocursor`

### MONITOR CONFIGURATIONS
---
If you want to have no black borders along the monitor and if you need
to rotate the display, you'll need to change add some configurations on
the file `/boot/config.txt`  
You'll need to add these lines:

`disable_overscan=1`    _removes black borders_
`display_rotate=3`		_rotate the display of 270 degrees clockwise

### FOLDERS
#### /Fonts
---
Folder that contains all the fonts used by _UIController_

### MODULES

#### \_\_init\_\_.py
---
This is the main program that runs and communicate with the **CORE** to do _UI operations_

#### renderer.py
---
This is the module that creates _Surfaces_ to be rendered, like text, images, etc...

#### types.py
---
This is the module that contains all the _classes_ that are used by _UIController_

These are the following classes:
* **Text**  
    It contains all the informations regarding texts (raw text, font, size, color, etc...)

