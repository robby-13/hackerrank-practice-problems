'''
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any  less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Example:

- grade = 84, round to 85 (85 - 84 is less than 3)
- grade = 29, do not round (result is less than 40)
- grade = 57, do not round (60 - 57 is 3 or higher)

'''

def gradingStudents(grades):
    # Write your code here
    # essentially the grade needs to be less than 3 points away from the next variable of 5. so the grade needs to be raised by just a point or two, hence the determining factors would be 1 and 2
    determining_factor = [1, 2]
    
    # loop through grades array 
    for i in range(len(grades)):
        # grades CAN NOT be lower than 38 in order to be considered for rounding up
        if grades[i] >= 38:
            # loop through determining factors to examine whether there's a match and then replace the value in the grades array with the new one
            for j in determining_factor:
                if (grades[i] + j) % 5 == 0:
                    grades[i] = grades[i] + j
    
    return grades
