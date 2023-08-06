# ReqCheq

### Use this module to automatically verify and install referenced modules you are using in your project. It's a script made to easy the process of first running a program in a fresh environment.

## Instalation

```bash
pip install reqcheq
```

## Usage

```python
from reqcheq import reqcheq
reqcheq()
```

Make a `requirements.txt` next to your main file, from which you are going to call this function.
Each line is an item. It can have 1 or 2 words.

1st word: import name of the module. If install name is equal to import name, you can leave only this single word. (if you `import flask`, you should just add `flask` to your requirements.txt)

2nd word: install name of the module. If your module is imported by a different name than it is installed you add the install name after the 1st word. (if you `import dotenv`, you should add `dotenv python-dotenv` to your requirements.txt)

ReqCheq will then automatically try to import given modules and if it fails, will try to install it with pip (windows) or pip3 (linux).
