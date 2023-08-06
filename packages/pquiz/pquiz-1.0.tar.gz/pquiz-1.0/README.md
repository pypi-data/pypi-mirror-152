# PQuiz

`pip install pquiz`

```
usage: pquiz [-h] [-b [1-65536]] [-e [1-65536]] [--all] -p PORT [PORT ...]
             [-m {pretty,printable}] [-t TIMEOUT]

A simple utility to check what ports are available for outgoing tcp connection
(ports 22 and 25 are not testable). Gianluca Caronte 2019-2022 (c)

optional arguments:
  -h, --help            show this help message and exit
  -b [1-65536], --range-begin [1-65536]
                        the begin of the ports range
  -e [1-65536], --range-end [1-65536]
                        the end of the ports range
  --all                 test all the ports
  -p PORT [PORT ...], --port PORT [PORT ...]
                        the port(s) to test
  -m {pretty,printable}, --print-mode {pretty,printable}
  -t TIMEOUT, --timeout TIMEOUT
                        timeout in seconds
```

## Examples

*Testing ports from 79 to 83:*
```
> python -m pquiz -b 79 -e 83
79      KO
80      OK
81      KO
82      KO
83      KO
```

*Testing ports from 79,80 and 83:*
```
> python -m pquiz -p 79 80 83
79      KO
80      OK
83      KO
```

*Testing ports from 79 to 83, with printable output:*
```
> python -m pquiz -b 79 -e 83 -m printable
80
```

*Testing ports from 79 to 83, with a half second timeout:*
```
> pquiz -b 79 -e 83 -t 0.5
79      KO
80      OK
81      KO
82      KO
83      KO
```