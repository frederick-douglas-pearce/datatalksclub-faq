---
id: 8637328bbb
question: How to easily get file size in powershell terminal ?
sort_order: 3180
---

To check your file size using the powershell terminal, you can do the following command lines:

$File = Get-Item -Path path_to_file

$FileSize = (Get-Item -Path $FilePath).Length

Now you can check the size of your file, for example in MB:

Write-host "MB":($FileSize/1MB)

Source: [https://www.sharepointdiary.com/2020/10/powershell-get-file-size.html#:~:text=To%20get%20the%20size%20of,the%20file%2C%20including%20its%20size](https://www.sharepointdiary.com/2020/10/powershell-get-file-size.html#:~:text=To%20get%20the%20size%20of,the%20file%2C%20including%20its%20size).

Added by Mélanie Fouesnard

