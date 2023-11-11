sumy=0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
if query_name in student_marks :
    res = student_marks.get(query_name)
#print(res)
#print(student_marks)
#print(scores)
length = len(res)
#print(length)
for i in res:
    sumy = sumy + i
avg_marks = sumy/length
print(format(avg_marks,".2f"))
