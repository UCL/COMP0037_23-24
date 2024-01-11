## About

This repository contains lab exercises for the [COMP0037 Robotic Systems](https://moodle.ucl.ac.uk/course/view.php?id=33669&section=0) module for taught MSc students at UCL, delivered in Spring 2024. Exercises are designed to be attempted in the on-campus lab sessions on Friday afternoon, though you are free to do additional work in your own time if you wish.

Lab attendance will be monitored, but the exercises are **not graded**. You are welcome to discuss and help each other with these tasks and to ask for assistance and clarification from the TAs, but there is nothing to be gained by simply copying each others' work.

## Install basic software (before start of term)

* Install [Git](https://git-scm.com) (if you don't already have it).
* Install [Python 3](https://www.python.org/downloads/) (if you don't already have it).
* Install [Ghostscript](https://ghostscript.com/index.html). For Windows, use the [64-bit binary AGPL release](https://ghostscript.com/releases/gsdnld.html). For Mac, use home brew and run ``brew install ghostscript``. For Linux, use ``apt install ghostscript``, ``snap install code --classic`` (or your preferred package manager).

In addition we highly recommend using Visual Studio code:

* Download [Visual Studio Code](https://code.visualstudio.com/), an easy-to-use editor
* Install the [Python Plugin](https://code.visualstudio.com/docs/python/python-tutorial/) and test the hello world example

## Install software to support this module

* Download the material from GitHub: [COMP0037 Robotic Systems](https://github.com/UCL/COMP0037_23-24) and put the lab material in a folder named, for example, "comp0037-labs":
    ```
    mkdir comp0037-labs
    cd comp0037-labs
    git clone https://github.com/UCL/COMP0037_23-24.git
    ```
* Open the cloned folder in Visual Studio Code: File > Open Folder > select the cloned repository folder
* Open a new terminal in Visual Studio Code and make sure you are in the folder 'comp0037-labs'
* Create and activate a virtual environment:
    ```
    python3 -m venv comp0037-venv
    # On Unix/MacOS:
    source comp0037-venv/bin/activate
    # On Windows:
    .\comp0037-venv\Scripts\activate
    # Upgrade pip:
    python -m pip install --upgrade pip
    ```
     If you get the error "python3 : The term 'python3' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again", try using:
    ```
    python -m venv comp0037-venv
    ```
    If you are encountering issues, you can create a conda environment
    ```
    conda create -n comp0037-venv python=3.9 -y
    conda activate comp0037-venv
    ```
* Install the Python package requirements:
    ```sh
    pip install -r requirements-1.txt
    ```
    In case packages are missing, you can just run
    ```sh
    pip install _package_
    ```

* Select the Python interpreter. If you do not do this, then none of the packages you just installed will be recognized. There are the "easy" instructions (which did not work for me, version 1.85.1) and the harder ones.
    
* Easier: On the bottom left of you VS Code window you should see a "Select Interpreter" button:
    * Click on the button
    * Select "Enter interpreter path..."
    * Select "Find..."
        * Go to your virtual environment folder in ```comp0037-venv``` > Scripts > python.exe > Select Interpreter (Windows) 
        * Go to your virtual environment folder in ```comp0037-venv``` > bin > python.exe (or just python if you don't see the .exe extension)> Select Interpreter (Unix/MacOS) 
    * Instead of "Select Interpreter" you should now see "3.x.x('comp0037-venv':venv) or similar
 
* Harder: Press <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>
    * In the dialogue box type ```python: select interpreter```
    * Use the file browser (which might open _behind_ the edit screen), navigate to the ```comp0037-venv``` directory and select ```bin/python```
    * There is no visual update ot say the interpreter has worked but the dependencies seem to be in place.
