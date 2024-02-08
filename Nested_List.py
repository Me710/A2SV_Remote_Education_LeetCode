if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    sorted_students = sorted(list(set([score for name, score in students])))
    second_lowest = sorted_students[1] 
    
    for name, score in sorted(students):
        if score == second_lowest:
            print(name)