# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Daily Rainfall Average — With Input Validation
# DATE WRITTEN: Fall 2020
# UPDATED:      2026 — removed unused toFixed() and spaces1 variable,
#                      cleaned up comments, fixed filename prompt,
#                      added get_yes_no() so invalid responses are rejected
#
# PURPOSE: Use a WHILE loop to collect daily rainfall amounts with their
#          day and date, validate input data, calculate the average rainfall,
#          and write the results to a user-named external text file.
#
# IMPROVEMENT OVER BASIC VERSION:
#   Added nested while loop with try/except to validate rainfall input.
#   Rejects: non-numeric values, negative values, values over 60 inches.
#   Added get_yes_no() to validate the y/n loop control variable.

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
out_file.write("=" * 75 + "\n")
out_file.write("NAME OF DAY & DATE             RAINFALL [INCHES]\n")
out_file.write("=" * 75 + "\n")

# ============================================================
# Initialize loop control variable (lcv) answer
answer = get_yes_no("Do you wish to enter a rainfall amount, along with the day and date?\n"
                    "[Type 'y' or 'Y' for yes — Otherwise, type no for NO]")

# ============================================================
# WHILE LOOP — test the lcv answer
while answer == "y":

    # Input day and date of the rainfall
    day_date = input("Enter the Name of the Day and Date of the Rainfall [e.g. Monday 2-12-20]\n")

    # Enter the actual rainfall amount
    print(f"What is the rainfall amount in inches on {day_date}?\n"
          "[Enter as positive value between 0 and 60, decimals allowed e.g. 2.58]")

    # Check data type for positive data entry — nested validation loop
    while True:
        try:
            rainfall = float(input())
        except ValueError:
            print("Wrong data type entered — Enter a value between 0 and 60.\n")
            continue
        if rainfall < 0:
            print("Negative value entered — Re-enter a positive numeric value.\n")
            continue
        elif rainfall > 60:
            print("Value exceeds maximum (60 inches) — Re-enter a valid rainfall amount.\n")
            continue
        else:
            break  # Valid input received

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
out_file.write("=" * 75 + "\n")
rainfall_avg = sum_rainfall / (count - 1)
out_file.write("count = " + format(count - 1, "2d") + "\n")
out_file.write("THE AVERAGE RAINFALL AMOUNT = " + format(rainfall_avg, "6.2f") + " INCHES\n")
out_file.write("=" * 75 + "\n")

out_file.close()
print(f"Results written to {file_name}")

# END PROGRAM
