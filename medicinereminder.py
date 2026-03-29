import time
medicines=[]
n=int(input("How many medicines do you want to add?"))
for i in range(n):
  name=input("Enter medicine name: ")
  medtime=input("Enter time(HH:MM in 24hr format):")
  medicines.append((name,medtime))
print("\nReminder started...")
while True:
  currentime=time.strftime("%H:%M")
  for med in medicines:
    if med[1]==currentime:
        print(f"\nTime to take your medicine:{med[0]}")
  time.sleep(60)
