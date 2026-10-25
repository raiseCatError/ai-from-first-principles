# Week 01 / Day 01 — NumPy arrays and matrix multiplication

## Materials

Read the [NumPy absolute beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html) through array creation, array dimensions, shapes, and indexing. Review relevant [3Blue1Brown linear algebra visuals](https://www.3blue1brown.com/topics/linear-algebra). You don't need a full lecture today.

## Learning targets

1. Predict shapes and dtypes for NumPy arrays without running them.
2. Explain the difference between elementwise multiplication and matrix multiplication.
3. Write a dot-product loop and a 2-D matrix multiplication **without** NumPy dot/matmul.
4. Write tests for dimension mismatch and numerical correctness.

## Exercises

Edit `starter.py` and replace `NotImplementedError` with your own implementations.

1. `vector_dot([1,2,3],[4,5,6])` should return `32`.
2. `matrix_multiply([[1,2],[3,4]],[[5,6],[7,8]])` should return `[[19,22],[43,50]]`.
3. `describe_array(np.array([[1.,2.],[3.,4.]]))` returns shape and ndim according to the documented signature.
4. Predict the shapes of A `(4,3)` @ B `(3,2)` and A `(4,3)` * vector `(3,)`.

Your functions should handle bad dimensions with `ValueError`, not silently produce invalid results. Use Python loops for 1–2; you may use NumPy **only** in exercise 3.

## Self-check

```sh
python -m unittest discover -s exercises/week-01 -p 'test_*.py' -v
```

Tests **will fail until you solve TODOs**. That's intentional. Do not blindly copy a reference answer; reason through one row-by-column dot product by hand.

## Next day

Study a matrix as a linear transformation. Reimplement transpose and a matrix-vector multiply without NumPy, then use NumPy for validation.
