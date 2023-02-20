[1. re 정규 표현식](#re-정규-표현식)

### re 정규 표현식

#### 문자열 뒤집기 [[code]](https://github.com/songhee-lee/2023-python-coding-test/blob/main/1.%20Greedy/Joohyun/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
```python
import re

S = input()
S = re.sub('[0]{1,}','0',S)   # 000..0 을 0으로
S = re.sub('[1]{1,}','1',S)   # 111..1 을 1로
```

