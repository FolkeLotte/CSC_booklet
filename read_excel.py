import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Entries.xlsx')

# Create a LaTeX line for each row
lines = []
for index, row in df.iterrows():
    line = "\\DogCaptionAuto" + \
           "{" + str(row.iloc[0]) + "}" + \
           "{" + str(row.iloc[1]) + "}" + \
           "{" + str(row.iloc[2]) + "}" + \
           "{" + str(row.iloc[3]) + "}" + \
           "{" + str(row.iloc[4]) + "}" + \
           "{" + str(row.iloc[5]) + "}" + \
           "{" + str(row.iloc[6]) + "}" + \
           "{" + str(row.iloc[7]) + "}" + "\n"
    lines.append(line)

# Join all lines with newline characters
output = "\n".join(lines)

# Write the contents to entries.tex
with open('entries.tex', 'w') as f:
    f.write(output)

print("Successfully wrote to entries.tex")

# Display the DataFrame
print("DataFrame shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Optional: Display basic information about the DataFrame
print("\nDataFrame info:")
print(df.info())
