# minipyg
Simple(st) python dependency manager

## Install
```bash
python3 -m pip install minipyg
```
## Prerequisites
You should work inside an activated virtual environment.
## Usage
If you need to install some package, you just run:
```bash
minipyg install <some_package>
```
Uninstalling packages:
```bash
minipyg uninstall <some_package>
```
After pulling an update of your project from git repository, you can update your local dependencies too:
```bash
minipyg update
```
## 'run' command
In `minipig.json` file you can specify a run command that launch your project, for example:
```json
{
    "commands": {
        "run": "python3 manage.py runserver"
    }
}
```
Then running the command:
```bash
minipyg run
```
will automatically update your dependencies and start your project.
