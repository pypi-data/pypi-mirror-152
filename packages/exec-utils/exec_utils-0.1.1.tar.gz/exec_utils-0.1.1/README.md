## python-exec-utils

### Getting started

```python
from exec_utils import exec_strict

cmd = ["sort", "-n"]
stdout = exec_strict(cmd, stdin_str="2 world\n1 hello\n")
print(stdout)
# "1 hello\n2 world"

```







