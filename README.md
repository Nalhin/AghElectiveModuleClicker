#AGH Elective Subject Clicker

This app automates the process of choosing your favourite elective subjects.

#### Installation

```bash
pacman -S firefox
git clone https://github.com/Nalhin/AghElectiveSubjectClicker
pip install selenium
yay -S geckodriver
```

You also need to create data.json file with the following structure

```json
{
  "login": "your_login",
  "password": "your_password",
  "subjects": [
    "partial_subject_names",
    "partial_subject_names"
  ]
}
```

####  Start

```bash
cd AghElectiveSubjectClicker
python clicker.py 
```
