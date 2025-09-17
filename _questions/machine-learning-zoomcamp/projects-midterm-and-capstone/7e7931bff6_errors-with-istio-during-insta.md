---
id: 7e7931bff6
question: Errors with istio during installation
sort_order: 3700
---

Problem description:

Running this:

curl -s "[raw.githubusercontent.com](https://raw.githubusercontent.com/kserve/kserve/release-0.9/hack/quick_install.sh") | bash

Fails with errors because of istio failing to update resources, and you are on kubectl > 1.25.0.

Check kubectl version with kubectl version

Solution description

Edit the file “quick_install.bash” by downloading it with curl without running bash. Edit the versions of Istio and Knative as per the matrix on the [KServe website](https://kserve.github.io/website/master/admin/serverless/serverless/#recommended-version-matrix).

Run the bash script now.

Added by Andrew Katoch

