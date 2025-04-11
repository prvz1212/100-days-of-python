student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_scores = sum (student_scores)
print(total_scores)

total = 0
for score in student_scores:
    total += score
print(total)

#challenge with using max
student_score = [8,65,89,86,55,91,64,89]
# print(max(student_score))
a=0
for num in student_score:
    if a <= num:
        a = num
print(f"The highest number is{a}")
for num in student_score:
    if a>=num:
        a=num

print(f"The smallest number is {a}")

