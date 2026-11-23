total = int(input ('total seconds '))
hours = total // 3600
minutes = (total // 3600) // 60
seconds = (total // 3600 // 60) // 60
print (f"{hours}:{minutes:02d}:{seconds:02d}")
