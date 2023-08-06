## Ant Fake

[Github repository](https://github.com/inkviz96/antFake)

[PyPi](https://pypi.org/project/AntFake/)

### Install
```shell
pip install AntFake==0.1.0
```

Get random string
```python
from ant_fake import r_string
random_string = r_string(length=16, space=True)

>>> 'Sdw rrvSfreHL fs'
```

Random eth address
```python
from ant_fake import address
random_addr = address()

>>> '0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31'
```

Random float
```python
from ant_fake import r_digital
random_addr = r_digital(start=0, end=1000, decimals=8)

>>> 26.42244885
```

Random digital
```python
from ant_fake import r_digital
random_addr = r_digital(start=0, end=1000)

>>> 197
```