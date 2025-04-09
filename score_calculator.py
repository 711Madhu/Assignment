def calculate_score(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)
