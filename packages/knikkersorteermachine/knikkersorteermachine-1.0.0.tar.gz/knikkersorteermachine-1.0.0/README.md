# Knikkersorteermachine
## Table of contents
- [Knikkersorteermachine](#knikkersorteermachine)
  - [Table of contents](#table-of-contents)
  - [Getting started](#getting-started)
  - [Example](#example)
  - [Author](#author)

## Getting started
1. Start out by importing the library
2. Next you open a new serial connection using the pyserial library
3. Then you initialize an instance of KnikkerSorteerMachine with the open serial connection
4. You can now call one of the methods to control the machine

## Example
```python
import time
import serial
from logging import DEBUG
from knikkersorteermachine import KnikkerSorteerMachine

with serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0) as port:
    interface = KnikkerSorteerMachine(serial=port, log_level=DEBUG)
    chute_pos = 0

    while True:
        interface.move_chute(chute_pos)

        chute_pos += 1
        if chute_pos > 6:
            chute_pos = 0

        time.sleep(0.2)

        interface.feed_one()

        time.sleep(1)

```

## Author
Jonas Claes <[jonas@jonasclaes.be](mailto:jonas@jonasclaes.be)>
