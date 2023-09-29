import pandas as pd

# Sample DataFrame
data = {
    'user_phone': ['User1', 'User1', 'User2', 'User2', 'User3'],
    'jenis_program_satu': ['Program A', 'Program B', 'Program A', 'Program B', 'Program A'],
    'Choice': [1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# Group by 'user_phone' and 'jenis_program_satu', and calculate the sum of 'Choice'
program_type_analysis = df.groupby(['user_phone', 'jenis_program_satu'])['Choice'].sum().reset_index()

# Display the result
print(program_type_analysis)
