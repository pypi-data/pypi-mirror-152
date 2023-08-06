## py_bark_client

yet another python bark client for bark, see https://github.com/Finb/Bark

## install
```shell script
pip install py_bark_client
```

## quick start

```python
from py_bark_client import Bark
bark = Bark(server='api.day.app', keys=['your key'])
bark.push(title="hello world", content="visit baidu", group='search', level=TimelinessLevel.TIME_SENSITIVE,
          automatically_copy=True, copy='https://wwww.baidu.com')

```