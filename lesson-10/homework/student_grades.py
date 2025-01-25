import csv
from collections import defaultdict

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_totals = defaultdict(list)  

    for grade_entry in grades:
        subject = grade_entry['Subject']
        grade = grade_entry['Grade']
        subject_totals[subject].append(grade)

    average_grades = {}
    for subject, grades in subject_totals.items():
        average_grades[subject] = sum(grades) / len(grades)

    return average_grades

def write_average_grades(file_name, average_grades):
    with open(file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Subject', 'Average Grade'])
        for subject, avg_grade in average_grades.items():
            csv_writer.writerow([subject, round(avg_grade, 2)])

if __name__ == '__main__':
    with open('grades.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Subject', 'Grade'])
        csv_writer.writerows([
            ['Alice', 'Math', 85],
            ['Bob', 'Science', 78],
            ['Carol', 'Math', 92],
            ['Dave', 'History', 74]
        ])

    grades = read_grades('grades.csv')
    average_grades = calculate_average_grades(grades)
    write_average_grades('average_grades.csv', average_grades)

    print("Average grades have been calculated and saved to 'average_grades.csv'.")
