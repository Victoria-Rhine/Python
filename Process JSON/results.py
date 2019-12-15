import json

def main():
    with open('grades.json') as f:
        grades = json.load(f)

    print ("Exam results for class 28\n=========================")

    for grade in grades:
        if (grade['class_id'] == 28):
            print (grade['student_id'])

if __name__ == "__main__":
    main()
