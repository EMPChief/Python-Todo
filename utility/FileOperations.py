import json
from pathlib import Path

class FileOperations:
    filename = Path("db/db.json")

    @staticmethod
    def initialize_tasks():
        if not FileOperations.filename.exists():
            FileOperations.filename.parent.mkdir(parents=True, exist_ok=True)
            with FileOperations.filename.open("w") as file:
                json.dump([], file)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file)
