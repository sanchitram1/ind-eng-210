import numpy as np
from numpy.testing import assert_array_equal
from numpy.typing import NDArray


def transpose_2d(arr: NDArray):
    """
    This function takes a 2d array, arr, and returns the matrix transposed.
    (rows become columns and columns become rows)
    """
    if len(arr.shape) < 2:
        raise NotImplementedError(
            f"Function is only implemented for 2d arrays, input's shape is {arr.shape}"
        )

    rows = arr.shape[0]
    cols = arr.shape[1]
    transposed = np.zeros(shape=(cols, rows))

    for i in range(rows):
        transposed[:, i] = arr[i, :]

    return transposed


def test():
    # Fail on 1d arrays
    try:
        transpose_2d(np.array([1, 2, 3]))
    except NotImplementedError:
        print("1 dimensional arrays correctly fail")
    except Exception as e:
        raise e

    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    assert_array_equal(transpose_2d(arr1), arr1.T)

    arr2 = np.array([[i for i in range(100)], [j for j in range(100)]])
    assert_array_equal(transpose_2d(arr2), arr2.T)


if __name__ == "__main__":
    test()
