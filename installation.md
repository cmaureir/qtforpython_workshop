# Install Python

Python can be [downloaded](https://python.org/download) from their
official website for macOS, Linux or Windows.

Use the latest **Python 3** version available.

## macOS

* `pkg` installer, e.g.: [macOS 64-bit installer](https://www.python.org/ftp/python/3.7.2/python-3.7.2-macosx10.9.pkg)
* **Important:** Make sure to add Python to your PATH.

## Windows

* Installer, e.g.: [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe)
* **Important:** Make sure to add Python to your PATH.

## Linux

* You can use your package manager to search and install it (**Recommended**)
 * Debian/Ubuntu: `apt-get install python3`
 * Fedora: `dnf install python3`
 * Arch: `pacman -S python`
* Optionally you can download the source and compile it from scratch.

## Does it work?

* macOS and Linux:
  * Open a terminal and type `python` you should see something like this:
    ```bash
    Python 3.7.2 (default, Jan 10 2019, 23:51:51)
    [GCC 8.2.1 20181127] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
 * **Important:** In some systems you should execute `python3` instead.

* Windows
  * Open `cmd` by typing `WindowsKey + r`, then writing `cmd` and `Enter`.
  * Type `python` or `python3` and you should see something like:
    ```bash
    Python 3.7.2 (default, Jan 10 2019, 23:51:51)
    [GCC 8.2.1 20181127] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

# Install Virtualenv (optional)

It is recommendable to use `virtualenv` to create a separate Python environment
where we can install packages freely, without affecting the installed modules
that are installed in the system.

* Install `virtualenv`
  ```bash
  pip install virtualenv
  ```
* Create a virtual environment:
  ```bash
  virtualenv workshop
  ```
* Activate the virtual environment:
  ```bash
  source workshop/bin/activate
  ```
* Verify where is your python executable. It should be inside the virtual environment.
  ```bash
  which python
  > ~/workshop/bin/python
  ```

# Install PySide6

* Activate your virtual environment (optional)
* Install `PySide6` via pip
  ```bash
  pip install PySide6
  ```
* Execute `python` and try to import the module `import PySide6`, if no error
  appeared, you successfully installed it. Something like this:
  ```python
  >>> import PySide6
  >>>
  ```
