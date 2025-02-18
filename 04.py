def generate_brackets(n):
    def backtrack(open_count, close_count, current, result, counter):
        if len(current) == 2 * n:
            result[counter[0]] = current
            counter[0] += 1
            # print(counter[0], current)
            return
            
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(', result, counter)
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')', result, counter)
    
    result = {}
    counter = [0]  # используем список для передачи счетчика по ссылке
    backtrack(0, 0, '', result, counter)
    return result

n = 3
sequences = generate_brackets(n)
for key in sorted(sequences.keys()):
    print(sequences[key])
