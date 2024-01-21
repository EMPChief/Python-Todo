import json
from pathlib import Path

class FileOperations:
    # Set the filename relative to the Python-Todo directory
    filename = Path("db/db.json")

    @staticmethod
    def initialize_tasks():
        if not FileOperations.filename.exists():
            # Create the db directory if it doesn't exist
            FileOperations.filename.parent.mkdir(parents=True, exist_ok=True)
            # Create an empty JSON file
            with FileOperations.filename.open("w") as file:
                json.dump([], file)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file)
