import pandas as pd

# Read the survey data
df = pd.read_csv("C:\\Users\\albar\\Documents\\GitHub\\dw-productsurvey\\conjoint_survey_ads.csv")
ds = pd.read_csv("C:\\Users\\albar\\Documents\\GitHub\\dw-productsurvey\\conjoint_survey_organic.xlsx - Sheet1.csv")

# Concatenate the dataframes
result = pd.concat([df, ds], ignore_index=True)

# Rename columns
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

# Drop the "Timestamp" column
renaming_2 = renaming.drop(columns="Timestamp")

# Melt the dataframe to long format
kotak_1 = renaming_2.melt(id_vars="user_phone", var_name="Questions", value_name="Responses")

# Define the question order
question_order = [
    'soal_1', 'soal_2', 'soal_3', 'soal_4', 'soal_5',
    'soal_6', 'soal_7', 'soal_8', 'soal_9', 'soal_10'
]

# Categorize the "Questions" column
kotak_1['Questions'] = pd.Categorical(kotak_1['Questions'], categories=question_order, ordered=True)

# Sort the dataframe
kotak_2 = kotak_1.sort_values(by=["user_phone", "Questions"])

# Replace responses
kotak_2["Responses"].replace({"D. Tidak memilih semua product": "D"}, inplace=True)

# Split and join responses
kotak_2['Responses'] = kotak_2['Responses'].str.split(', ').apply(lambda x: ', '.join(x))

# Create a list to store choices
choice = []

# Define dataframes for questions
df_2_q1 = pd.DataFrame({
    "skill": ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"],
    "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
    "harga_program": ["500.000", "350.000", "350.000"]
})

df_2_q2 = pd.DataFrame({
    "skill": ["Create Analytics Dashboard", "Design Data Pipeline", "Perform Customer Segmentation"],
    "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
    "harga_program": ["500.000", "300.000", "550.000"]
})

df_2_q3 = pd.DataFrame({
    "skill": ["Perform Customer Segmentation", "Design Data Pipeline", "Perform Customer Segmentation"],
    "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
    "harga_program": ["500.000", "300.000", "550.000"]
})

# Iterate through the rows and assign choices
for index, row in kotak_2.iterrows():
    response = row["Responses"]
    if 'A' in response or 'A, B' in response or 'A, C' in response:
        choice.append(1)
    elif response == 'B':
        choice.append(1)
    elif response == 'C':
        choice.append(1)
    else:
        choice.append(0)

# Add the choice column to kotak_2
kotak_2['choice'] = choice

# Merge kotak_2 with df_2_q1 based on the "skill" column
merge = kotak_2.merge(df_2_q1, on="skill", how="left")

# Display the merged DataFrame
print(merge)
