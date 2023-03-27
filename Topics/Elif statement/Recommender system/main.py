age = int(input())

if age <= 16:
    recommendation = "Lion King"
elif age <= 25:
    recommendation = "Trainspotting"
elif age <= 40:
    recommendation = "Matrix"
elif age <= 60:
    recommendation = "Pulp Fiction"
else:
    recommendation = "Breakfast at Tiffany's"

print(recommendation)