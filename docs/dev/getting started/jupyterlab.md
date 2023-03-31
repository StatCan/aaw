# Jupyterlab

This file is to detail any extra intricacies or features our jupyterlab-xyz offerings have that are non-obvious


## Concurrency in Jupyterlab Notebooks

The same jupyterlab notebook can be open on two separate windows and can maintain a certain amount of independence from each other. Keystrokes or mouse movements are not mirrored, as in if in one window the user moves the mouse around the second window's mouse will not move. They of course share the exact same file system and when a file is created in one window, that created file will eventually appear as available in the other window. 


### Opening a new terminal in a second window
Upon initially opening up a second window, the user will be shown whatever is open on the first window. They can open up their own `terminal` and perform tasks independent of whatever is happening in the first window. Note that this second terminal opened up in the second window will not be shown in the first window. If in the first window you open up a terminal the terminal number will just increment up by one and be its own session.

### "Shared" terminals upon first startup
As mentioned above if the user opens up a notebook in a second window they will be shown whatever is open in the first window. If either the first or second window closes the shared terminal that was mirrored, that terminal will close on the other window.

### Python notebooks
These interact the same way as the terminal above. User A can make changes to the .ipynb, but they wont be reflected in User B until User A saves, and then User B reopens the .ipynb

### VsCode
Actions taken in vscode are mirrored and matches up to the most recent state of the file. Given the following setup you will observe the following;
User A creates a text file (either on vscode or through the terminal). 
User B opens that text file and leaves it open
User A makes changes to the created text file and saves
User B will see changes to the text file reflected on their vscode session. 


### Saving files in conflict
Both window instances can save to the same file, however if it is in conflict you will get the following image
![image](https://user-images.githubusercontent.com/23174198/227596318-7df6e6c0-d22d-4345-ac59-d25cdc729fc8.png)
However, vscode behaves differently. vscode will take whatever is on that session and save over it with no prompt asking about the file difference.

