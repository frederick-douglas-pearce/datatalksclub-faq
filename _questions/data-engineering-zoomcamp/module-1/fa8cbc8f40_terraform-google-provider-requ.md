---
id: fa8cbc8f40
question: Terraform google provider requires credentials.
sort_order: 1720
---

To ensure the sensitivity of the credentials file, I had to spend lot of time to input that as a file.

provider "google" {

project     = var.projectId

credentials = file("${var.gcpkey}")

#region      = var.region

zone = var.zone

}

