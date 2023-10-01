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


df_2_q1 = pd.DataFrame({ "skill" : ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation", ], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "350.000", "350.000"]})
        
opsi_1 = ["A", "B", "C"]
opsi_1_skill = ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"]
opsi_n = {"A" : "Create Analytics Dashboard", "B": "Perform Customer Segmentation", "C":"Design AB Test Experimentation"}

data_list = []


for index, kotak_aja in kotak_2.iterrows():
    opsi = kotak_aja['Responses'].split(', ')
    jenis = kotak_aja['Questions']
    identitas = kotak_aja['user_phone']
    for y in opsi_1:
        for key, value in opsi_n.items():
            choice = 1 if y in opsi else 0
            if y in opsi:
                if y == key:
                    data = {
                        'User_phone': identitas,
                        'Choice': choice,
                        'Soal': jenis,
                        'Varian': y,
                        'Jawaban': ', '.join(opsi)
                    }
                    data_list.append(data) 

df_result = pd.DataFrame(data_list)
result_1 = pd.concat([df_result, df_2_q1], axis=1)
print(result_1)

'''
for index, kotak_aja in kotak_2.iterrows():
    opsi = kotak_aja['Responses'].split(', ')
    jenis = kotak_aja['Questions']
    identitas = kotak_aja['user_phone']
    for y in opsi_1:
        for key, value in opsi_n.items():
            choice = 1 if y in opsi else 0
            if y in opsi:
                if y == key:
                    data = {
                        'User_phone': identitas,
                        'Choice': choice,
                        'Soal': jenis,
                        'Varian': y,
                        'Jawaban': ', '.join(opsi)
                        }  
                    data_list.append(data)  # Append the dictionary to the list
            # result = {"user_phone" : identitas, "choice" : 1, "skill" : skill, "bentuk_program": bentuk, harga_program": price,}
            #print(f"1 {y} {opsi} {jenis} {identitas}")
        #else:
            
            #print(f"0 {y} {opsi} {jenis} {identitas}")
'''