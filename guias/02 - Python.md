Python
===

Python Version and Interpreter
---

It's quite easy to check the version of Python installed on your system. For example, in the Windows Operating System simply access a terminal window, then at the command prompt type: `python -V` and press the return key. If you have multiple versions of python installed on your system or python 3 you may need to type either `py -3 -V` or `python3 -V` depending upon your operating system.

```bash
$ python -V

$ py -3 -V

$ python3 -V
```

Hello World
---

1. Type the appropriate python command to start the interpreter. For example, in Windows you would type python then press the return key.
2. Type `print("Hello World! How are you?")` and press the return key.
3. When you are done, to exit the interpreter type `quit()` and press the Enter key

Python scripts
---

A Python script is just a text file that has two essential characteristics:

1. The script contains the required Python syntax. For example, I could write in a file `print("I'm a Python script!")` and save it. This would almost make this file a Python script because the function `print` is a built-in Python function and I'm using the required Python syntax to call the function. More on that later.
2. The script ends with a `.py`. For example, if I named a script `myscript.txt` it would not be a python script because the name does not end with a `.py`. To make it a python script I would have to rename it `myscript.py`.

To run a Python script is quite simple. For example in the Windows Operating System access a terminal window command prompt and type python followed by the full name of the python script and press the return key. If you are not at the directory where the python script resides you will have to specify the full directory location of the script followed by the name of the script.

```bash
$ python script.py
```

### Primer script

Vamos a escribir nuestro primer script de Python. El mismo contiene varios componentes que vamos a desarrollar sobre este curso. Por ahora, solo copiaremos el script que aparece a continuación y lo correremos. 

**Recomendación:** Intente escribir el codigo en el editor de texto en vez de copiarlo para empezar a acostumbrarse a escibir codigo.

#### Instrucciones

1. Ir al archivo `codes/01-primer-script.py`.
2. Copiar o redactar el siguiente contenido dentro del archivo:

```python
""" 01 - Primer script """

from helpers import curry

COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'blue': '\033[94m',
    'endc': '\033[0m'
}

def puts(text, color='green'):
    """ Prints to the console with colors if the color is defined. """
    if COLORS.get(color):
        print(COLORS[color] + text + COLORS['endc'] + '\n')
    else:
        print(text + '\n')

red = curry(puts, 'red')
blue = curry(puts, 'blue')

# Add a new line
print()

red("CONATEL S.A.")
puts("Devnet express.")
blue("Cisco .:|:.:|:.")
```
