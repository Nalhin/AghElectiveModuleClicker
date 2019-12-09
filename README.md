# AGH Elective Module Clicker

This app automates the process of choosing elective modules.

#### Installation

```bash
git clone https://github.com/Nalhin/AghElectiveModuleClicker
pacman -S firefox
pip install selenium
yay -S geckodriver
```

You also need to create config.json file with the following structure.

```json
{
  "login": "your_login",
  "password": "your_password",
  "partial_module_names": [
    "partial_module_name",
    "partial_module_name"
  ],
  "time": "hour:minute:second"
}
```

####  Start

```bash
cd AghElectiveModuleClicker
python clicker.py 
```
