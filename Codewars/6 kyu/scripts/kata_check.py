def check(function, args, expected):
    if not isinstance(args, tuple):
        args = (args,)

    actual = function(*args)
    if actual == expected:
        print(f"OK   {function.__name__}{args} -> {actual!r}")
        return True

    print(
        f"FAIL {function.__name__}{args}: "
        f"expected {expected!r}, got {actual!r}"
    )
    return False


def run_tests(function, cases):
    passed = 0

    for args, expected in cases:
        if check(function, args, expected):
            passed += 1

    total = len(cases)
    if passed == total:
        print(f"All tests passed: {passed}/{total}")
    else:
        print(f"Tests failed: {total - passed}/{total}")
