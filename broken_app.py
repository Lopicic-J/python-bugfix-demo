def calculate_average(numbers):
    total = sum(numbers)
    return total / len(number)


def categorize_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    student_scores = [88, 92, 76, 81, 95]
    average = calculate_average(student_scores)

    print("Student scores:", student_scores)
    print("Average score:", round(average, 2))
    print("Category:", categorize_score(average_score))


if __name__ == "__main__":
    main()
