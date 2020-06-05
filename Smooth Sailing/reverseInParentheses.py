def reverseInParentheses(inputString):
    while "(" in inputString or ")" in inputString:
        end_index = -1
        start_index = -1
        for index, value in reversed(list(enumerate(inputString))):
            if value == ")":
                end_index = index
            elif value == "(":
                start_index = index
                word = (inputString[start_index + 1:end_index])[::-1]
                if end_index != len(inputString) - 1:
                    inputString = inputString[:start_index] + word + inputString[end_index + 1:]
                else:
                    inputString = inputString[:start_index] + word
                break
    return inputString
