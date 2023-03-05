# Teaching FastAPI

This repository has been built on the Windows Operating System and has not been tested on a Linux.

## 1. Setup

### 1.1 Virtual Environment

#### 1.1.1 Create Virtual Environment

When you first use the repository, create the virtual environment.
```
python -m venv ./venv
```

#### 1.1.2 Activate Virtual Environment

Activate the python environment
```shell
# Windows
./venv/Scripts/activate
```

```bash
# Linux
source ./venv/bin/activate
```

#### 1.1.3 Install dependencies

Install the dependencies
```
# Install package
pip install -r requirements.txt -r requirements-dev.txt
```

### 1.2 Pre-commit

Ensure pre-commit is installed
```
pre-commit install
```

## 2 Teardown

### 2.1 Virtual Environment

#### 2.1.1 Deactivate Virtual Environment

Deactivate the python environment
```
deactivate
```

#### 2.1.2 Delete Virtual Environment

Delete the python environment
```shell
# Windows
rm venv
```

```bash
# Linux
rm -rf venv
```

## 3 FAQ

### 3.1 Configuration

On Windows, how do I fix the following error?
`./venv/Scripts/activate : File .\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

See corresponding [StackOverflow post](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl)

In Visual Studio Code:
* Open the repository as a folder
* Hit F1
* Navigate to: `Preferences: Open User Settings (JSON)`
* Ensure that there are no entries for `terminal.integrated.profiles.windows`: delete any that exist.
* Navigate to: `Preferences: Open Workspace Settings (JSON)`
* Add an arbitrary space and then re-save the file
* Reload Visual Studio Code
* "Kill" the old terminal (the bin icon in the top-right of the terminal panel)
* Start a new terminal (Terminal > New Terminal)
* Test this has worked by activating the virtual environment (see instructions above)

### 3.2 Linting

Pre-commit doesn't seem to be checking the code.

This happens when you haven't run `pre-commit install`. See section on pre-commit.
