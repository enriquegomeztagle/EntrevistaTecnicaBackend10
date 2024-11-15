def longest_palindromic_substring_manacher(s):
    t = "#".join(f"^{s}$")
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len, center_index = max((n, i) for i, n in enumerate(p))
    start = (center_index - max_len) // 2
    return s[start : start + max_len]


input_string = "ababacdfgdcabbabba"
output = longest_palindromic_substring_manacher(input_string)
print(output)

### OUTPUT
# abbabba
