---
id: 10316840ce
question: The input device is not a TTY when running docker in interactive mode (Running
  Docker on Windows in GitBash)
sort_order: 1950
---

$ docker exec -it 1e5a1b663052 bash

the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'

Fix:

winpty docker exec -it 1e5a1b663052 bash

A TTY is a terminal interface that supports escape sequences, moving the cursor around, etc.

Winpty is a Windows software package providing an interface similar to a Unix pty-master for communicating with Windows console programs.

More info on terminal, shell, console applications hi and so on:

[https://conemu.github.io/en/TerminalVsShell.html](https://conemu.github.io/en/TerminalVsShell.html)

(Marcos MJD)

