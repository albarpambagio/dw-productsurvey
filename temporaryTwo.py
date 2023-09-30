import pandas as pd

df = pd.read_csv("C:\\Users\\albar\\Documents\\GitHub\\dw-productsurvey\\conjoint_survey_ads.csv")
ds = pd.read_csv("C:\\Users\\albar\\Documents\\GitHub\\dw-productsurvey\\conjoint_survey_organic.xlsx - Sheet1.csv")

result = pd.concat([df, ds], ignore_index=True)
renaming = result.rename(columns= {'1. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_1',
       '2. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_2' ,
       '3. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_3',
       '4. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_4',
       '5. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_5',
       '6. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_6',
       '7. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_7',
       '8. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_8',
       '9. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_9',
       '10. Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)' : 'soal_10',
       'Berapa nomer telepon anda? Nomer ini akan digunakan untuk membagikan GoPay Rp 50.000 per orang, hasil undian untuk 100 orang. Kami hanya akan mengirimkan ke pengisi kuisioner yang valid, i.e. jawaban tidak random.' : 'user_phone'})
renaming_2 = renaming.drop(columns="Timestamp")
kotak_1 = renaming_2.melt(id_vars="user_phone", var_name="Questions", value_name="Responses")
question_order = [
    'soal_1', 'soal_2', 'soal_3', 'soal_4', 'soal_5',
    'soal_6', 'soal_7', 'soal_8', 'soal_9', 'soal_10']
kotak_1['Questions'] = pd.Categorical(kotak_1['Questions'], categories=question_order, ordered=True)
kotak_2 = kotak_1.sort_values(by= ["user_phone", "Questions"])
kotak_2["Responses"].replace({"D. Tidak memilih semua product": "D"}, inplace=True)
kotak_2['Responses'] = kotak_2['Responses'].str.split(', ').apply(lambda x: ', '.join(x))

choice = []


df_2_q1 = pd.DataFrame({"opsi" : ["A", "B", "C"],
          "skill" : ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "350.000", "350.000"]})
        
for index, row_kotak in kotak_2.iterrows():
    response = row_kotak["Responses"]
    match_found = False  # Flag to track if a match is found for this row
    for index, row_df in df_2_q1.iterrows():
        opsi = row_df["opsi"]
        if opsi in response.split(', '):  # Check if opsi is in the list of responses
            choice.append(1)
            match_found = True  # Set the flag to True if a match is found
            break  # Exit the inner loop once a match is found
    if not match_found:
        choice.append(0) 


# Add the 'choice' column to kotak_2
kotak_2['choice'] = choice

# Reset indices of both dataframes
kotak_2.reset_index(drop=True, inplace=True)
df_2_q1.reset_index(drop=True, inplace=True)

# Concatenate kotak_2 and df_2_q1
final_result = pd.concat([kotak_2, df_2_q1], axis=1)

# Print the final result
print(final_result)


'''
for index, row_kotak in kotak_2.iterrows():
    response = row_kotak["Responses"]
    match_found = False  # Flag to track if a match is found for this row
    for index, row_df in df_2_q1.iterrows():
        opsi = row_df["opsi"]
        if response == opsi:
            choice.append(1)
            match_found = True  # Set the flag to True if a match is found
            break  # Exit the inner loop once a match is found
    if not match_found:
        choice.append(0) 
'''

# merge = pd.concat([kotak_2, df_2_q1])
'''
for x in kotak_2.iterrows():
    if x["Responses"] == 'A':
        wadah.append(1)
    elif x["Responses"] == 'B':
        wadah.append(1)
    elif x["Responses"] == 'C':
        wadah.append(1)
    else:
        wadah.append(0)
'''

# Use DataFrame.transpose().iterrows()
'''
for (column_name, column) in df.transpose().iterrows():
    print (column_name)
'''


"""
# variasi opsi soal 1
# soalSatu = {"skill" : "", "bentuk_program": "","harga_program": ""}
soalSatuA = {"skill" : "Create Analytics Dashboard", "bentuk_program": "Tutorial Based","harga_program": "500.000"}
soalSatuB = {"skill" : "Perform Customer Segmentation", "bentuk_program": "Mentoring Based","harga_program": "350.000"}
soalSatuC = {"skill" : "Design AB Test Experimentation", "bentuk_program": "Mentoring Based","harga_program": "300.000"}

soalSatuA = {"skill" : "Create Analytics Dashboard", "bentuk_program": "Tutorial Based","harga_program": "500.000"}

"""
'''
df_2_q1 = pd.DataFrame({"skill" : ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "350.000", "350.000"]})


df_2_q1 = pd.DataFrame({"skill" : ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "350.000", "350.000"]})

df_2_q2 = pd.DataFrame({"skill" : ["Create Analytics Dashboard", "Design Data Pipeline", "Perform Customer Segmentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "300.000", "550.000"]})

df_2_q3 = pd.DataFrame({"skill" : ["Perform Customer Segmentation", "Design Data Pipeline", "Perform Customer Segmentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "300.000", "550.000"]})
'''

"""
soalSatuA = ["Create Analytics Dashboard", "Tutorial Based", "500.000"]
soalSatuB = ["Perform Customer Segmentation", "Mentoring Based", "350.000"]
soalSatuC = ["Design AB Test Experimentation", "Mentoring Based", "300.000"]
"""


"""
jenis_program_satu = ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"]
metode_program_satu = ["Tutorial Based", "Mentoring Based", "Mentoring Based"]
harga_program_satu = ["500.000", "350.000", "300.000"]
"""

'''
nested_df_2_q1 = pd.DataFrame({"A" : [{"skill" : "Create Analytics Dashboard"}, {"bentuk_program": "Tutorial Based"}, {"harga_program" : "500.000"}], 
                               "B" : [{"skill" : "Perform Customer Segmentation"}, {"bentuk_program": "Mentoring Based"}, {"harga_program" : "350.000"}], 
                               "C" : [{"skill" : "Design AB Test Experimentation"}, {"bentuk_program": "Mentoring Based"}, {"harga_program" : "300.000"}]
                                      })
                                      
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
'''