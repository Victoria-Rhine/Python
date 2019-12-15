def encode(input_string):
    count = 1
    encoding = ''

    # if empty string return empty string
    if not input_string:
        return ""
    
    # start keeping track of characters
    encoding += input_string[0]

    for i in range(len(input_string) - 1):
        # if char is the same as next char increase count
        if(input_string[i] == input_string[i + 1]):
            count += 1
        else:
            # keep track of repeating character count
            if(count > 1):
                encoding += str(count)
            encoding += input_string[i + 1]
            count = 1
    if(count > 1):
        encoding += str(count)
    return encoding
            
