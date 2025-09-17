---
id: 00e8093b90
question: Running out of storage when using kestra with postgres on GCP VM
sort_order: 1890
---

Running out of storage while trying to backfill. I realized my GCP VM only has 30GB of storage and I was eating it up! Couple things I did/would suggest:

Clean up your GCP VM drive. You can use this command to see what is taking up the most space:  $ sudo du -sh *

(~1gb) For me, Anaconda installer was taking up lots of space - you can delete that immediately because I already installed anaconda. I don’t need the installer anymore.

Rm -rf  <anacondainstaller_fpath>

(~3gb) Anaconda also takes up lots of space. You can’t delete it all if you want to run python, but you can clean it up significantly. I don’t care much about libs, etc. because I can build them in a docker container! Command is $ conda clean --all -y

You can clean up your kestra files with a purge flow. Here is the generic one: [https://kestra.io/docs/administrator-guide/purge](https://kestra.io/docs/administrator-guide/purge)

I personally wanted to do it immediately, not at end of month, so I made end date just now and got rid of the trigger block. You can also specify if you want to removed FAILED state executions, but I chose not to: endDate: "{{ now() }}"

You can clean up your pg database by manually deleting tables in pgadmin. Or possibly set up a workflow for it in kestra, but it was easy enough to manually delete.

