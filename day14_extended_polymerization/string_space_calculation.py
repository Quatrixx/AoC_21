element_count = [(0, len('PBFNVFFPCPCPFPHKBONB'))]

for step in range(1, 41):
    element_count.append((step, element_count[step-1][1] * 2 + 1))

for step, length in element_count:
    if step % 5 == 0:
        if len(str(length)) > 12:
            print(f'step {step:2}:  {length // 1000000000000:3} TB')
        elif len(str(length)) > 9:
            print(f'step {step:2}:  {length // 1000000000:3} GB')
        elif len(str(length)) > 6:
            print(f'step {step:2}:  {length // 1000000:3} MB')
        elif len(str(length)) > 3:
            print(f'step {step:2}:  {length // 1000:3} KB')
        else:
            print(f'step {step:2}:  {length:3}  B')