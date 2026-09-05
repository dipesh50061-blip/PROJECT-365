from modelus.task_manager import tasks
from modelus.study_tracker import study_sessions
from modelus.goal_manager import goals
from modelus.habit_tracker import habits
from modelus.focus_center import focus_sessions
from modelus.notes_manager import notes


def dashboard():
    print("\n" + "=" * 55)
    print("                 N E X U S")
    print("                  DASHBOARD")
    print("=" * 55)

    # =========================
    # TASK OVERVIEW
    # =========================

    total_tasks = len(tasks)

    completed_tasks = sum(
        1
        for task in tasks
        if task.get("completed", False)
    )

    pending_tasks = total_tasks - completed_tasks

    if total_tasks > 0:
        task_completion_rate = (
            completed_tasks / total_tasks
        ) * 100
    else:
        task_completion_rate = 0


    # =========================
    # STUDY OVERVIEW
    # =========================

    total_study_sessions = len(study_sessions)

    total_study_duration = sum(
        session["duration"]
        for session in study_sessions
    )

    if total_study_sessions > 0:
        average_study_duration = (
            total_study_duration / total_study_sessions
        )
    else:
        average_study_duration = 0


    # =========================
    # GOAL OVERVIEW
    # =========================

    total_goals = len(goals)

    completed_goals = sum(
        1
        for goal in goals
        if goal.get("completed", False)
    )

    pending_goals = total_goals - completed_goals

    if total_goals > 0:
        goal_completion_rate = (
            completed_goals / total_goals
        ) * 100
    else:
        goal_completion_rate = 0


    # =========================
    # HABIT OVERVIEW
    # =========================

    total_habits = len(habits)

    completed_habits = sum(
        1
        for habit in habits
        if habit.get("completed", False)
    )

    pending_habits = total_habits - completed_habits


    # =========================
    # FOCUS OVERVIEW
    # =========================

    total_focus_sessions = len(focus_sessions)

    completed_focus_sessions = sum(
        1
        for session in focus_sessions
        if session.get("completed", False)
    )

    total_focus_duration = sum(
        session["duration"]
        for session in focus_sessions
    )

    if total_focus_sessions > 0:
        average_focus_duration = (
            total_focus_duration / total_focus_sessions
        )
    else:
        average_focus_duration = 0


    # =========================
    # NOTES OVERVIEW
    # =========================

    total_notes = len(notes)


    # =========================
    # DISPLAY DASHBOARD
    # =========================

    print("\n📋 TASKS")
    print("-" * 55)
    print(f"Total Tasks          : {total_tasks}")
    print(f"Completed Tasks      : {completed_tasks}")
    print(f"Pending Tasks        : {pending_tasks}")
    print(f"Completion Rate      : {task_completion_rate:.2f}%")


    print("\n📚 STUDY")
    print("-" * 55)
    print(f"Study Sessions       : {total_study_sessions}")
    print(f"Total Study Time     : {total_study_duration} minutes")
    print(f"Average Session      : {average_study_duration:.2f} minutes")


    print("\n🎯 GOALS")
    print("-" * 55)
    print(f"Total Goals          : {total_goals}")
    print(f"Completed Goals      : {completed_goals}")
    print(f"Pending Goals        : {pending_goals}")
    print(f"Completion Rate      : {goal_completion_rate:.2f}%")


    print("\n🔥 HABITS")
    print("-" * 55)
    print(f"Total Habits         : {total_habits}")
    print(f"Completed Habits     : {completed_habits}")
    print(f"Pending Habits       : {pending_habits}")


    print("\n⏱️ FOCUS")
    print("-" * 55)
    print(f"Focus Sessions       : {total_focus_sessions}")
    print(f"Completed Sessions   : {completed_focus_sessions}")
    print(f"Total Focus Time     : {total_focus_duration} minutes")
    print(f"Average Session      : {average_focus_duration:.2f} minutes")


    print("\n📝 NOTES")
    print("-" * 55)
    print(f"Total Notes          : {total_notes}")


    print("\n" + "=" * 55)
    print("              END OF DASHBOARD")
    print("=" * 55)