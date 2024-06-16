import numpy as np

def finite_difference(f_vals, coeffs, interval_width):
    N = f_vals.shape[0]
    dx = interval_width / (N-1)

    derivatives = np.empty(N, dtype="float64")
    window_size = coeffs.shape[0]

    assert window_size % 2 == 1, """
    An odd number of coefficients must be provided to perform the finite
    difference method"""
    side_buffer = window_size // 2

    # set positions where window cannot fit around to 'not a number'
    derivatives[:side_buffer] = float("nan")
    derivatives[N-side_buffer:] = float("nan")

    for i in range(side_buffer, N-side_buffer):
        l,r = i-side_buffer,i+side_buffer+1
        derivatives[i] = sum(f_vals[l:r] * coeffs) / dx
    return derivatives

def first_order_deriv(f_vals, interval_width=1):
    weights = np.array([-1/2, 0, 1/2])
    return finite_difference(f_vals, weights, interval_width)

print(first_order_deriv(np.array([2., 3., 2., 4., 6., 0.])))
