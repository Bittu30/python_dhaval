# this is the assignment for the file handling

student_marks = {}
with open("student_marks.csv", "r") as f:
    for line in f:
        line = line.split(',')
        name = line[0]
        scores = line[3:]
        if name in student_marks:
            student_marks[name].append(scores)
        else:
            student_marks[name] = scores
print(student_marks)

del student_marks['']

total_mark = 0
for name, scores in student_marks.items():
    # print(scores)
    for i in range(0, len(scores)):
        print(sum(scores[i]))
        #print(int(float(scores[i])))
        #total_mark = total_mark + int(scores[i])
        # scores[i] = int(scores[i])
    # total_marks = student_marks[scores]
