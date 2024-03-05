def StringChallenge(str):
    num_dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    expression = ""
    i = 0
    
    while i < len(str):
        if str[i:i+3] in num_dict:
            expression += num_dict[str[i:i+3]]
            i += 3
        elif str[i:i+4] == 'plus':
            expression += '+'
            i += 4
        elif str[i:i+5] == 'minus':
            expression += '-'
            i += 5
    
    result = eval(expression)
    final_str = 'negative' + str(abs(result)) if result < 0 else str(result)
    
    challenge_token = 'zwgm43h52'
    final_output = final_str + challenge_token
    modified_output = ''.join('X' if (i + 1) % 3 == 0 else c for i, c in enumerate(final_output))
    
    return modified_output

# Test case
print(StringChallenge("onezeropluseight"))