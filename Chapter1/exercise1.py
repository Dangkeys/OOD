def is_valid_time(hh: int, mm: int, ss: int) -> dict:
    if hh < 0:
        return {'valid': False, 'message': f'hh({hh}) is invalid!'}
    if mm < 0 or mm > 59:
        return {'valid': False, 'message': f'mm({mm}) is invalid!'}
    if ss < 0 or ss > 59:
        return {'valid': False, 'message': f'ss({ss}) is invalid!'}
    return {'valid': True, 'message': 'Time is valid'}

print('*** Converting hh.mm.ss to seconds ***')
try:
    hh, mm, ss = [int(x) for x in input('Enter hh mm ss : ').split()]

    validation_result = is_valid_time(hh, mm, ss)
    if not validation_result['valid']:
        print(validation_result['message'])
    else:
        time = ss + mm * 60 + hh * 60 * 60
        
        hh_str = str(hh).zfill(2)
        mm_str = str(mm).zfill(2)
        ss_str = str(ss).zfill(2)
        
        print(f'{hh_str}:{mm_str}:{ss_str} = {"{:,}".format(time)} seconds')

except ValueError:
    print('Invalid input! Please enter integers for hh, mm, and ss.')
