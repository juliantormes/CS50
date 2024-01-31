import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    cumulative_cases = dict()
    new_cases = dict()

    # Create a dictionay of lists
    # where each state has its 14-day
    # values list
    for value in reader:
        state = str(value["state"])
        cases = int(value["cases"])

        # Initialize the dictionary value
        if state not in cumulative_cases:
            cumulative_cases[state] = list()

        # Append the first 14 values
        # if len(cumulative_cases[state]) != 14:
        cumulative_cases[state].append(cases)

    # Create a dictionary with new cases per day
    for state, cases in cumulative_cases.items():
        # Intilize the dictionary
        if state not in new_cases:
            new_cases[state] = list()
            new_cases[state].append(cases[0])

        # Compute the cases per day
        for i in range(1, len(cases)):
            diff = cases[i] - cases[i - 1]
            new_cases[state].append(diff)

    return new_cases

# Calculate and print out seven day average for given state
def comparative_averages(new_cases_data, selected_states):
    for state in selected_states:
        # Retrieve the list of new cases for the state.
        daily_new_cases = new_cases_data[state]

        # Initialize lists to store seven-day totals and averages.
        seven_day_totals = []
        seven_day_averages = []

        # Ensure there are enough data points.
        if len(daily_new_cases) >= 14:
            # Calculate the seven-day totals.
            for i in range(len(daily_new_cases) - 13):
                # Sum up the total new cases over a seven-day period.
                weekly_total = sum(daily_new_cases[i:i+7])
                seven_day_totals.append(weekly_total)

            # Calculate seven-day averages from the totals.
            for total in seven_day_totals:
                weekly_average = total / 7
                seven_day_averages.append(weekly_average) #Append = Add space in memory dynamiclly

            # Retrieve the last two seven-day averages.
            latest_week_avg = seven_day_averages[-1] # The - access the list from the back of it (-1) is the most recent
            previous_week_avg = seven_day_averages[-2] # The - access the list from the back of it (-2) is the 2nd most recent

            # Calculate the percentage change between the two seven-day averages.
            try:
                percent_change = ((latest_week_avg - previous_week_avg) / previous_week_avg) * 100
            except ZeroDivisionError:
                ...

            # Output the results.
            print(f"{state} had a 7-day average of {latest_week_avg:.2f} new cases.")
            if percent_change>0 :
                print(f"This is an increase of {percent_change:.2f}% from the previous week.\n")
            elif percent_change<0 :
                print(f"This is a decrease of {percent_change:.2f}% from the previous week.\n")
            else :
                print("There is no change from the previous week.")
        else:
            print(f"Not enough data available for {state} to calculate a 14-day trend.\n")



main()