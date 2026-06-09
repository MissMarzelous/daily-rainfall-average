# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Daily Rainfall Average — Basic Version (No Input Validation)
# DATE WRITTEN: Fall 2020
# UPDATED:      2026 — removed unused toFixed(), fixed filename prompt,
#                      added get_yes_no() so invalid responses are rejected.
#                      See daily_rainfall_average_with_validation.py for
#                      the improved version with data validation.
#
# PURPOSE: Use a WHILE loop to collect daily rainfall amounts with their
#          day and date, calculate the average rainfall, and write the
#          results to a user-named external text file.
#
# NOTE: This is the basic version — no input validation on rainfall amounts.

# ============================================================
# Function to validate yes/no input — rejects anything that isn't y or no
def get_yes_no(prompt):
    while True:
        print(prompt)
        response = input().strip().lower()
        if response in ("y", "yes"):
            return "y"
        elif response in ("n", "no"):
            return "n"
        else:
            print("Invalid input. Please type 'y' for yes or 'no' to quit.")

# ============================================================
# Declare variables in alpha order
# Initialize processed variables used to calculate rainfall average
count = 1
rainfall_avg = 0.0
sum_rainfall = 0.0

# ============================================================
# Creating an external file to store output
file_name = input("Enter the filename where output will be written\n"
                  "Include the .txt extension (e.g. rainfall.txt) ---->\n")
out_file = open(file_name, "w")

# Display column headings
out_file.write("================================================================\n")
out_file.write("NAME OF DAY & DATE             RAINFALL [INCHES]\n")
out_file.write("================================================================\n")

# ============================================================
# Initialize loop control variable (lcv) answer
answer = get_yes_no("Do you wish to enter a rainfall amount, along with the day and date?\n"
                    "[Type 'y' or 'Y' for yes — Otherwise, type no for NO]")

# ============================================================
# WHILE LOOP — test the lcv answer
while answer == "y":

    # Input day and date of the rainfall
    print("Enter the Name of the Day and Date of the Rainfall [e.g. Monday 2-12-20]")
    day_date = input()

    # Enter the actual rainfall amount
    rainfall = float(input(f"What is the rainfall amount in inches on {day_date}?\n"
                           "[Enter as positive value, decimals allowed e.g. 2.58]\n"))

    # Keep a running sum or total of all rainfalls
    sum_rainfall = sum_rainfall + rainfall

    # Write day, date, and rainfall to output file
    out_file.write(format(day_date, "20s") + " " * 16 + format(rainfall, "6.2f") + "\n")

    # Update the lcv answer
    answer = get_yes_no("Do you wish to enter another rainfall amount?\n"
                        "[Type 'y' or 'Y' for yes — Otherwise, type no for NO]")

    # Count or tally the number of rainfalls entered
    count = count + 1
    # While Loop ends

# ============================================================
# Write summary to output file
out_file.write("================================================================\n")
out_file.write("count = " + format(count - 1, "2d") + "\n")
rainfall_avg = sum_rainfall / (count - 1)
out_file.write("THE AVERAGE RAINFALL AMOUNT = " + format(rainfall_avg, "6.2f") + " INCHES\n")
out_file.write("================================================================\n")

out_file.close()
print(f"Results written to {file_name}")

# END PROGRAM
