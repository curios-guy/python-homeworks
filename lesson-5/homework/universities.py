# list of universities
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# returns university name, student numbers and tuition fees
def enrollment_stats(unis):
    uni = [each[0] for each in unis]
    students = [each[1] for each in unis]
    tuitions = [each[2] for each in unis]
    # print(enrollments)
    # print(tuitions)
    return uni, students, tuitions

# calculates mean value
def mean(val):
    return round(sum(val) / len(val),2)

# calculates median value
def median(val):
    sortedd = sorted(val)
    # print(sortedd)
    length = len(sortedd)
    mid = length // 2
    if length%2==0:
        return (sortedd[mid]+ sortedd[mid-1])/2
    else: return sortedd[mid]

# main call-for-action to functions
uni, students, tuitions = enrollment_stats(universities)

totalStudents = sum(students)
totalTuition = sum(tuitions)
studentMean = mean(students)
studentMedian = median(students)
tuitionMean = mean(tuitions)
tuitionMedian = median(tuitions)

# prints result
print("*******************")
print(f"Total students: {sum(students)}")
print(f"Total tuition: ${sum(tuitions)}")

print(f"\n\nStudent mean: {mean(students)}")
print(f"Student median: {median(students)}")

print(f"\n\nTuition mean: ${mean(tuitions)}")
print(f"Tuition median: ${median(tuitions)}")
print("*******************")

