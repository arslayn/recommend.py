import pandas as pd
import random

# Define lists for data generation
college_names = [
    "Indian Institute of Technology",
    "St. Xavier's College",
    "Indian Institute of Science",
    "National Institute of Fashion Technology",
    "Indian Institute of Management",
    "Anna University",
    "Jamia Millia Islamia",
    "Birla Institute of Technology",
    "Loyola College",
    "Panjab University",
    "Manipal University",
    "Vellore Institute of Technology",
    "Indian School of Business",
    "Tata Institute of Social Sciences",
    "Symbiosis International University",
    "University of Delhi",
    "Jawaharlal Nehru University",
    "University of Mumbai",
    "Banaras Hindu University",
    "University of Calcutta"
]

fields_of_study = [
    "Engineering",
    "Arts",
    "Science",
    "Design",
    "Management",
    "Social Science",
    "Commerce",
    "Law",
    "Medicine",
    "Hospitality"
]

locations = [
    "Mumbai", "Kolkata", "Bangalore", "New Delhi", "Ahmedabad",
    "Chennai", "Ranchi", "Chandigarh", "Hyderabad", "Pune",
    "Jaipur", "Lucknow", "Coimbatore", "Nagpur", "Visakhapatnam",
    "Surat", "Patna", "Bhopal", "Indore", "Vadodara"
]

# Generate data
data = []
for _ in range(150):
    college_name = random.choice(college_names)
    field_of_study = random.choice(fields_of_study)
    average_grade = random.randint(70, 95)  # Random average grade between 70 and 95
    location = random.choice(locations)
    data.append([college_name, field_of_study, average_grade, location])

# Create DataFrame
df = pd.DataFrame(data, columns=["college_name", "field_of_study", "average_grade", "location"])

# Save to CSV
df.to_csv("college_data_india.csv", index=False)