def split_parentheses(word: str) -> str:
    stack = list()
    remove_idx = set()

    for idx, token in enumerate(word):
        if token == "(":
            stack.append(idx)
        elif token == ")":
            if len(stack) == 0 or word[stack[-1]] == ")":
                remove_idx.add(idx)
            else:
                stack.pop()

    # remove unbalanced '(' parentheses from the stack
    remove_idx.update(stack)

    return "".join(
        [char for (idx, char) in enumerate(word) if idx not in remove_idx]
    )


assert split_parentheses(")a(b((cd)e(f)g)") == "ab((cd)e(f)g)"
assert split_parentheses("lee(t(c)o)de)") == "lee(t(c)o)de"
assert split_parentheses("))((") == ""
assert split_parentheses("(a(b(c)d)") == "a(b(c)d)"
