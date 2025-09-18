---
id: accd08bead
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_b74116cb.png
question: How to install WSL on Windows 10 and 11?
sort_order: 1800
---

### Windows 10:

1. Open PowerShell as Admin.
2. Run the following command:
   ```bash
   wsl --install
   ```
3. Restart your computer.
4. Set up your Linux distribution (e.g., Ubuntu).

### Windows 11:

1. Open Windows Terminal as Admin.
2. Run:
   ```bash
   wsl --install
   ```
3. Restart if prompted.
4. Set up your Linux distribution.

### Additional Notes:

- To install a specific distribution, use:
  ```bash
  wsl --install -d <DistributionName>
  ```
- For updates, run:
  ```bash
  wsl --update
  ```

It is important to ensure that the "Virtual Machine Platform" feature is activated in your Windows "Features." You can check this by searching for "features" in the search bar to see if the checkbox is selected. Additionally, ensure that your system (in the BIOS) supports virtualization.

In the Microsoft Store, search for ‘Ubuntu’ or ‘Debian’ (or any Linux distribution you want) and install it. After downloading, open the app and choose a username and a password. Note that while typing your password, it may not display any characters (this is normal).

Once inside your Linux system, you can try commands such as `pwd`. To navigate back to your Windows system:

1. Use `cd ../..` twice.
2. Go to the "mnt" directory:
   ```bash
   cd mnt
   ```
3. List your files to view your disks and move to the desired folder.

<{IMAGE:image_1}>

Python should be already installed, but you can check with:
```bash
sudo apt install python3
```

To make your current folder the default when opening Ubuntu terminal, use:
```bash
echo "cd ../../mnt/your/folder/path" >> ~/.bashrc
```

To disable bell sounds, edit the inputrc file:
1. Open the file:
   ```bash
   sudo vim /etc/inputrc
   ```
2. Uncomment `set bell-style none`:
   - Press `i` (for insert), navigate to the line, delete `#`, press `Escape`, and then `:wq` to save and quit.
3. Open a new terminal to check the changes.

To install pip, run:
```bash
sudo apt install python3-pip
```

#### Possible Error

You might encounter the following error when installing pipenv:
```bash
/sbin/ldconfig.real: Can't link /usr/lib/wsl/lib/libnvoptix_loader.so.1 to libnvoptix.so.1
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link
```
To resolve, create a symbolic link:
```bash
sudo ln -s /usr/lib/wsl/lib/libcuda.so.1 /usr/lib64/libcuda.so
```