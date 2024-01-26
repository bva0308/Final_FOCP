import sys

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        other_cats = 0
        total_time = 0
        visit_lengths = []

        for line in lines:
            if line.strip() == 'END':
                break

            data = line.strip().split(',')
            cat_type, entry_time, exit_time = data

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            if cat_type == 'OURS':
                cat_visits += 1
                total_time += exit_time - entry_time
                visit_lengths.append(exit_time - entry_time)
            elif cat_type == 'THEIRS':
                other_cats += 1

        if cat_visits == 0:
            print("No cat visits found in the log file.")
            return

        average_visit_length = sum(visit_lengths) // cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)

        total_hours = total_time // 60
        total_minutes = total_time % 60

        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}\n")
        print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
        print(f"Average Visit Length: {average_visit_length} Minutes")
        print(f"Longest Visit:        {longest_visit} Minutes")
        print(f"Shortest Visit:       {shortest_visit} Minutes\n")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f'An error occurred: {e}')



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        analyze_log(sys.argv[1])
