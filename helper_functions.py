import pandas as pd


def data_clean(df):
    df_tmp = df[["Main Option", "Enquiry", "Fares", "Resolved", "Others", "Res_Amenities_s",
                 "Res_lost_found", "SUG & COMPLNT", "Suggestion", "Complaint", "Res_sug_complai",
                 "Fares - Email id", "Suggestion on fares", "Complaint on Fare", "Fare_suggestion/Complaint",
                 "Survey", "Res_Station/train", "Complaint_Email Id"]].copy()
    df_tmp.drop(axis=1, columns=["Fares - Email id", "Complaint_Email Id"],
                inplace=True)
    df_tmp.fillna("", inplace=True)
    return df_tmp


def preprocess(df):
    a = list(map(lambda x: "complaint_on_fare" if len(x) != 0 else "", df['Complaint on Fare']))
    df['Complaint on Fare'] = pd.Series([""] + a)
    a = list(map(lambda x: "suggestion_on_fare" if len(x) != 0 else "", df['Suggestion on fares']))
    df['Suggestion on fares'] = pd.Series([""] + a)

    final = []
    for j in range(len(df)):
        arr = []
        for item in df.iloc[j]:
            if item == "":
                continue
            arr.append(item.split(","))

        arr1 = []
        for i in range(5):
            sentence = ''
            for item in arr:
                if i > len(item) - 1:
                    continue
                if item[i] != "Others" and item[i] != "Go back to Main Menu" and item[
                    i] != "Go back to previous menu" and item[i] != "Yes" and item[i] != "No":
                    sentence += item[i] + " "
            if len(sentence) != 0:
                arr1.append(sentence.strip())
        final.append(arr1)

    return final
