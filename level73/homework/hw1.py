def check_exam(arr1, arr2):
    score = 0  # Initialize score
    
    for correct, student in zip(arr1, arr2):
        if student == correct:
            score += 4  # Correct answer
        elif student == "":  
            score += 0  # Blank answer, no points added
        else:
            score -= 1  # Incorrect answer
    
    return max(score, 0)  # Ensure score is not negative
