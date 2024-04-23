from process import process_commands, ProcessError
from statistics import calculate_statistics

def main():
    try:
        contributors = process_commands()
        calculate_statistics(contributors)
    except ProcessError as pe:
        print(f"Error processing commands: {pe}")
    except ValueError as ve:
        print(f"Error calculating statistics: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()