import pandas as pd

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

# Define DataFrames for question choices
question_choices = {
    'soal_1': ['A', 'B', 'C', 'D'],
    'soal_2': ['A', 'B', 'C', 'D'],
    'soal_3': ['A', 'B', 'C', 'D'],
    'soal_4': ['A', 'B', 'C', 'D'],
    'soal_5': ['A', 'B', 'C', 'D'],
    'soal_6': ['A', 'B', 'C', 'D'],
    'soal_7': ['A', 'B', 'C', 'D'],
    'soal_8': ['A', 'B', 'C', 'D'],
    'soal_9': ['A', 'B', 'C', 'D'],
    'soal_10': ['A', 'B', 'C', 'D']
}

# Count responses for each question and user_phone
for user_phone in kotak_2['user_phone'].unique():
    user_data = kotak_2[kotak_2['user_phone'] == user_phone]
    user_choices = {}
    
    for question, options in question_choices.items():
        user_choices[question] = {option: 0 for option in options}
    
    for _, row in user_data.iterrows():
        response = row['Responses']
        question = row['Questions']
        
        if response in question_choices[question]:
            user_choices[question][response] += 1
    
    choices.append({
        'user_phone': user_phone,
        **{f"{question}_count": user_choices[question][response] for question in question_choices for response in question_choices[question]}
    })

# Create the final DataFrame
choices_df = pd.DataFrame(choices)

# Print the final DataFrame
print(choices_df)
