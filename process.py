from models import Contributor, Resource
import sys

class ProcessError(Exception):
    pass

def process_contributor(command_parts, contributors):
    if len(command_parts) != 2:
        raise ProcessError("Contributor command requires exactly one argument.")
    name = command_parts[1]
    if name not in contributors:
        contributors[name] = Contributor(name)
    else:
        raise ProcessError(f"Contributor '{name}' is already registered.")

def process_resource(command_parts, contributors):
    if len(command_parts) != 4:
        raise ProcessError("Resource command requires exactly three arguments.")
    name, resource_id, rating = command_parts[1], command_parts[2], int(command_parts[3])
    if rating > 2:
        if name in contributors:
            contributors[name].resources[resource_id] = Resource(resource_id, rating)
        else:
            raise ProcessError(f"Contributor '{name}' not found.")
    else:
        print(f"Resource ID with ID '{resource_id}' and rating {rating} skipped because rating is too low. ")

def process_download(command_parts, contributors):
    if len(command_parts) != 3:
        raise ProcessError("Download command requires exactly two arguments.")
    resource_id, date = command_parts[1], command_parts[2]
    if date.startswith("2020"):
        for contributor in contributors.values():
            if resource_id in contributor.resources:
                contributor.resources[resource_id].downloads.append(date)
                break
    else:
        print(f"Download for resource ID '{resource_id}' on date '{date}' skipped because it is not within 2020.")

def process_commands():
    contributors = {}
    for line in sys.stdin:
        command_parts = line.strip().split()
        if not command_parts:
            continue
        command_type = command_parts[0]
        try:
            if command_type == "Contributor":
                process_contributor(command_parts, contributors)
            elif command_type == "Resource":
                process_resource(command_parts, contributors)
            elif command_type == "Download":
                process_download(command_parts, contributors)
            else:
                raise ProcessError(f"Unknown command '{command_type}'.")
        except ValueError as err:
            raise ProcessError(f"Invalid data format: {err}")
    return contributors