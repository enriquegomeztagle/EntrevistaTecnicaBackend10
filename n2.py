def find_unique_palindromic_substrings(string):
    n = len(string)
    unique_palindromes = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                unique_palindromes.add(substring)
    return list(unique_palindromes)


input_string = "aabaa"
output = find_unique_palindromic_substrings(input_string)
print(output)

### OUTPUT
# ['b', 'aabaa', 'a', 'aa', 'aba']
