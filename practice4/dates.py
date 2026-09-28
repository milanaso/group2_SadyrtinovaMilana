from datetime import datetime, timedelta


# 1. Subtract five days from current date

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("Current date:", today.date())
print("Five days ago:", five_days_ago.date())


# 2. Print yesterday, today and tomorrow

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


# 3. Drop microseconds from datetime

current_datetime = datetime.now()

without_microseconds = current_datetime.replace(microsecond=0)

print("Original:", current_datetime)
print("Without microseconds:", without_microseconds)


# 4. Calculate difference between two dates in seconds

date1 = datetime(2026, 1, 1, 12, 0, 0)
date2 = datetime(2026, 1, 2, 12, 0, 0)

difference = date2 - date1

print("Difference in seconds:", difference.total_seconds())