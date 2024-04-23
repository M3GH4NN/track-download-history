from datetime import datetime

def calculate_statistics(contributors):
    if not contributors:
        raise ValueError("No contributors data to process")
    
    results = {}
    for name, contributor in contributors.items():
        total_downloads = sum(len(res.downloads) for res in contributor.resources.values())
        first_date = datetime(2020, 1, 1)
        last_date = datetime(2020, 12, 31)
        days = (last_date - first_date).days + 1
        if total_downloads > 0:
            avg_downloads = total_downloads / days if days > 0 else 0
            results[name] = (total_downloads, round(avg_downloads, 3))
    if not results:
        print("No downloads to report for 2020.")
    else:
        for name, stats in sorted(results.items(), key=lambda item: item[1][0], reverse=True):
            print(f"{name}: {stats[0]} downloads, {stats[1]} downloads/day")