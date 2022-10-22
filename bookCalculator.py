# Program will ask for a word count and then will divide word count 
# by number of days to get a daily word count goal.


# Ask for word count goal
word_count = int(input("What is your word count goal? "))

# Ask for number of days
days = int(input("How many days do you have to write? "))

# Calculate daily word count
# FIX ME: Will move this to separate function file
daily_word_count = round(word_count / days)

# Print daily word count goal
print("Your daily word count goal is", daily_word_count, " per day. So get to writing!")
