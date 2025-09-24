from datetime import date, datetime
from typing import List, Dict
from collections import defaultdict


def filter_by_date(date_to_filter: date, submissions: List[Dict]) -> List[Dict]:
    """
    Returns a list of submission objects with submissionDate equal to the given date.
    Returns an empty list if submissions array is empty or no matches are found.
    """
    if not submissions:
        return []

    filtered = []
    for sub in submissions:
        try:
            sub_date = datetime.strptime(sub["submissionDate"], "%Y-%m-%d").date()
            if sub_date == date_to_filter:
                filtered.append(sub)
        except (KeyError, ValueError, TypeError):
            continue
    return filtered


def filter_by_student_id(student_id: int, submissions: List[Dict]) -> List[Dict]:
    if not submissions:
        return []
    return [sub for sub in submissions if sub.get("studentId") == student_id]


def find_unsubmitted(
    date_to_check: date, student_names: List[str], submissions: List[Dict]
) -> List[str]:
    if not student_names:
        return []
    if not submissions:
        return student_names.copy()

    submitted_students = set()
    for sub in submissions:
        try:
            sub_date = date.fromisoformat(sub["submissionDate"])
            if sub_date == date_to_check:
                submitted_students.add(sub.get("studentName"))
        except (KeyError, ValueError, TypeError):
            continue

    return [name for name in student_names if name not in submitted_students]


def get_average_score(submissions: List[Dict]) -> float:
    if not submissions:
        return 0.0

    total_score = 0
    count = 0
    for sub in submissions:
        try:
            score = float(sub.get("quizScore"))
            total_score += score
            count += 1
        except (TypeError, ValueError):
            continue
    if count == 0:
        return 0.0

    return round(total_score / count, 1)


def get_average_score_by_module(submissions: List[Dict]) -> Dict[str, float]:
    if not submissions:
        return {}

    module_totals = defaultdict(float)
    module_counts = defaultdict(int)
    for sub in submissions:
        module = sub.get("quizModule")
        try:
            score = float(sub.get("quizScore"))
            if module:
                module_totals[module] += score
                module_counts[module] += 1
        except (TypeError, ValueError):
            continue

    return {
        module: round(module_totals[module] / module_counts[module], 1)
        for module in module_totals
    }


submissions = [
    {
        "quizName": "Quiz 1",
        "quizModule": "Statistics",
        "quizScore": 85,
        "studentId": 1,
        "studentName": "Alice",
        "submissionDate": "2025-09-24",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "Algebra",
        "quizScore": 78,
        "studentId": 2,
        "studentName": "Bob",
        "submissionDate": "2025-09-24",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "Statistics",
        "quizScore": 82,
        "studentId": 3,
        "studentName": "Charlie",
        "submissionDate": "2025-09-23",
    },
    {
        "quizName": "Quiz 2",
        "quizModule": "Algebra",
        "quizScore": 81,
        "studentId": 1,
        "studentName": "Alice",
        "submissionDate": "2025-09-23",
    },
    {
        "quizName": "Quiz 1",
        "quizModule": "History",
        "quizScore": 80,
        "studentId": 2,
        "studentName": "Bob",
        "submissionDate": "2025-09-23",
    },
]

all_students = ["Alice", "Bob", "Charlie", "David"]


filtered_date = filter_by_date(date(2025, 9, 24), submissions)
print("Filter by Date (2025-09-24):")
for f in filtered_date:
    print(f)
print()


filtered_student = filter_by_student_id(1, submissions)
print("Filter by Student ID (1):")
for f in filtered_student:
    print(f)
print()


unsubmitted_students = find_unsubmitted(date(2025, 9, 24), all_students, submissions)
print("Unsubmitted Students on 2025-09-24:")
print(unsubmitted_students)
print()

average_score = get_average_score(submissions)
print("Average Quiz Score:")
print(average_score)
print()

average_by_module = get_average_score_by_module(submissions)
print("Average Score by Module:")
print(average_by_module)
print()
