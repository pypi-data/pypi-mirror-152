# quake3rcon
A tiny library for using Quake 3's RCON protocol feature for some game servers like [FiveM](https://fivem.net/).
The RCON protocols are used to remotely control game servers, i.e. execute commands on a game server and receive the respective results.

## License
> MIT License
> 
> Copyright (c) 2022 hellyet
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## `class Rcon`
| __function__ | __args__                                                               | __returns__ | __description__                               |
|--------------|------------------------------------------------------------------------|-------------| --------------------------------------------- |
| \_\_init\_\_ | ip (*ip*), port (*int*), password (*str*), timeout (*float*, optional) | *None*      | *Initialize rcon connection*                  |
| \_\_del\_\_  | *None*                                                                 | *None*      | *Close rcon connection on object destruction* |
| recv         | *None*                                                                 | *None*      | *Gets server response*                        |
| send         | command (*str*)                                                        | *str*       | *Send rcon command*                           |

## How i can use this?
To install run  
`pip install quake3rcon`  

### This is an example using q3rcon-py in your code
```py
from quake3rcon.rcon import Rcon

rcon = Rcon('192.168.0.1', 30120, 'yourstrongpassword') # Connecting to RCON

responce = rcon.send('command and some args for it') # Send RCON command
print(responce) # Show server response

# Do some stuff

del rcon # Delete object and disconnect from RCON
```
