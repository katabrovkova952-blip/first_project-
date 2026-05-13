seconds = int(input("Enter a seconds: "))
minute = seconds // 60
hour = minute // 60
minute = minute - (hour * 60)
second = seconds % 60
days = hour // 24
hour = hour - (days * 24)
hour = str(hour).zfill(2)
minute = str(minute).zfill(2)
second = str(second).zfill(2)
if 11 <= days % 100 <= 14:
    result = "днів"
elif days % 10 == 1:
    result = "день"
elif 2 <= days % 10 <= 4:
    result = "дні"
else:
    result = "днів"
print(f"{days} {result}, {hour}:{minute}:{second}")
