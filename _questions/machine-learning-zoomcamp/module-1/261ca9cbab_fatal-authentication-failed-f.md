---
id: 261ca9cbab
question: 'Fatal: Authentication failed for https://github.com/username'
sort_order: 350
---

I had a problem when I tried to push my code from Git Bash:

remote: Support for password authentication was removed on August 13, 2021.

remote: Please see [GitHub](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls) for information on currently recommended modes of authentication.

fatal: Authentication failed for '[https://github.com/username](https://github.com/username)

Solution:

Create a personal access token from your github account and use it when you make a push of your last changes.

[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Bruno Bedón

