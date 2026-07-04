def char_freq(s):
    freq = {}
    
    for char in s:
        if char != " ":
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq
    
inp = input("Enter a string: ")
print(char_freq(inp))