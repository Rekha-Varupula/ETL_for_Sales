# transformation.py

import pandas as pd
def transform_data(df):
    # Perform data cleaning and transformations here (if needed)
    
    # Displays info of count of non-null rows for each column
    print("Display Non-null row count and data type for each column")
    df.info()
    
    # Combine both the ADDRESSLINE1 and ADDRESSLINE2 columns into a single column "ADDRESS"
    df["ADDRESS"] = df["ADDRESSLINE1"].fillna(' ') + "  " + df["ADDRESSLINE2"].fillna('')   

    # Combine both the CONTACTFIRSTNAME and CONTACTLASTNAME columns into a single column "CONTACT"
    df["CONTACTNAME"]= df["CONTACTFIRSTNAME"].fillna(' ') + "  " + df["CONTACTLASTNAME"].fillna(' ')

    # Drop the unnecessary columns
    df.drop(['ORDERLINENUMBER','QTR_ID','PHONE','PRODUCTCODE','STATE','POSTALCODE','TERRITORY','ADDRESSLINE1','ADDRESSLINE2','CONTACTFIRSTNAME','CONTACTLASTNAME'], axis=1, inplace=True)
    print("Data after dropping unnecessary columns")
    display(df)

    # Transform all the values of DATE column to DATE format
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    print("Transformed DATE column to a date format")
    df.head(20)

    # To find any null values
    Find_null_values= df[df.isna().any(axis=1)]     
    Find_null_values.head(20)

    # Duplicate rows count
    df.duplicated(keep='first').sum() 


    transformed_df = df.copy()
    return transformed_df
