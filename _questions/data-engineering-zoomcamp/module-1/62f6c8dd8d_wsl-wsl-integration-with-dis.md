---
id: 62f6c8dd8d
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_bc654841.png
question: WSL - WSL integration with distro Ubuntu unexpectedly stopped with exit
  code 1.
sort_order: 1030
---

<{IMAGE:image_1}>

Up restarting the same issue appears. Happens out of the blue on windows.

Solution 1: Fixing DNS Issue (credit: [reddit](https://www.reddit.com/r/docker/comments/p98xq6/docker_failed_to_start_exit_code_1/)) this worked for me personally

reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "4" /f

Restart your computer and then enable it with the following

reg add "HKLM\System\CurrentControlSet\Services\Dnscache" /v "Start" /t REG_DWORD /d "2" /fRestart your OS again. It should work.

Solution 2: right click on running Docker icon (next to clock) and chose "Switch to Linux containers" n

bash: conda: command not found

Database is uninitialized and superuser password is not specified.

Database is uninitialized and superuser password is not specified.

