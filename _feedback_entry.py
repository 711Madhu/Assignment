
def collect_feedback():
    name = input("Enter your name: ")
    course = input("Enter your course name: ")
    feedback = input("Please provide your feedback: ")

    with open("feedback.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Course: {course}\n")
        f.write(f"Feedback: {feedback}\n")
        f.write("-" * 40 + "\n")

    print("Thank you for your feedback!")

if __name__ == "__main__":
    collect_feedback()
