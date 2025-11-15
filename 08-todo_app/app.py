import time
import json

FILE_NAME = "todo_list.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}


def save_tasks(tasks):
    print("saving tasks:")
    print(tasks)
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed saving tasks.")


def view_tasks(tasks):
    task_list = tasks["tasks"]

    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("\nYour To-Do list:\n")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["completed"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        print(tasks)
        save_tasks(tasks)
        print("Task added")
    else:
        print("Description cannot be empty.")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: ").strip())
        print(task_number)
        print(len(tasks["tasks"]))

        if 1 <= task_number <= len(tasks["tasks"]):
            # if 1 <= task_number and task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["completed"] = True
            print(tasks)
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")


if __name__ == "__main__":
    #    save_tasks({"tasks": ["task 3", "task 4"]})
    tasks = load_tasks()
    print(tasks)

    while True:
        print("\nTo-do List Manager:")
        print("1. View Tasks")
        print("2. Add task")
        print("3. Task completed")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("GoodBye!!")
            break
        else:
            print("\nInvalid choice, try again.\n")
            time.sleep(2)
