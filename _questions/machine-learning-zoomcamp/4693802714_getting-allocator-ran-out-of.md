---
course: machine-learning-zoomcamp
id: '4693802714'
question: 'Getting: Allocator ran out of memory errors?'
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3440
---

If you are running tensorflow on your own machine and you start getting the following errors:

Allocator (GPU_0_bfc) ran out of memory trying to allocate 6.88GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.

Try adding this code in a cell at the beginning of your notebook:

config = tf.compat.v1.ConfigProto()

config.gpu_options.allow_growth = True

session = tf.compat.v1.Session(config=config)

After doing this most of my issues went away. I say most because there was one instance when I still got the error once more, but only during one epoch. I ran the code again, right after it finished, and I never saw the error again.

Added by Martin Uribe

Problem with downloading  [xception_v4_large_08_0.894.h5](https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5)  fileThe following old link is not valid anymore :[[GitHub](https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5)](https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5)====>The new link to download the file is :

[[GitHub](https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/tag/chapter7-model)](https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/tag/chapter7-model)

Added by Sam

