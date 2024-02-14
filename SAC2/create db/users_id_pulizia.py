import pandas as pd
import pandas as pd

def pulizia_users(work):
    if work == "Data Scientis":
        return "Data Scientist"
    return work

if __name__ == '__main__':
    df = pd.read_csv("users_edit.csv")
    df["Work"] = df["Work"].apply(pulizia_users)
    df.to_csv("new_users_edit.csv", index=False)

