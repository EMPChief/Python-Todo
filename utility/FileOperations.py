import json
from pathlib import Path


"""File operations for task database.

This class provides methods for initializing the task 
database if it doesn't exist, loading tasks from the 
database, and saving tasks to the database.

The filename refers to a JSON file that will store the
task data.
"""


class FileOperations:
    filename = Path("db/db.json")

    @staticmethod
    def initialize_tasks():
        if not FileOperations.filename.exists():
            FileOperations.filename.parent.mkdir(parents=True, exist_ok=True)
            with FileOperations.filename.open("w") as file:
                json.dump([], file, indent=4)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file, indent=4)
