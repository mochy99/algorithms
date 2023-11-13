def test(order, input, output):
    expect_output = input
    if expect_output == output:
        return "Test " + str(order) + " passed"
    else:
        return "Test " + str(order) + " failed"