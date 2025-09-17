---
id: a5a8a6ac39
question: Setting JAVA_HOME with Homebrew on Apple Silicon
sort_order: 3890
---

The MacOS setup instruction ([https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/macos.md#installing-java](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/macos.md#installing-java)) for setting the JAVA_HOME environment variable is for Intel-based Macs which have a default install location at /usr/local/. If you have an Apple Silicon mac, you will have to set JAVA_HOME to /opt/homebrew/, specifically in your .bashrc or .zshrc:

export JAVA_HOME="/opt/homebrew/opt/openjdk/bin"

export PATH="$JAVA_HOME:$PATH"

Confirm that your path was correctly set by running the command: which java

You should expect to see the output:

/opt/homebrew/opt/openjdk/bin/java

Check java version with the next command:

Java -version

Reference: [https://docs.brew.sh/Installation](https://docs.brew.sh/Installation)

