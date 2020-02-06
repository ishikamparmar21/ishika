#start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def sort(start, finish):
     for i in range(0, len(finish)-1):
          for j in range(i, len(finish)):
               if finish[i] > finish[j]:
                    temp = finish[i]
                    finish[i] = finish[j]
                    finish[j] = temp
                    temp = start[i]
                    start[i] = start[j]
                    start[j] = temp


def greedy_activity_selector(s, f):
     assert(len(s) == len(f)) #each start time must watch a finish time
     n = len(s) # equal to len f
     a = []
     k = 0
     for m in range(1, n):
            if s[m] >= f[k]:
                 a.append(m)
                 k = m
     return a

start = [0]
finish = [0]
print('Enter the start time and end time of tasks')
print('------------------------------------------')
cont = 'Y'
while cont == 'y' or cont == 'Y':
      st = int(input('Enter the start time:'))
      ft = int(input('Enter the finish time:'))
      start.append(st)
      finish.append(ft)
      cont = input('Continue? (Y/N): ')

sort(start, finish)
print(start[1:], finish[1:])
a = greedy_activity_selector(start, finish)
print('Sequence of execution:')
for i in range(0, len(a)):
    print('task: ',a[i])        

















               
