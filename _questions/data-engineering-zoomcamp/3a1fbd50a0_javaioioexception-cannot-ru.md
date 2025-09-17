---
course: data-engineering-zoomcamp
id: 3a1fbd50a0
question: Java.io.IOException. Cannot run program “C:\hadoop\bin\winutils.exe”. CreateProcess
  error=216, This version of 1% is not compatible with the version of Windows you
  are using.
section: 'Module 5: pyspark'
sort_order: 3740
---

Change the hadoop version to 3.0.1.Replace all the files in the local hadoop bin folder with the files in this repo:  [winutils/hadoop-3.0.1/bin at master · cdarlint/winutils (github.com)](https://github.com/cdarlint/winutils/tree/master/hadoop-3.0.1/bin)

If this does not work try to change other versions found in this repository.

For more information please see this link: [This version of %1 is not compatible with the version of Windows you're running · Issue #20 · cdarlint/winutils (github.com)](https://github.com/cdarlint/winutils/issues/20)

