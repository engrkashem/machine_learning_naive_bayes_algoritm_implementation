column_data = list(np.unique(dFrame[unique_column]))
    print(f'Please choose an option from {unique_column}')
    for index in range(len(column_data)):
        print(f'{index}. {column_data[index]}')
    inp = None
    while True:
        inp = int(input())
        if inp < 0 or inp >= len(column_data):
            print('Error Occured. Your input is out of range. Try again.')
        else:
            break