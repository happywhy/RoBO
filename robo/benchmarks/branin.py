
import numpy as np


def branin(x):
    """Branin test function
        optima:  (-pi, 12.275), (pi, 2.275), (9.42478, 2.475)
        best value = 0.397887

    Arguments: 2 dimensional numpy array
    Return: y value
    """

    X_lower, X_upper, n_dims = get_branin_bounds()

    assert x.shape[1] == n_dims
    assert np.all(x[:, 0] >= X_lower[0])
    assert np.all(x[:, 1] >= X_lower[1])
    assert np.all(x[:, 0] <= X_upper[0])
    assert np.all(x[:, 1] <= X_upper[1])
    assert np.all(x < X_upper)

    y = (x[:, 1] - (5.1 / (4 * np.pi ** 2)) * x[:, 0] ** 2 + 5 * x[:, 0] / np.pi - 6) ** 2
    y += 10 * (1 - 1 / (8 * np.pi)) * np.cos(x[:, 0]) + 10
    return y[:, np.newaxis]


def get_branin_bounds():
    X_lower = np.array([-5, 0])
    X_upper = np.array([10, 15])
    n_dims = 2
    return X_lower, X_upper, n_dims
