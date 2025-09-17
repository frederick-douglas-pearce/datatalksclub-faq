---
id: 3ef50b0d88
question: 'Question 7: Multiplication operators.'
sort_order: 510
---

Note, that matrix multiplication (matrix-matrix, matrix-vector multiplication) can be written as * operator in some sources, but performed as [@](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) operator or [np.matmul()](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) via numpy. * operator performs element-wise multiplication ([Hadamard product](https://en.wikipedia.org/wiki/Hadamard_product_(matrices))).

[numpy.dot()](https://numpy.org/doc/stable/reference/generated/numpy.dot.html) or [ndarray.dot()](https://numpy.org/doc/1.21/reference/generated/numpy.ndarray.dot.html) can be used, but for matrix-matrix multiplication @ or np.matmul() is preferred (as per numpy [doc](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot)).

If multiplying by a scalar [numpy.multiply()](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html) or * is preferred.

Added by Andrii Larkin

