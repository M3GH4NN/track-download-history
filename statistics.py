from datetime import datetime


def get_total_downloads(contributor):
    # Calculate the total number of downloads for a single contributor
    return sum(len(res.downloads) for res in contributor.resources.values())


def calculate_average_downloads(total_downloads):
    # Calculate the number of days in 2020 first
    first_date = datetime(2020, 1, 1)
    last_date = datetime(2020, 12, 31)
    days = (last_date - first_date).days + 1  # leap year
    if days > 0:
        return total_downloads / days
    return 0


def print_statistics(contributors_stats):
    # Print the statistics of all contributors
    if not contributors_stats:
        print("No downloads to report for 2020.")
        return
    for name, stats in sorted(
        contributors_stats.items(), key=lambda item: item[1][0], reverse=True
    ):
        print(f"{name}: {stats[0]} downloads, {stats[1]} downloads/day")


def calculate_statistics(contributors):
    # Calculate and print statistics for all contributors
    if not contributors:
        raise ValueError("No contributors data to process.")

    results = {}
    for name, contributor in contributors.items():
        total_downloads = get_total_downloads(contributor)
        if total_downloads > 0:
            avg_downloads = calculate_average_downloads(total_downloads)
            results[name] = (total_downloads, round(avg_downloads, 3))

    print_statistics(results)
