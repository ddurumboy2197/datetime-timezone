from datetime import datetime
import zoneinfo

# Toshkent vaqt zonasi
toshkent_tz = zoneinfo.ZoneInfo('Asia/Toshkent')

# London vaqt zonasi
london_tz = zoneinfo.ZoneInfo('Europe/London')

# Hozirgi vaqtni olish
now = datetime.now(toshkent_tz)

# Toshkent va London vaqtini solishtirish
print(f"Toshkent vaqt: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"London vaqt: {now.astimezone(london_tz).strftime('%Y-%m-%d %H:%M:%S')}")
