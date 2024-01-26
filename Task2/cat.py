import sys

def analyze_log(file_path):
    """
    Analyzes a cat log file to extract information about cat visits.

    Parameters:
        file_path (str): The path to the cat log file.

    Prints:
        - Cat visit statistics, including the number of cat visits, total time in the house, average visit length,
          longest visit, and shortest visit.
        - If the log file doesn't exist, a message is printed indicating the file could not be found.
        - If an unexpected error occurs during file processing, an error message is printed.

    """
    try:
        # Open the log file and read its lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Initialize variables for cat visit statistics
        cat_visits = 0
        other_cats = 0
        total_time = 0
        visit_lengths = []

        # Iterate through each line in the log file
        for line in lines:
            if line.strip() == 'END':
                break

            # Split the line into cat_type, entry_time, and exit_time
            data = line.strip().split(',')
            cat_type, entry_time, exit_time = data

            # Convert entry_time and exit_time to integers
            entry_time = int(entry_time)
            exit_time = int(exit_time)

            # Update statistics based on cat type
            if cat_type == 'OURS':
                cat_visits += 1
                total_time += exit_time - entry_time
                visit_lengths.append(exit_time - entry_time)
            elif cat_type == 'THEIRS':
                other_cats += 1

        # If no cat visits are found, print a message and return
        if cat_visits == 0:
            print("No cat visits found in the log file.")
            return

        # Calculate additional statistics
        average_visit_length = sum(visit_lengths) // cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)

        total_hours = total_time // 60
        total_minutes = total_time % 60

        # Print the analysis results
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}\n")
        print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
        print(f"Average Visit Length: {average_visit_length} Minutes")
        print(f"Longest Visit:        {longest_visit} Minutes")
        print(f"Shortest Visit:       {shortest_visit} Minutes\n")

    except FileNotFoundError:
        # Handle file not found error
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        # Handle other unexpected errors
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        # Analyze the cat log file specified in the command line argument
        analyze_log(sys.argv[1])
