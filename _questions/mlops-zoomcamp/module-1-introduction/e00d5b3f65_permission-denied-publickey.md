---
id: e00d5b3f65
question: Permission denied (publickey) Error (when you remove your public key on
  the AWS machine)
sort_order: 680
---

I found a good guide how to get acces to your machine again when you removed your public key.

Using the following link you can go to Session Manager and log in to your instance and create public key again. [https://repost.aws/knowledge-center/ec2-linux-fix-permission-denied-errors](https://repost.aws/knowledge-center/ec2-linux-fix-permission-denied-errors)

The main problem for me here was to get my old public key, so for doing this you should run the following command: ssh-keygen -y -f /path_to_key_pair/my-key-pair.pem

For more information: [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html#retrieving-the-public-key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html#retrieving-the-public-key)

Hanna Zhukavets ([a.zhukovec1901@gmail.com](mailto:a.zhukovec1901@gmail.com))

