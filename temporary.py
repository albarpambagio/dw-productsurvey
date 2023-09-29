import pandas as pd
import numpy as np

# Read the survey data
df = pd.read_csv("conjoint_survey_ads.csv")
ds = pd.read_csv("conjoint_survey_organic.xlsx - Sheet1.csv")

# Concatenate the survey data
result = pd.concat([df, ds], ignore_index=True)

# Rename columns for clarity
renaming = result.rename(columns={
    '1. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_1',
    '2. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_2',
    '3. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_3',
    '4. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_4',
    '5. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_5',
    '6. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_6',
    '7. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_7',
    '8. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_8',
    '9. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_9',
    '10. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)': 'soal_10',
    'Berapa nomer telepon anda? Nomer ini akan digunakan untuk membagikan GoPay Rp 50.000 per orang, hasil undian untuk 100 orang. Kami hanya akan mengirimkan ke pengisi kuisioner yang valid, i.e. jawaban tidak random.': 'user_phone'
})

# Drop the 'Timestamp' column
renaming_2 = renaming.drop(columns="Timestamp")

# Melt the DataFrame
kotak_1 = renaming_2.melt(id_vars="user_phone", var_name="Questions", value_name="Responses")

# Define the order of questions
question_order = [
    'soal_1', 'soal_2', 'soal_3', 'soal_4', 'soal_5',
    'soal_6', 'soal_7', 'soal_8', 'soal_9', 'soal_10'
]

# Categorize the 'Questions' column
kotak_1['Questions'] = pd.Categorical(kotak_1['Questions'], categories=question_order, ordered=True)

# Sort the DataFrame
kotak_2 = kotak_1.sort_values(by=["user_phone", "Questions"])

# Create a list to store choices
choices = []

# Define DataFrame for question 1 choices
df_2_q1 = pd.DataFrame({
    "skill": ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"],
    "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
    "harga_program": ["500.000", "350.000", "350.000"]
})

# Debugging: Check for mismatched 'Responses' values
mismatched_responses_q1 = kotak_2[~kotak_2['Responses'].isin(df_2_q1['skill'])]
print("Mismatched Responses (Question 1):")
print(mismatched_responses_q1)

# Merge DataFrame for question 1 and fill missing values with NaN
merged_df_q1 = kotak_2.merge(df_2_q1, left_on='Responses', right_on='skill', how='left')

# Rename columns for question 1
merged_df_q1.rename(columns={
    'skill': 'jenis_program_satu',
    'bentuk_program': 'metode_program_satu',
    'harga_program': 'harga_program_satu'
}, inplace=True)

# Debugging: Check for mismatched 'Responses' values after merging
mismatched_responses_q1_after_merge = merged_df_q1[merged_df_q1['jenis_program_satu'].isna()]
print("Mismatched Responses After Merge (Question 1):")
print(mismatched_responses_q1_after_merge)

# Add the 'Choice' column based on the 'Responses' column for question 1
merged_df_q1['Choice'] = merged_df_q1['Responses'].apply(lambda x: 1 if 'A' in x or 'A, B' in x or 'A, C' in x else 0)

# Define DataFrame for question 2 choices
df_2_q2 = pd.DataFrame({
    "skill": ["Create Analytics Dashboard", "Design Data Pipeline", "Perform Customer Segmentation"],
    "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
    "harga_program": ["500.000", "300.000", "550.000"]
})

# Debugging: Check for mismatched 'Responses' values
mismatched_responses_q2 = kotak_2[~kotak_2['Responses'].isin(df_2_q2['skill'])]
print("\nMismatched Responses (Question 2):")
print(mismatched_responses_q2)

# Merge DataFrame for question 2 and fill missing values with NaN
merged_df_q2 = kotak_2.merge(df_2_q2, left_on='Responses', right_on='skill', how='left')

# Rename columns for question 2
merged_df_q2.rename(columns={
    'skill': 'jenis_program_dua',
    'bentuk_program': 'metode_program_dua',
    'harga_program': 'harga_program_dua'
}, inplace=True)

# Debugging: Check for mismatched 'Responses' values after merging
mismatched_responses_q2_after_merge = merged_df_q2[merged_df_q2['jenis_program_dua'].isna()]
print("\nMismatched Responses After Merge (Question 2):")
print(mismatched_responses_q2_after_merge)

# Add the 'Choice' column based on the 'Responses' column for question 2
merged_df_q2['Choice'] = merged_df_q2['Responses'].apply(lambda x: 1 if 'A' in x or 'A, B' in x or 'A, C' in x else 0)

# Concatenate both question 1 and question 2 DataFrames
final_merged_df = pd.concat([merged_df_q1, merged_df_q2], ignore_index=True)

# Sort the final DataFrame
final_merged_df.sort_values(by=["user_phone", "Questions"], inplace=True)

# Print the final DataFrame
print(final_merged_df)
