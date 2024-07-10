def my_range(end, start=0.0, step=1.0):
    result = []
    end_after_decimal = str(end).split('.')[1]
    start_after_decimal = str(start).split('.')[1]
    step_after_decimal = str(step).split('.')[1]
    lst = [len(end_after_decimal) if end_after_decimal else 1, len(start_after_decimal) if start_after_decimal else 1, len(step_after_decimal) if step_after_decimal else 0 ]
    max_decimal = max(lst)
    
    while start < end:
        formatted_number = f"{start:.{max_decimal}f}"
        if '.' in formatted_number:
            parts = formatted_number.split('.')
            if len(parts[1]) > 1:
                formatted_number = parts[0] + '.' + parts[1][0] + parts[1][1:].rstrip('0')
            else:
                formatted_number = parts[0] + '.' + parts[1]
        result.append(formatted_number)
        start += step

    formatted_result = '(' + ', '.join(result) + ')'
    print(formatted_result)

print('*** New Range ***')
input_list = [float(x) for x in input('Enter Input : ').split()]

if len(input_list) == 1:
    my_range(input_list[0])
elif len(input_list) == 2:
    my_range(input_list[1], input_list[0])
elif len(input_list) == 3:
    my_range(input_list[1], input_list[0], input_list[2])
