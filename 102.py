import jdatetime

# test = str(jdatetime.datetime.now())
# test2 = test.split(" ")
# print(test2)

shamsi1 = str(jdatetime.date.fromgregorian(day=5, month=1, year=2009))
shamsi2 = str(jdatetime.date.fromgregorian(day=28, month=12, year=2005))

date1 = shamsi1.split("-")
date2 = shamsi2.split("-")
print(f"Parsa motevaled rooz {date1[2]} az mah {date1[1]} az sal {date1[0]} ast")
print(f"Amirali motevaled rooz {date2[2]} az mah {date2[1]} az sal {date2[0]} ast")
