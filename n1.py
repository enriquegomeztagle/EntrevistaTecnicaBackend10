def find_palindromic_substrings(string):
    n = len(string)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.append(substring)
    return result


input_string = "aab"
output = find_palindromic_substrings(input_string)
print(output)

### OUTPUT
# ["a", "aa", "a", "b"]
