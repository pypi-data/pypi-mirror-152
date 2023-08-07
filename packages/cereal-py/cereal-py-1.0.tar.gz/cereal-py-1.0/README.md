# cereal
Parallelization requires tools to reference data without overuse of memory, cereal allows you to reference PyObjects to pointers without creating a deep copy in memory. Inspired by [ZeroIntensity's](https://github.com/ZeroIntensity) [pointers.py](https://github.com/ZeroIntensity/pointers.py).


- [Documentation](https://cereal-py.netlify.app)
- [Repository](https://github.com/joshua-auchincloss/cereal-py)

```py
import numpy as np
from cereal import eat

x = [1, 2, 3, 4]

yum = eat(x, its = 4, np.array, copy = False)

>> yum
>> array([<pointer to list object at 0x113b3edc0>,
          <pointer to list object at 0x113b3edc0>,
          <pointer to list object at 0x113b3edc0>,
          <pointer to list object at 0x113b3edc0>], dtype=object) # 4 pointers to the original object

>> (~yum[0])[0]
>> 1

yum[0][0] = 4

>> x # the original object
>> [4, 2, 3, 4] # it changed!
```
