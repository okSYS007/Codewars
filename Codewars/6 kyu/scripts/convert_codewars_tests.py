import ast
import re
import sys
from pathlib import Path


ASSERT_RE = re.compile(r"^\s*#?\s*test\.assert_equals\((.*)\)\s*$")
LOCAL_TESTS_RE = re.compile(r"\n\n# --- local tests ---\nif __name__ == .__main__.:\n.*\Z", re.S)


def split_assert_equals_args(text):
    node = ast.parse(f"f({text})", mode="eval").body
    if not isinstance(node, ast.Call) or len(node.args) < 2:
        raise ValueError("expected test.assert_equals(actual, expected)")
    return node.args[0], node.args[1]


def convert_line(line):
    match = ASSERT_RE.match(line)
    if not match:
        return None

    actual, expected = split_assert_equals_args(match.group(1))
    if not isinstance(actual, ast.Call) or not isinstance(actual.func, ast.Name):
        raise ValueError("first assert argument must be a function call")

    function_name = actual.func.id
    args = ", ".join(ast.unparse(arg) for arg in actual.args)
    if len(actual.args) == 1:
        args += ","

    return function_name, f"        (({args}), {ast.unparse(expected)}),"


def convert_file(path):
    source_path = Path(path)
    text = source_path.read_text(encoding="utf-8")

    cases = []
    function_name = None
    remaining_lines = []

    for line in text.splitlines():
        try:
            converted = convert_line(line)
        except SyntaxError:
            converted = None

        if converted is None:
            remaining_lines.append(line)
            continue

        current_function, case_line = converted
        function_name = function_name or current_function
        if current_function != function_name:
            raise ValueError(
                f"mixed test functions: {function_name!r} and {current_function!r}"
            )
        cases.append(case_line)

    if not cases:
        raise ValueError("no test.assert_equals(...) lines found")

    text_without_asserts = "\n".join(remaining_lines).rstrip()
    text_without_asserts = LOCAL_TESTS_RE.sub("", text_without_asserts).rstrip()

    local_tests = [
        "",
        "",
        "# --- local tests ---",
        'if __name__ == "__main__":',
        "    from scripts.kata_check import run_tests",
        "",
        f"    run_tests({function_name}, [",
        *cases,
        "    ])",
        "",
    ]

    source_path.write_text(text_without_asserts + "\n".join(local_tests), encoding="utf-8")
    print(f"Converted {len(cases)} tests for {function_name} in {source_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/convert_codewars_tests.py <kata-file.py>")
        raise SystemExit(2)

    convert_file(sys.argv[1])


if __name__ == "__main__":
    main()
