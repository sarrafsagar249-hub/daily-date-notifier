from datetime import datetime
import pytz
import nepali_datetime

# India Time
india_timezone = pytz.timezone("Asia/Kolkata")
india_now = datetime.now(india_timezone)

# Nepal Time
nepal_now = nepali_datetime.date.today()

# India Date
india_date = india_now.strftime("%A, %d %B %Y")

# Nepal Date
nepal_date = nepal_now.strftime("%K %d, %N %Y")

# Day
day = india_now.strftime("%A")

print("Today's Date")

print("---------------------------")

print("🇳🇵 Nepal (BS)")
print(nepal_date)

print()

print("🇮🇳 India (AD)")
print(india_date)

print()

print("Day:", day)
