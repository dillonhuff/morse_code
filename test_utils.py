def test_result(result, expected, test_name):
    if result == expected:
        print test_name + ' passed'
    else:
        print test_name + ' failed\n\texpected: ' + str(expected) + '\n\tactual: ' + str(result)
