


# for i in range(2,10,4):
#     for j in range(2,11):
#         for k in range(i,i+4):
#             print(f'{k:>3} *{j:>3} ={k * j:>3}', end = '\t')
#         print()
#     print()


# res = [f'{k:>3} *{j:>3} ={(k * j):>3}' for i in range(2, 10, 4)  for j in range(2, 11) for k in range(i, i+4) ]

# res = [f'{i:>3} *{j:>3} ={(i * j):>3}' for i in range(2,10)  for j in range(2, 10)]
# print(*res, sep='\n')

#  Так делать не нужно!!!

res = ['\n'+'\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                       for k in range(i, i + 4)])
       if i == 6 and j == 2 else '\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                                            for k in range(i, i + 4)])
       for i in range(2, 10, 4)
       for j in range(2, 11)]

# print('\t'.join(res))


print(*res, sep='\n')