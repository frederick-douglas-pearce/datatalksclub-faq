---
id: f3dd94f323
question: 'WSL2 - ResponseError: model requires more system memory (X.X GiB) than
  is available (Y.Y GiB). My system has more than X.X GiB.'
sort_order: 110
---

Your WSL2 is set to use Y.Y GiB, not all your computer memory. Create .wslconfig file under your Windows user profile directory (C:\Users\YourUsername\.wslconfig) with the desired RAM allocation:

[wsl2]

memory=8GB

Restart WSL: wsl --shutdown

Run the free command to verify the changes. For more details, read [this article](https://www.aleksandrhovhannisyan.com/blog/limiting-memory-usage-in-wsl-2/).

