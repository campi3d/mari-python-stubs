# Python Stubs for Mari & Mari Extension Pack

This folder contains **statically generated Python stub files (`.pyi`)** for the `mari()` API.  

The stubs can be found build against different Mari Versions at https://github.com/campi3d/mari-python-stubs<br>
Each folder name includes the **Mari version** and the **Mari Extension Pack version** 
used to generate the stubs, making it easier to match them to your local installation.

These stubs provide:

- IDE auto-completion  
- limited Type hints  

when writing Python tools for Mari.

---

## Using the stubs in your IDE

To enable code completion and type checking, you must add the stub folder to your IDE’s Python analysis paths.

The stub folder is the one that directly contains the folder with the `.pyi` files.

---

## Visual Studio Code

1. Open **Settings**
2. Search for **Python: Analysis Extra Paths**
3. Add the path to the stub folder, for example:
4. Reload VS Code

The `mari` module will now provide full autocomplete and type hints.

---

## PyCharm

PyCharm requires **two steps**:  
the folder must be added to the interpreter **and** marked as a **Source Root**.

### 1. Add the stub folder to the interpreter

1. Open **Settings → Project → Python Interpreter**
2. Click the ⚙️ icon → **Show All**
3. Select your interpreter → **Paths** (the hierarchy icon)
4. Click **Add** and select the stub folder  
5. Click **OK** → **Apply**

### 2. Mark the folder as a Source Root

1. In the **Project** panel, locate the stub folder
2. Right-click the folder  
3. Select **Mark Directory As → Sources Root**

This step is required or PyCharm will not index the `.pyi` files for code completion.

After this, `import mari` will have full autocompletion and typing support.

---

## Regenerating the Python stubs

If you have **Mari Extension Pack 6 R4 or newer**, you can regenerate the stubs directly from Mari.

Run the following command inside Mari’s Python environment:

```python
mari.ExtensionPack.dev.generatePythonStubs(self, target_directory: str)
```
Example:
```python
mari.ExtensionPack.dev.generatePythonStubs(
    self,
    "D:/mari_stubs/Mari_75v2_ExtensionPack_6R4"
)
```

This will generate a complete, up-to-date set of .pyi files for the mari() API in the specified directory.
