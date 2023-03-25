def average_gpa(gpas):
    sum = 0
    for gpa in gpas:
        assert(type(gpa) == type(4.0))
        assert(gpa > 0.0)
        sum += gpa
        
    average = sum / len(gpas)
    return average

gpas = [1.2, 3.9, 2.89, 4.5]
assert(len(gpas) >= 0)
print("Averages: ", average_gpa(gpas))