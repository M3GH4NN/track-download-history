from models import Contributor, Resource
import sys


class ProcessError(Exception):
    pass

def process_commands():
    contributors = {}
    for line in sys.stdin:
        command_parts = line.strip().split()
        if not command_parts:
            continue  # skip empty lines
        command_type = command_parts[0]
        try:
            if command_type == "Contributor":
                if len(command_parts) != 2:
                    raise ProcessError(
                        "Contributor command requires exactly one argument."
                    )
                name = command_parts[1]
                if name not in contributors:
                    contributors[name] = Contributor(name)
                else:
                    raise ProcessError(f"Contributor '{name}' is already registered.")
            elif command_type == "Resource":
                if len(command_parts) != 4:
                    raise ProcessError(
                        "Resource command requires exactly three arguments."
                    )
                name, resource_id, rating = (
                    command_parts[1],
                    command_parts[2],
                    int(command_parts[3]),
                )
                if rating > 2:
                    if name in contributors:
                        contributors[name].resources[resource_id] = Resource(
                            resource_id, rating
                        )
                    else:
                        raise ProcessError(f"Contributor '{name}' not found.")
                else:
                    print(
                        f"Resource ID with ID '{resource_id}' and rating {rating} skipped because rating is too low. "
                    )
            elif command_type == "Download":
                if len(command_parts) != 3:
                    raise ProcessError(
                        "Download command requires exactly two arguments."
                    )
                resource_id, date = command_parts[1], command_parts[2]
                if date.startswith("2020"):
                    found = False
                    for contributor in contributors.values():
                        if resource_id in contributor.resources:
                            contributor.resources[resource_id].downloads.append(date)
                            found = True
                            break
                else:
                    print(
                        f"Download for resource ID '{resource_id}' on date '{date}' skipped because it is not within 2020."
                    )

            else:
                raise ProcessError(f"Unknown command '{command_type}'.")
        except ValueError as err:
            raise ProcessError(f"Invalid data format: {err}")
    return contributors
