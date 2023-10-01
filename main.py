import pandas as pd

df = pd.read_csv("data\conjoint_survey_ads.csv")
ds = pd.read_csv("data\conjoint_survey_organic.xlsx - Sheet1.csv")

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


df_2_q1 = pd.DataFrame({ "skill" : ["Create Analytics Dashboard", "Perform Customer Segmentation", "Design AB Test Experimentation"], 
          "bentuk_program": ["Tutorial Based", "Mentoring Based", "Mentoring Based"],
          "harga_program": ["500.000", "350.000", "350.000"]})
        
opsi_1 = ["A", "B", "C"]
opsi_n = {"A" : "Create Analytics Dashboard", "B": "Perform Customer Segmentation", "C":"Design AB Test Experimentation"}

opsi_n_soal_1 = {"A" : ["Create Analytics Dashboard", "Tutorial Based", "500.000"], "B": ["Perform Customer Segmentation", "Mentoring Based", "350.000"], "C":["Design AB Test Experimentation", "Mentoring Based", "350.000"]}
opsi_n_soal_2 = {"A" : ["Create Analytics Dashboard", "Tutorial Based", "500.000"], "B": ["Design Data Pipeline", "Mentoring Based", "300.000"], "C":["Perform Credit Scoring Analytics", "Mentoring Based", "550.000"]}
opsi_n_soal_3 = {"A" : ["Perform Credit Scoring Analytics", "Mentoring Based", "350.000"], "B": ["Perform Customer Segmentation", "Tutorial Based", "450.000"], "C":["Design Data Pipeline", "Mentoring Based", "250.000"]}
opsi_n_soal_4 = {"A" : ["Design AB Test Experimentation", "Mentoring Based", "500.000"], "B": ["Perform Price Optimization", "Mentoring Based", "350.000"], "C":["Perform Credit Scoring Analytics", "Mentoring Based", "350.000"]}
opsi_n_soal_5 = {"A" : ["Design Data Pipeline", "Mentoring Based", "400.000"], "B": ["Perform Customer Lifetime Analysis", "Tutorial Based", "300.000"], "C":["Design AB Test Experimentation", "Tutorial Based", "300.000"]}
opsi_n_soal_6 = {"A" : ["Perform Churn Analytics", "Tutorial Based", "450.000"], "B": ["Perform Customer Segmentation", "Mentoring Based", "300.000"], "C":["Create Machine Learning Model", "Mentoring Based", "550.000"]}
opsi_n_soal_7 = {"A" : ["Perform Customer Lifetime Analysis", "Tutorial Based", "500.000"], "B": ["Design Data Pipeline", "Mentoring Based", "550.000"], "C":["Deploy Machine Learning Model", "Tutorial Based", "350.000"]}
opsi_n_soal_8 = {"A" : ["Perform Credit Scoring Analytics", "Mentoring Based", "300.000"], "B": ["Design Data Pipeline", "Mentoring Based", "550.000"], "C":["Create Machine Learning Model", "Tutorial Based", "350.000"]}
opsi_n_soal_9 = {"A" : ["Create Analytics Dashboard", "Mentoring Based", "250.000"], "B": ["Design AB Test Experimentation", "Tutorial Based", "550.000"], "C":["Perform Customer Lifetime Analysis", "Tutorial Based", "350.000"]}
opsi_n_soal_10 = {"A" : ["Perform Credit Scoring Analytics", "Mentoring Based", "400.000"], "B": ["Perform Churn Analytics", "Mentoring Based", "450.000"], "C":["Perform Churn Analytics", "Tutorial Based", "500.000"]}

jenis_to_opsi_n = {
    'soal_1': opsi_n_soal_1,
    'soal_2': opsi_n_soal_2,
    'soal_3': opsi_n_soal_3,
    'soal_4': opsi_n_soal_4,
    'soal_5': opsi_n_soal_5,
    'soal_6': opsi_n_soal_6,
    'soal_7': opsi_n_soal_7,
    'soal_8': opsi_n_soal_8,
    'soal_9': opsi_n_soal_9,
    'soal_10': opsi_n_soal_10,
}

column_names = ["User_Phone", "Choice", "Skill", "Bentuk_Program", "Harga_Program"]

output_lines = []

output_lines.append(",".join(column_names))

for index, kotak_aja in kotak_2.iterrows():
    opsi = kotak_aja['Responses'].split(', ')
    jenis = kotak_aja['Questions']
    identitas = kotak_aja['user_phone']
    current_opsi_n = jenis_to_opsi_n.get(jenis, {})
    for y in opsi_1:
        for key, value in current_opsi_n.items():
            if y in opsi:
                if y == key:
                    #print(f"1 {y} {opsi} {jenis} {identitas} {value}")
                    output_lines.append(f"{identitas},1,{value}")
                else:
                    #print(f"0 {y} {opsi} {jenis} {identitas} {value}")
                    output_lines.append(f"{identitas},0,{value}")


csv_file_path = r"C:\Users\albar\Documents\GitHub\dw-productsurvey\Output\clean_version(1).csv"


with open(csv_file_path, "w") as csv_file:
    csv_file.write("\n".join(output_lines))

print(f"Output written to {csv_file_path}")