import argparse
import json
import os

DATA_FILE = "data/students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)

def add_student(name):
    students = load_students()
    if name in students:
        print(f"{name} already exists.")
        return
    students[name] = []
    save_students(students)
    print(f"Added student: {name}")

def add_grade(name, subject, score):
    students = load_students()
    if name not in students:
        print(f"No student named {name}. Add them first.")
        return
    students[name].append({"subject": subject, "score": score})
    save_students(students)
    print(f"Added grade: {name} - {subject}: {score}")

def report(name):
    students = load_students()
    if name not in students:
        print(f"No student named {name}.")
        return
    grades = students[name]
    if not grades:
        print(f"{name} has no grades yet.")
        return
    scores = [g["score"] for g in grades]
    print(f"Report for {name}:")
    for g in grades:
        print(f"  {g['subject']:10} : {g['score']}")
    print(f"  Average: {sum(scores)/len(scores):.2f}")
    print(f"  Highest: {max(scores)}")
    print(f"  Lowest:  {min(scores)}")

def main():
    parser = argparse.ArgumentParser(description="Student Grade Manager")
    subparsers = parser.add_subparsers(dest="command")

    sp = subparsers.add_parser("add-student")
    sp.add_argument("--name", required=True)

    gp = subparsers.add_parser("add-grade")
    gp.add_argument("--name", required=True)
    gp.add_argument("--subject", required=True)
    gp.add_argument("--score", type=float, required=True)

    rp = subparsers.add_parser("report")
    rp.add_argument("--name", required=True)

    args = parser.parse_args()

    if args.command == "add-student":
        add_student(args.name)
    elif args.command == "add-grade":
        add_grade(args.name, args.subject, args.score)
    elif args.command == "report":
        report(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()