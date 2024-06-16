function finite_difference(f_vals, coeffs, interval_width)
	N = size(f_vals)[1]
	dx = interval_width / (N-1)

	derivatives = Vector{Float64}(undef, N)
	window_size = size(coeffs)[1]

	@assert window_size % 2 == 1
	"An odd number of coefficients must be provided to perform the finite
	difference method";
	side_buffer = window_size ÷ 2

	# set positions where window cannot fit around to 'not a number'
	derivatives[1:side_buffer] .= NaN
	derivatives[(N-side_buffer+1):N] .= NaN

	for i = side_buffer+1:N-side_buffer
		window = i-side_buffer:i+side_buffer
		derivatives[i] = sum(f_vals[window] .* coeffs) / dx
	end

	return derivatives
end

first_order_deriv(f_vals, interval_width=1) =
	finite_difference(f_vals, [-1/2, 0, 1/2], interval_width)

println(first_order_deriv([2., 3., 2., 4., 6., 0.]))
