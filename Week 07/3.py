def display_grade(grade):
    assert(len(grade) == 2)
    assert(type(grade) == type([]) or type(grade) == type("") or type(grade) == (1,1))
    assert(grade[0] in ['A', 'B', 'C', 'D', 'F'])
    assert(grade[1] in ['+', '-', ' '])
    letter = grade[0]
    sign = grade[1]
    
    print("Your letter grade is", letter, "and your sign is", sign, ".")
    
grade = ["A", "+"]
display_grade(grade)