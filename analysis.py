import pandas as pd

# Assuming 'your_dataset.csv' is the path to your CSV file
df = pd.read_csv('dataset.csv')

user_input = ['OPEN', 'Computer Engineering', '2022', '85']
c = user_input[0]
d = user_input[1]
y = int(user_input[2])  # Convert 'Year' to an integer

# Convert 'Category' and 'department' to lowercase and remove spaces
user_input[0] = c.lower().replace(' ', '')
user_input[1] = d.lower().replace(' ', '')

# Define ranges and corresponding labels
ranges = [(60, 70), (70, 75), (75, 80), (80, 85), (85, 90), (90, 100)]
labels = ['60-70', '70-75', '75-80', '80-85', '85-90', '90-100']

# Find the matching range label
matching_label = None
for r, label in zip(ranges, labels):
    if r[0] <= int(user_input[3]) < r[1]:
        matching_label = label
        break

# Filter the dataset based on the user-input criteria and matching range
if matching_label:
    filtered_df = df[
        (df['Category'].str.lower().str.replace(' ', '') == user_input[0]) &
        (df['department'].str.lower().str.replace(' ', '') == user_input[1]) &
        (df['Year'] == y) &
        (df['MHT_CET_Percentile'].between(*ranges[labels.index(matching_label)]))
    ]

    # Extract the Collage_name and MHT_CET_Percentile columns for the matching records
    matching_data = filtered_df[['Collage_name', 'MHT_CET_Percentile']]

    # Print the matching data
    if not matching_data.empty:
        print("Matching Colleges:")
        for i, (college_name, percentile) in enumerate(matching_data.itertuples(index=False), 1):
            print(f"Sr. No.: {i}, Category: {user_input[0].upper()}, Department: {user_input[1].upper()}, College Name: {college_name}, MHT_CET_Percentile: {percentile}")
    else:
        print("No colleges found for the specified criteria.")
else:
    print("MHT_CET_Percentile value does not fall within predefined ranges.")
