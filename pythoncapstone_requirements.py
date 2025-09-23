{
    "quizName": "string",
    "quizModule": "string",
    "quizScore": number,
    "studentId": number,
    "studentName": "string",
    "submissionDate": "string",
}


def filter_by_date(date_to_filter, submissions):
    """
    Filters a list of submission objects, returning only those
    with a submission_date matching the provided date.

    Args:
        date_to_filter (datetime.date): The date to filter by.
        submissions (list): A list of Submission objects.

    Returns:
        list: A new list containing only the matching Submission objects.
              Returns an empty list if no matches are found or the input list is empty.
    """
    return [
        submission
        for submission in submissions
        if submission.submission_date == date_to_filter
    ]


class Submission:
    """A mock Submission object for demonstration."""

    def __init__(self, submission_id, student_id, grade):
        self.submission_id = submission_id
        self.student_id = student_id
        self.grade = grade

    def __repr__(self):
        """String representation for easy printing."""
        return f"Submission(submission_id='{self.submission_id}', student_id='{self.student_id}', grade={self.grade})"


def filter_by_student_id(student_id: str, submissions: list) -> list:
    """
    Filters a list of submission objects by a given student ID.

    Args:
        student_id: The ID of the student to filter by.
        submissions: A list of submission objects.

    Returns:
        A new list containing only the submissions matching the student_id.
    """
    return [s for s in submissions if s.student_id == student_id]


def find_unsubmitted(target_date, student_names, submission_objects):
    """
    Identifies students who have not made any submissions on a specific date.

    Args:
        target_date (str): The date to check for unsubmitted quizzes (e.g., "YYYY-MM-DD").
        student_names (list): A list of student names.
        submission_objects (list): A list of submission objects. Each submission
                                   object is expected to have 'student_name' and 'submission_date' attributes.

    Returns:
        list: A list of names of students who have not completed any quizzes on the target date.
              Returns an empty list if all students submitted or if no unsubmitted students are found.
    """
    submitted_students_on_date = set()
    for submission in submission_objects:
        if submission.get("submission_date") == target_date:
            submitted_students_on_date.add(submission.get("student_name"))

    unsubmitted_students = []
    for student in student_names:
        if student not in submitted_students_on_date:
            unsubmitted_students.append(student)

    return unsubmitted_students


def get_average_score(submissions):
    """
    Calculates the average score from a list of submission objects.

    Args:
      submissions: A list of submission objects, each having a 'score' attribute.

    Returns:
      The average score, rounded to one decimal place.
    """
    if not submissions:
        return 0.0  # Return 0 if the list is empty to avoid division by zero

    total_score = 0
    for submission in submissions:
        total_score += submission.score  # Assuming each object has a 'score' attribute

    average = total_score / len(submissions)
    return round(average, 1)


def get_average_score_by_module(submissions):
    """
    Calculates the average quiz score for each module from a list of submissions.

    Args:
        submissions (list): A list of submission objects.
                            Each object is expected to have 'module_name' and 'score' attributes.

    Returns:
        dict: An object with module names as keys and their average quiz score as values.
    """
    scores_by_module = {}

    # Group scores by module name
    for submission in submissions:
        module_name = submission.get("module_name")
        score = submission.get("score")

        if module_name not in scores_by_module:
            scores_by_module[module_name] = []
        scores_by_module[module_name].append(score)

    average_scores = {}

    # Calculate the average for each module
    for module_name, scores in scores_by_module.items():
        if scores:
            average_scores[module_name] = sum(scores) / len(scores)
        else:
            average_scores[module_name] = 0.0  # Handle empty score lists

    return average_scores
