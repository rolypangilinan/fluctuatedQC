#%%


# import pandas as pd

# dataList = []


# pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)


# # --- Load data ---
# file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# # LOAD CSV
# try:
#     df = pd.read_csv(file_path, encoding='latin1')
# except UnicodeDecodeError:
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# # Clean column names by stripping whitespace
# df.columns = df.columns.str.strip()


# # 1ST DATAFRAME (compiledFrame)
# emptyColumn = [
#     "DATE",
#     "TIME",
#     "MODEL CODE",
#     "TYPE",
#     "BARCODE",
#     "SERIAL No.",
#     "PASS/NG",

#     "50Hz WATTAGE"   # CANT DISPLAY
#     "50Hz WATTAGE FLUCTUATED"

#     # "50Hz AIR VOLUME",
#     # "50Hz AIR VOLUME PASS"

#     # "50Hz CLOSED PRESSURE",
#     # "50Hz CLOSED PRESSURE PASS",

#     # "50Hz AMPERAGE",
#     # "50Hz AMPERAGE PASS",

#     # "60Hz WATTAGE ",
#     # "60Hz WATTAGE PASS",

#     # "60Hz AIR VOLUME ",
#     # "60Hz AIR VOLUME PASS",

#     # "60Hz CLOSED PRESSURE ",
#     # "60Hz CLOSED PRESSURE PASS",

#     # "60Hz AMPERAGE",
#     # "60Hz AMPERAGE PASS"
# ]
# compiledFrame = pd.DataFrame(columns=emptyColumn)






# # --- CLEANING before loop ---
# df = df[(~df["MODEL CODE"].isin(['120HP1000M']))]
# df = df[(~df["MODEL CODE"].isin(['60CAT0203M']))]
# df = df[(~df["TYPE"].isin(['T']))]
# df = df[(~df["TYPE"].isin(['D']))]
# df = df[(~df["TYPE"].isin(['A']))]
# df = df[(~df["PASS/NG"].isin([0]))]








# # --- Custom loop FIRST (to populate compiledFrame) ---
# for a in range(len(df)):
#     print(f"ROW: {a}")
#     tempdf = df.iloc[[a]]
#     model_code = tempdf["MODEL CODE"].values[0]

#     dataFrame = {
#         "DATE": tempdf["DATE"].values[0],
#         "TIME": tempdf["TIME"].values[0],
#         "MODEL CODE": model_code,
#         "TYPE": tempdf["TYPE"].values[0],
#         "BARCODE": tempdf["BARCODE"].values[0],
#         "SERIAL No.": tempdf["SERIAL No."].values[0],
#         "PASS/NG": tempdf["PASS/NG"].values[0],
#         "50Hz WATTAGE": tempdf["50Hz WATTAGE"].values[0]
#         # "50Hz AIR VOLUME": tempdf["50Hz AIR VOLUME"].values[0]
#         # "50Hz CLOSED PRESSURE": tempdf["50Hz CLOSED PRESSURE"].values[0],
#         # "50Hz AMPERAGE": tempdf["50Hz AMPERAGE"].values[0],
#         # "60Hz WATTAGE": tempdf["60Hz WATTAGE"].values[0],
#         # "60Hz AIR VOLUME": tempdf["60Hz AIR VOLUME"].values[0],
#         # "60Hz CLOSED PRESSURE": tempdf["60Hz CLOSED PRESSURE"].values[0],
#         # "60Hz AMPERAGE": tempdf["60Hz AMPERAGE"].values[0]

#     }


# # PASS
# # SEPARATE PASS FROM NG
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["50Hz WATTAGE PASS"] = tempdf["50Hz WATTAGE"].values[0]    
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["50Hz AIR VOLUME PASS"] = tempdf["50Hz AIR VOLUME"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["50Hz CLOSED PRESSURE PASS"] = tempdf["50Hz CLOSED PRESSURE"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["50Hz AMPERAGE PASS"] = tempdf["50Hz AMPERAGE"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["60Hz WATTAGE PASS"] = tempdf["60Hz WATTAGE"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["60Hz AIR VOLUME PASS"] = tempdf["60Hz AIR VOLUME"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["60Hz CLOSED PRESSURE PASS"] = tempdf["60Hz CLOSED PRESSURE"].values[0]
#     # if tempdf["PASS/NG"].values[0] == 1:
#     #     dataFrame["60Hz AMPERAGE PASS"] = tempdf["60Hz AMPERAGE"].values[0]



#     dataList.append(dataFrame)

# dataFrame = pd.DataFrame(dataList)
# compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)


# # Add this at the end of your existing code (after the concat operation)

# # Export compiledFrame to CSV
# output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
# compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

# print(f"CSV file successfully saved to: {output_path}")


# %%

import pandas as pd

dataList = []

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


# --- Load data ---
file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# LOAD CSV
try:
    df = pd.read_csv(file_path, encoding='latin1')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# Clean column names by stripping whitespace
df.columns = df.columns.str.strip()


# 1ST DATAFRAME (compiledFrame)
emptyColumn = [
    "DATE",
    "TIME",
    "MODEL CODE",
    "TYPE",
    "BARCODE",
    "SERIAL No.",
    "PASS/NG",

    "50Hz WATTAGE",   # CANT DISPLAY
    "50Hz WATTAGE FLUCTUATED",

    "50Hz AIR VOLUME",
    "50Hz AIR VOLUME FLUCTUATED"

    # "50Hz CLOSED PRESSURE",
    # "50Hz CLOSED PRESSURE PASS",

    # "50Hz AMPERAGE",
    # "50Hz AMPERAGE PASS",

    # "60Hz WATTAGE ",
    # "60Hz WATTAGE PASS",

    # "60Hz AIR VOLUME ",
    # "60Hz AIR VOLUME PASS",

    # "60Hz CLOSED PRESSURE ",
    # "60Hz CLOSED PRESSURE PASS",

    # "60Hz AMPERAGE",
    # "60Hz AMPERAGE PASS"
]
compiledFrame = pd.DataFrame(columns=emptyColumn)

# --- CLEANING before loop ---
df = df[(~df["MODEL CODE"].isin(['120HP1000M']))]
df = df[(~df["MODEL CODE"].isin(['60CAT0203M']))]
df = df[(~df["TYPE"].isin(['T']))]
df = df[(~df["TYPE"].isin(['D']))]
df = df[(~df["TYPE"].isin(['A']))]
df = df[(~df["PASS/NG"].isin([0]))]

# Initialize variables to track previous values
previous_wattage = None
previous_fluctuation = None

# --- Custom loop FIRST (to populate compiledFrame) ---
for a in range(len(df)):
    print(f"ROW: {a}")
    tempdf = df.iloc[[a]]
    model_code = tempdf["MODEL CODE"].values[0]
    current_wattage = tempdf["50Hz WATTAGE"].values[0]
    
    # Calculate fluctuation
    if current_wattage == 0:
        fluctuation = 0
    elif previous_wattage is None:
        # First run - set default fluctuation
        fluctuation = 5.00
    else:
        fluctuation = abs(previous_wattage - current_wattage)
    
    dataFrame = {
        "DATE": tempdf["DATE"].values[0],
        "TIME": tempdf["TIME"].values[0],
        "MODEL CODE": model_code,
        "TYPE": tempdf["TYPE"].values[0],
        "BARCODE": tempdf["BARCODE"].values[0],
        "SERIAL No.": tempdf["SERIAL No."].values[0],
        "PASS/NG": tempdf["PASS/NG"].values[0],
        "50Hz WATTAGE": current_wattage,
        "50Hz WATTAGE FLUCTUATED": fluctuation,
        "50Hz AIR VOLUME": tempdf["50Hz AIR VOLUME"].values[0]
        # "50Hz CLOSED PRESSURE": tempdf["50Hz CLOSED PRESSURE"].values[0],
        # "50Hz AMPERAGE": tempdf["50Hz AMPERAGE"].values[0],
        # "60Hz WATTAGE": tempdf["60Hz WATTAGE"].values[0],
        # "60Hz AIR VOLUME": tempdf["60Hz AIR VOLUME"].values[0],
        # "60Hz CLOSED PRESSURE": tempdf["60Hz CLOSED PRESSURE"].values[0],
        # "60Hz AMPERAGE": tempdf["60Hz AMPERAGE"].values[0]
    }
    
    # Update previous values for next iteration
    previous_wattage = current_wattage
    previous_fluctuation = fluctuation

    dataList.append(dataFrame)

dataFrame = pd.DataFrame(dataList)
compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)

# Export compiledFrame to CSV
output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"CSV file successfully saved to: {output_path}")










# %%


# import pandas as pd

# dataList = []

# pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)


# # --- Load data ---
# file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# # LOAD CSV
# try:
#     df = pd.read_csv(file_path, encoding='latin1')
# except UnicodeDecodeError:
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# # Clean column names by stripping whitespace
# df.columns = df.columns.str.strip()


# # 1ST DATAFRAME (compiledFrame)
# emptyColumn = [
#     "DATE",
#     "TIME",
#     "MODEL CODE",
#     "TYPE",
#     "BARCODE",
#     "SERIAL No.",
#     "PASS/NG",

#     "50Hz WATTAGE",   # CANT DISPLAY
#     "50Hz WATTAGE FLUCTUATED",

#     "50Hz AIR VOLUME",
#     "50Hz AIR VOLUME FLUCTUATED",

#     "50Hz CLOSED PRESSURE",
#     "50Hz CLOSED PRESSURE FLUCTUATED"

#     # "50Hz AMPERAGE",
#     # "50Hz AMPERAGE FLUCTUATED",

#     # "60Hz WATTAGE ",
#     # "60Hz WATTAGE FLUCTUATED",

#     # "60Hz AIR VOLUME ",
#     # "60Hz AIR VOLUME FLUCTUATED",

#     # "60Hz CLOSED PRESSURE ",
#     # "60Hz CLOSED PRESSURE FLUCTUATED",

#     # "60Hz AMPERAGE",
#     # "60Hz AMPERAGE FLUCTUATED"
# ]
# compiledFrame = pd.DataFrame(columns=emptyColumn)

# # --- CLEANING before loop ---
# df = df[(~df["MODEL CODE"].isin(['120HP1000M']))]
# df = df[(~df["MODEL CODE"].isin(['60CAT0203M']))]
# df = df[(~df["TYPE"].isin(['T']))]
# df = df[(~df["TYPE"].isin(['D']))]
# df = df[(~df["TYPE"].isin(['A']))]
# df = df[(~df["PASS/NG"].isin([0]))]

# # Initialize variables to track previous values
# previous_wattage = None
# previous_air_volume = None

# # --- Custom loop FIRST (to populate compiledFrame) ---
# for a in range(len(df)):
#     print(f"ROW: {a}")
#     tempdf = df.iloc[[a]]
#     model_code = tempdf["MODEL CODE"].values[0]
#     current_wattage = tempdf["50Hz WATTAGE"].values[0]
#     current_air_volume = tempdf["50Hz AIR VOLUME"].values[0]
    
#     # Calculate wattage fluctuation
#     if current_wattage == 0:
#         wattage_fluctuation = 0
#     elif previous_wattage is None:
#         # First run - set default fluctuation
#         wattage_fluctuation = 5.00
#     else:
#         wattage_fluctuation = abs(previous_wattage - current_wattage)
    
#     # Calculate air volume fluctuation
#     if current_air_volume == 0:
#         air_volume_fluctuation = 0
#     elif previous_air_volume is None:
#         # First run - set default fluctuation
#         air_volume_fluctuation = 5.00
#     else:
#         air_volume_fluctuation = abs(previous_air_volume - current_air_volume)
    
#     dataFrame = {
#         "DATE": tempdf["DATE"].values[0],
#         "TIME": tempdf["TIME"].values[0],
#         "MODEL CODE": model_code,
#         "TYPE": tempdf["TYPE"].values[0],
#         "BARCODE": tempdf["BARCODE"].values[0],
#         "SERIAL No.": tempdf["SERIAL No."].values[0],
#         "PASS/NG": tempdf["PASS/NG"].values[0],
#         "50Hz WATTAGE": current_wattage,
#         "50Hz WATTAGE FLUCTUATED": wattage_fluctuation,
#         "50Hz AIR VOLUME": current_air_volume,
#         "50Hz AIR VOLUME FLUCTUATED": air_volume_fluctuation
#         # "50Hz CLOSED PRESSURE": tempdf["50Hz CLOSED PRESSURE"].values[0],
#         # "50Hz AMPERAGE": tempdf["50Hz AMPERAGE"].values[0],
#         # "60Hz WATTAGE": tempdf["60Hz WATTAGE"].values[0],
#         # "60Hz AIR VOLUME": tempdf["60Hz AIR VOLUME"].values[0],
#         # "60Hz CLOSED PRESSURE": tempdf["60Hz CLOSED PRESSURE"].values[0],
#         # "60Hz AMPERAGE": tempdf["60Hz AMPERAGE"].values[0]
#     }
    
#     # Update previous values for next iteration
#     previous_wattage = current_wattage
#     previous_air_volume = current_air_volume

#     dataList.append(dataFrame)

# dataFrame = pd.DataFrame(dataList)
# compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)

# # Export compiledFrame to CSV
# output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
# compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

# print(f"CSV file successfully saved to: {output_path}")












#%%
# import pandas as pd

# dataList = []

# pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_rows', None)

# # --- Load data ---
# file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# # LOAD CSV
# try:
#     df = pd.read_csv(file_path, encoding='latin1')
# except UnicodeDecodeError:
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# # Clean column names by stripping whitespace
# df.columns = df.columns.str.strip()

# # 1ST DATAFRAME (compiledFrame)
# emptyColumn = [
#     "DATE",
#     "TIME",
#     "MODEL CODE",
#     "TYPE",
#     "BARCODE",
#     "SERIAL No.",
#     "PASS/NG",

#     # 50Hz Measurements
#     "50Hz WATTAGE",
#     "50Hz WATTAGE FLUCTUATED",
#     "50Hz AIR VOLUME",
#     "50Hz AIR VOLUME FLUCTUATED",
#     "50Hz CLOSED PRESSURE",
#     "50Hz CLOSED PRESSURE FLUCTUATED",
#     "50Hz AMPERAGE",
#     "50Hz AMPERAGE FLUCTUATED",

#     # 60Hz Measurements
#     "60Hz WATTAGE",
#     "60Hz WATTAGE FLUCTUATED",
#     "60Hz AIR VOLUME",
#     "60Hz AIR VOLUME FLUCTUATED",
#     "60Hz CLOSED PRESSURE",
#     "60Hz CLOSED PRESSURE FLUCTUATED",
#     "60Hz AMPERAGE",
#     "60Hz AMPERAGE FLUCTUATED"
# ]
# compiledFrame = pd.DataFrame(columns=emptyColumn)

# # --- CLEANING before loop ---
# df = df[(~df["MODEL CODE"].isin(['120HP1000M']))]
# df = df[(~df["MODEL CODE"].isin(['60CAT0203M']))]
# df = df[(~df["TYPE"].isin(['T']))]
# df = df[(~df["TYPE"].isin(['D']))]
# df = df[(~df["TYPE"].isin(['A']))]
# df = df[(~df["PASS/NG"].isin([0]))]

# # Initialize variables to track previous values
# previous_values = {
#     '50Hz_WATTAGE': None,
#     '50Hz_AIR_VOLUME': None,
#     '50Hz_CLOSED_PRESSURE': None,
#     '50Hz_AMPERAGE': None,
#     '60Hz_WATTAGE': None,
#     '60Hz_AIR_VOLUME': None,
#     '60Hz_CLOSED_PRESSURE': None,
#     '60Hz_AMPERAGE': None
# }

# # --- Custom loop (to populate compiledFrame) ---
# for a in range(len(df)):
#     print(f"ROW: {a}")
#     tempdf = df.iloc[[a]]
#     model_code = tempdf["MODEL CODE"].values[0]
    
#     # Current values
#     current_values = {
#         '50Hz_WATTAGE': tempdf["50Hz WATTAGE"].values[0],
#         '50Hz_AIR_VOLUME': tempdf["50Hz AIR VOLUME"].values[0],
#         '50Hz_CLOSED_PRESSURE': tempdf["50Hz CLOSED PRESSURE"].values[0],
#         '50Hz_AMPERAGE': tempdf["50Hz AMPERAGE"].values[0],
#         '60Hz_WATTAGE': tempdf["60Hz WATTAGE"].values[0],
#         '60Hz_AIR_VOLUME': tempdf["60Hz AIR VOLUME"].values[0],
#         '60Hz_CLOSED_PRESSURE': tempdf["60Hz CLOSED PRESSURE"].values[0],
#         '60Hz_AMPERAGE': tempdf["60Hz AMPERAGE"].values[0]
#     }
    
#     # Calculate fluctuations
#     fluctuations = {}
#     for key in current_values:
#         if current_values[key] == 0:
#             fluctuations[key] = 0
#         elif previous_values[key] is None:
#             # First run - set default fluctuation
#             fluctuations[key] = 5.00
#         else:
#             fluctuations[key] = abs(previous_values[key] - current_values[key])
    
#     dataFrame = {
#         "DATE": tempdf["DATE"].values[0],
#         "TIME": tempdf["TIME"].values[0],
#         "MODEL CODE": model_code,
#         "TYPE": tempdf["TYPE"].values[0],
#         "BARCODE": tempdf["BARCODE"].values[0],
#         "SERIAL No.": tempdf["SERIAL No."].values[0],
#         "PASS/NG": tempdf["PASS/NG"].values[0],
        
#         # 50Hz Measurements
#         "50Hz WATTAGE": current_values['50Hz_WATTAGE'],
#         "50Hz WATTAGE FLUCTUATED": fluctuations['50Hz_WATTAGE'],
#         "50Hz AIR VOLUME": current_values['50Hz_AIR_VOLUME'],
#         "50Hz AIR VOLUME FLUCTUATED": fluctuations['50Hz_AIR_VOLUME'],
#         "50Hz CLOSED PRESSURE": current_values['50Hz_CLOSED_PRESSURE'],
#         "50Hz CLOSED PRESSURE FLUCTUATED": fluctuations['50Hz_CLOSED_PRESSURE'],
#         "50Hz AMPERAGE": current_values['50Hz_AMPERAGE'],
#         "50Hz AMPERAGE FLUCTUATED": fluctuations['50Hz_AMPERAGE'],
        
#         # 60Hz Measurements
#         "60Hz WATTAGE": current_values['60Hz_WATTAGE'],
#         "60Hz WATTAGE FLUCTUATED": fluctuations['60Hz_WATTAGE'],
#         "60Hz AIR VOLUME": current_values['60Hz_AIR_VOLUME'],
#         "60Hz AIR VOLUME FLUCTUATED": fluctuations['60Hz_AIR_VOLUME'],
#         "60Hz CLOSED PRESSURE": current_values['60Hz_CLOSED_PRESSURE'],
#         "60Hz CLOSED PRESSURE FLUCTUATED": fluctuations['60Hz_CLOSED_PRESSURE'],
#         "60Hz AMPERAGE": current_values['60Hz_AMPERAGE'],
#         "60Hz AMPERAGE FLUCTUATED": fluctuations['60Hz_AMPERAGE']
#     }
    
#     # Update previous values for next iteration
#     previous_values = current_values.copy()

#     dataList.append(dataFrame)

# dataFrame = pd.DataFrame(dataList)
# compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)

# # Export compiledFrame to CSV
# output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
# compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

# print(f"CSV file successfully saved to: {output_path}")












#%%import pandas as pd

# WORKING BUT NO TKINTER

# import pandas as pd

# dataList = []

# pd.set_option('display.max_columns', None)

# # --- Load data ---
# file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# # LOAD CSV
# try:
#     df = pd.read_csv(file_path, encoding='latin1')
# except UnicodeDecodeError:
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# # Clean column names by stripping whitespace
# df.columns = df.columns.str.strip()

# # Convert to datetime and sort chronologically
# df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])
# df = df.sort_values('DATETIME')

# # 1ST DATAFRAME (compiledFrame)
# emptyColumn = [
#     "DATE", "TIME", "MODEL CODE", "TYPE", "BARCODE", "SERIAL No.", "PASS/NG",
#     # 50Hz Measurements
#     "50Hz WATTAGE", "50Hz WATTAGE FLUCTUATED",
#     "50Hz AIR VOLUME", "50Hz AIR VOLUME FLUCTUATED",
#     "50Hz CLOSED PRESSURE", "50Hz CLOSED PRESSURE FLUCTUATED",
#     "50Hz AMPERAGE", "50Hz AMPERAGE FLUCTUATED",
#     # 60Hz Measurements
#     "60Hz WATTAGE", "60Hz WATTAGE FLUCTUATED",
#     "60Hz AIR VOLUME", "60Hz AIR VOLUME FLUCTUATED",
#     "60Hz CLOSED PRESSURE", "60Hz CLOSED PRESSURE FLUCTUATED",
#     "60Hz AMPERAGE", "60Hz AMPERAGE FLUCTUATED"
# ]
# compiledFrame = pd.DataFrame(columns=emptyColumn)

# # --- CLEANING before loop ---
# df = df[(~df["MODEL CODE"].isin(['120HP1000M', '60CAT0203M']))]
# df = df[(~df["TYPE"].isin(['T', 'D', 'A']))]
# df = df[(~df["PASS/NG"].isin([0]))]

# # Initialize variables to track previous values and date
# previous_values = {
#     '50Hz_WATTAGE': None,
#     '50Hz_AIR_VOLUME': None,
#     '50Hz_CLOSED_PRESSURE': None,
#     '50Hz_AMPERAGE': None,
#     '60Hz_WATTAGE': None,
#     '60Hz_AIR_VOLUME': None,
#     '60Hz_CLOSED_PRESSURE': None,
#     '60Hz_AMPERAGE': None
# }
# previous_date = None

# # --- Custom loop (to populate compiledFrame) ---
# for a in range(len(df)):
#     tempdf = df.iloc[[a]]
#     current_date = tempdf["DATE"].values[0]
#     model_code = tempdf["MODEL CODE"].values[0]
    
#     # Current values
#     current_values = {
#         '50Hz_WATTAGE': tempdf["50Hz WATTAGE"].values[0],
#         '50Hz_AIR_VOLUME': tempdf["50Hz AIR VOLUME"].values[0],
#         '50Hz_CLOSED_PRESSURE': tempdf["50Hz CLOSED PRESSURE"].values[0],
#         '50Hz_AMPERAGE': tempdf["50Hz AMPERAGE"].values[0],
#         '60Hz_WATTAGE': tempdf["60Hz WATTAGE"].values[0],
#         '60Hz_AIR_VOLUME': tempdf["60Hz AIR VOLUME"].values[0],
#         '60Hz_CLOSED_PRESSURE': tempdf["60Hz CLOSED PRESSURE"].values[0],
#         '60Hz_AMPERAGE': tempdf["60Hz AMPERAGE"].values[0]
#     }
    
#     # Check if this is a new date
#     is_new_date = (current_date != previous_date) if previous_date is not None else True
    
#     # Calculate fluctuations
#     fluctuations = {}
#     for key in current_values:
#         if current_values[key] == 0:
#             fluctuations[key] = 0
#         elif is_new_date:
#             # First record of new date - set default fluctuation
#             fluctuations[key] = 5.00
#         elif previous_values[key] is None:
#             # First record overall - set default fluctuation
#             fluctuations[key] = 5.00
#         else:
#             # Calculate normal fluctuation
#             fluctuations[key] = abs(previous_values[key] - current_values[key])
    
#     dataFrame = {
#         "DATE": current_date,
#         "TIME": tempdf["TIME"].values[0],
#         "MODEL CODE": model_code,
#         "TYPE": tempdf["TYPE"].values[0],
#         "BARCODE": tempdf["BARCODE"].values[0],
#         "SERIAL No.": tempdf["SERIAL No."].values[0],
#         "PASS/NG": tempdf["PASS/NG"].values[0],
        
#         # 50Hz Measurements
#         "50Hz WATTAGE": current_values['50Hz_WATTAGE'],
#         "50Hz WATTAGE FLUCTUATED": fluctuations['50Hz_WATTAGE'],
#         "50Hz AIR VOLUME": current_values['50Hz_AIR_VOLUME'],
#         "50Hz AIR VOLUME FLUCTUATED": fluctuations['50Hz_AIR_VOLUME'],
#         "50Hz CLOSED PRESSURE": current_values['50Hz_CLOSED_PRESSURE'],
#         "50Hz CLOSED PRESSURE FLUCTUATED": fluctuations['50Hz_CLOSED_PRESSURE'],
#         "50Hz AMPERAGE": current_values['50Hz_AMPERAGE'],
#         "50Hz AMPERAGE FLUCTUATED": fluctuations['50Hz_AMPERAGE'],
        
#         # 60Hz Measurements
#         "60Hz WATTAGE": current_values['60Hz_WATTAGE'],
#         "60Hz WATTAGE FLUCTUATED": fluctuations['60Hz_WATTAGE'],
#         "60Hz AIR VOLUME": current_values['60Hz_AIR_VOLUME'],
#         "60Hz AIR VOLUME FLUCTUATED": fluctuations['60Hz_AIR_VOLUME'],
#         "60Hz CLOSED PRESSURE": current_values['60Hz_CLOSED_PRESSURE'],
#         "60Hz CLOSED PRESSURE FLUCTUATED": fluctuations['60Hz_CLOSED_PRESSURE'],
#         "60Hz AMPERAGE": current_values['60Hz_AMPERAGE'],
#         "60Hz AMPERAGE FLUCTUATED": fluctuations['60Hz_AMPERAGE']
#     }
    
#     # Update previous values for next iteration
#     previous_values = current_values.copy()
#     previous_date = current_date
#     dataList.append(dataFrame)

# dataFrame = pd.DataFrame(dataList)
# compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)

# # Export compiledFrame to CSV
# output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
# compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

# print(f"CSV file successfully saved to: {output_path}")












#%%

# WORKING WITH TKINTER, PRESENTED TO MAM LENY
# import pandas as pd
# import tkinter as tk
# from tkinter import ttk

# dataList = []

# pd.set_option('display.max_columns', None)

# # --- Load data ---
# file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"

# # LOAD CSV
# try:
#     df = pd.read_csv(file_path, encoding='latin1')
# except UnicodeDecodeError:
#     df = pd.read_csv(file_path, encoding='ISO-8859-1', error='replace')

# # Clean column names by stripping whitespace
# df.columns = df.columns.str.strip()

# # Convert to datetime and sort chronologically
# df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])
# df = df.sort_values('DATETIME')

# # 1ST DATAFRAME (compiledFrame)
# emptyColumn = [
#     "DATE", "TIME", "MODEL CODE", "TYPE", "BARCODE", "SERIAL No.", "PASS/NG",
#     # 50Hz Measurements
#     "50Hz WATTAGE", "50Hz WATTAGE FLUCTUATED",
#     "50Hz AIR VOLUME", "50Hz AIR VOLUME FLUCTUATED",
#     "50Hz CLOSED PRESSURE", "50Hz CLOSED PRESSURE FLUCTUATED",
#     "50Hz AMPERAGE", "50Hz AMPERAGE FLUCTUATED",
#     # 60Hz Measurements
#     "60Hz WATTAGE", "60Hz WATTAGE FLUCTUATED",
#     "60Hz AIR VOLUME", "60Hz AIR VOLUME FLUCTUATED",
#     "60Hz CLOSED PRESSURE", "60Hz CLOSED PRESSURE FLUCTUATED",
#     "60Hz AMPERAGE", "60Hz AMPERAGE FLUCTUATED"
# ]
# compiledFrame = pd.DataFrame(columns=emptyColumn)

# # --- CLEANING before loop ---
# df = df[(~df["MODEL CODE"].isin(['120HP1000M', '60CAT0203M']))]
# df = df[(~df["TYPE"].isin(['T', 'D', 'A']))]
# df = df[(~df["PASS/NG"].isin([0]))]

# # Initialize variables to track previous values and date
# previous_values = {
#     '50Hz_WATTAGE': None,
#     '50Hz_AIR_VOLUME': None,
#     '50Hz_CLOSED_PRESSURE': None,
#     '50Hz_AMPERAGE': None,
#     '60Hz_WATTAGE': None,
#     '60Hz_AIR_VOLUME': None,
#     '60Hz_CLOSED_PRESSURE': None,
#     '60Hz_AMPERAGE': None
# }
# previous_date = None

# # --- Custom loop (to populate compiledFrame) ---
# for a in range(len(df)):
#     tempdf = df.iloc[[a]]
#     current_date = tempdf["DATE"].values[0]
#     model_code = tempdf["MODEL CODE"].values[0]
    
#     # Current values
#     current_values = {
#         '50Hz_WATTAGE': tempdf["50Hz WATTAGE"].values[0],
#         '50Hz_AIR_VOLUME': tempdf["50Hz AIR VOLUME"].values[0],
#         '50Hz_CLOSED_PRESSURE': tempdf["50Hz CLOSED PRESSURE"].values[0],
#         '50Hz_AMPERAGE': tempdf["50Hz AMPERAGE"].values[0],
#         '60Hz_WATTAGE': tempdf["60Hz WATTAGE"].values[0],
#         '60Hz_AIR_VOLUME': tempdf["60Hz AIR VOLUME"].values[0],
#         '60Hz_CLOSED_PRESSURE': tempdf["60Hz CLOSED PRESSURE"].values[0],
#         '60Hz_AMPERAGE': tempdf["60Hz AMPERAGE"].values[0]
#     }
    
#     # Check if this is a new date
#     is_new_date = (current_date != previous_date) if previous_date is not None else True
    
#     # Calculate fluctuations
#     fluctuations = {}
#     for key in current_values:
#         if current_values[key] == 0:
#             fluctuations[key] = 0
#         elif is_new_date:
#             # First record of new date - set default fluctuation
#             fluctuations[key] = 5.00
#         elif previous_values[key] is None:
#             # First record overall - set default fluctuation
#             fluctuations[key] = 5.00
#         else:
#             # Calculate normal fluctuation
#             fluctuations[key] = abs(previous_values[key] - current_values[key])
    
#     dataFrame = {
#         "DATE": current_date,
#         "TIME": tempdf["TIME"].values[0],
#         "MODEL CODE": model_code,
#         "TYPE": tempdf["TYPE"].values[0],
#         "BARCODE": tempdf["BARCODE"].values[0],
#         "SERIAL No.": tempdf["SERIAL No."].values[0],
#         "PASS/NG": tempdf["PASS/NG"].values[0],
        
#         # 50Hz Measurements
#         "50Hz WATTAGE": current_values['50Hz_WATTAGE'],
#         "50Hz WATTAGE FLUCTUATED": fluctuations['50Hz_WATTAGE'],
#         "50Hz AIR VOLUME": current_values['50Hz_AIR_VOLUME'],
#         "50Hz AIR VOLUME FLUCTUATED": fluctuations['50Hz_AIR_VOLUME'],
#         "50Hz CLOSED PRESSURE": current_values['50Hz_CLOSED_PRESSURE'],
#         "50Hz CLOSED PRESSURE FLUCTUATED": fluctuations['50Hz_CLOSED_PRESSURE'],
#         "50Hz AMPERAGE": current_values['50Hz_AMPERAGE'],
#         "50Hz AMPERAGE FLUCTUATED": fluctuations['50Hz_AMPERAGE'],
        
#         # 60Hz Measurements
#         "60Hz WATTAGE": current_values['60Hz_WATTAGE'],
#         "60Hz WATTAGE FLUCTUATED": fluctuations['60Hz_WATTAGE'],
#         "60Hz AIR VOLUME": current_values['60Hz_AIR_VOLUME'],
#         "60Hz AIR VOLUME FLUCTUATED": fluctuations['60Hz_AIR_VOLUME'],
#         "60Hz CLOSED PRESSURE": current_values['60Hz_CLOSED_PRESSURE'],
#         "60Hz CLOSED PRESSURE FLUCTUATED": fluctuations['60Hz_CLOSED_PRESSURE'],
#         "60Hz AMPERAGE": current_values['60Hz_AMPERAGE'],
#         "60Hz AMPERAGE FLUCTUATED": fluctuations['60Hz_AMPERAGE']
#     }
    
#     # Update previous values for next iteration
#     previous_values = current_values.copy()
#     previous_date = current_date
#     dataList.append(dataFrame)

# dataFrame = pd.DataFrame(dataList)
# compiledFrame = pd.concat([compiledFrame, dataFrame], ignore_index=True)

# # Export compiledFrame to CSV
# output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
# compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')

# print(f"CSV file successfully saved to: {output_path}")






# # --- Tkinter GUI ---
# class FluctuationMonitor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fluctuation Status Monitor")
#         self.root.geometry("500x500")
        
#         # Dictionary to hold our status variables and labels
#         self.status_vars = {}
#         self.status_labels = {}
        
#         # Create main frame
#         self.main_frame = ttk.Frame(root, padding="10")
#         self.main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Title label
#         ttk.Label(self.main_frame, text="Fluctuation Status Monitor", 
#                  font=('Arial', 14, 'bold')).pack(pady=10)
        
#         # Create display sections
#         self.create_section("50Hz Measurements", [
#             "50Hz WATTAGE FLUCTUATED",
#             "50Hz AIR VOLUME FLUCTUATED",
#             "50Hz CLOSED PRESSURE FLUCTUATED",
#             "50Hz AMPERAGE FLUCTUATED"
#         ])
        
#         # Separator
#         ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=10)
        
#         self.create_section("60Hz Measurements", [
#             "60Hz WATTAGE FLUCTUATED",
#             "60Hz AIR VOLUME FLUCTUATED",
#             "60Hz CLOSED PRESSURE FLUCTUATED",
#             "60Hz AMPERAGE FLUCTUATED"
#         ])
        
#         # Update button
#         ttk.Button(self.main_frame, text="Refresh Values", 
#                   command=self.update_values).pack(pady=10)
        
#         # Initialize with current values
#         self.update_values()
    
#     def create_section(self, title, columns):
#         """Create a section for a group of measurements"""
#         frame = ttk.Frame(self.main_frame)
#         frame.pack(fill=tk.X, pady=5)
        
#         # Section title
#         ttk.Label(frame, text=title, font=('Arial', 12, 'bold')).pack(anchor='w')
        
#         # Create rows for each measurement
#         for col in columns:
#             self.create_status_row(frame, col)
    
#     def create_status_row(self, parent, column_name):
#         """Create a row for a single measurement with status and reset button"""
#         row_frame = ttk.Frame(parent)
#         row_frame.pack(fill=tk.X, pady=2)
        
#         # Label for measurement name
#         label = ttk.Label(row_frame, text=f"{column_name.replace(' FLUCTUATED', '')}:", 
#                          width=25, anchor='w')
#         label.pack(side=tk.LEFT)
        
#         # Status variable and label
#         self.status_vars[column_name] = tk.StringVar()
#         self.status_labels[column_name] = ttk.Label(
#             row_frame, 
#             textvariable=self.status_vars[column_name],
#             font=('Arial', 10, 'bold'),
#             width=10
#         )
#         self.status_labels[column_name].pack(side=tk.LEFT)
        
#         # Reset button
#         reset_btn = ttk.Button(
#             row_frame, 
#             text="Reset", 
#             width=8,
#             command=lambda: self.reset_fluctuation(column_name)
#         )
#         reset_btn.pack(side=tk.RIGHT)
    
#     def update_values(self):
#         """Update all status values from the last row of data"""
#         last_row = compiledFrame.iloc[-1]
        
#         for column in self.status_vars:
#             value = last_row[column]
#             status = 1 if value > 5 else 0
#             self.status_vars[column].set(f"= {status}")
            
#             # Update color based on status
#             color = "red" if status == 1 else "green"
#             self.status_labels[column].configure(foreground=color)
    
#     def reset_fluctuation(self, column_name):
#         """Reset a specific fluctuation value to 0 in the DataFrame"""
#         compiledFrame.at[compiledFrame.index[-1], column_name] = 0
#         self.status_vars[column_name].set("= 0")
#         self.status_labels[column_name].configure(foreground="green")
        
#         # Update CSV file
#         compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
#         print(f"Reset {column_name} and updated CSV file")

# # Create and run the GUI
# root = tk.Tk()
# app = FluctuationMonitor(root)
# root.mainloop()



















# %%

# WORKING, WITH TKINTER AND REAL TIME MONITORING


# import pandas as pd
# import tkinter as tk
# from tkinter import ttk
# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# class FileChangeHandler(FileSystemEventHandler):
#     def __init__(self, callback):
#         self.callback = callback
    
#     def on_modified(self, event):
#         if event.src_path.endswith('.csv'):
#             self.callback()

# class FluctuationMonitor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fluctuation Status Monitor")
#         self.root.geometry("500x500")
        
#         self.status_vars = {}
#         self.status_labels = {}
        
#         self.main_frame = ttk.Frame(root, padding="10")
#         self.main_frame.pack(fill=tk.BOTH, expand=True)
        
#         ttk.Label(self.main_frame, text="Fluctuation Status Monitor", 
#                  font=('Arial', 14, 'bold')).pack(pady=10)
        
#         self.create_section("50Hz Measurements", [
#             "50Hz WATTAGE FLUCTUATED",
#             "50Hz AIR VOLUME FLUCTUATED",
#             "50Hz CLOSED PRESSURE FLUCTUATED",
#             "50Hz AMPERAGE FLUCTUATED"
#         ])
        
#         ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=10)
        
#         self.create_section("60Hz Measurements", [
#             "60Hz WATTAGE FLUCTUATED",
#             "60Hz AIR VOLUME FLUCTUATED",
#             "60Hz CLOSED PRESSURE FLUCTUATED",
#             "60Hz AMPERAGE FLUCTUATED"
#         ])
        
#         ttk.Button(self.main_frame, text="Refresh Values", 
#                   command=self.process_and_update).pack(pady=10)
        
#         # Initialize file monitoring
#         self.file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"
#         self.last_modified = os.path.getmtime(self.file_path)
        
#         event_handler = FileChangeHandler(self.check_file_update)
#         self.observer = Observer()
#         self.observer.schedule(event_handler, os.path.dirname(self.file_path))
#         self.observer.start()
        
#         # Initial processing
#         self.process_and_update()
        
#         # Schedule periodic checks (fallback)
#         self.root.after(1000, self.periodic_check)
    
#     def periodic_check(self):
#         self.check_file_update()
#         self.root.after(1000, self.periodic_check)
    
#     def check_file_update(self):
#         try:
#             current_modified = os.path.getmtime(self.file_path)
#             if current_modified > self.last_modified:
#                 self.last_modified = current_modified
#                 self.process_and_update()
#         except:
#             pass
    
#     def process_and_update(self):
#         global compiledFrame, output_path
        
#         try:
#             # Re-run the data processing
#             dataList = []
#             pd.set_option('display.max_columns', None)

#             try:
#                 df = pd.read_csv(self.file_path, encoding='latin1')
#             except UnicodeDecodeError:
#                 df = pd.read_csv(self.file_path, encoding='ISO-8859-1', error='replace')

#             df.columns = df.columns.str.strip()
#             df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])
#             df = df.sort_values('DATETIME')

#             emptyColumn = [
#                 "DATE", "TIME", "MODEL CODE", "TYPE", "BARCODE", "SERIAL No.", "PASS/NG",
#                 "50Hz WATTAGE", "50Hz WATTAGE FLUCTUATED",
#                 "50Hz AIR VOLUME", "50Hz AIR VOLUME FLUCTUATED",
#                 "50Hz CLOSED PRESSURE", "50Hz CLOSED PRESSURE FLUCTUATED",
#                 "50Hz AMPERAGE", "50Hz AMPERAGE FLUCTUATED",
#                 "60Hz WATTAGE", "60Hz WATTAGE FLUCTUATED",
#                 "60Hz AIR VOLUME", "60Hz AIR VOLUME FLUCTUATED",
#                 "60Hz CLOSED PRESSURE", "60Hz CLOSED PRESSURE FLUCTUATED",
#                 "60Hz AMPERAGE", "60Hz AMPERAGE FLUCTUATED"
#             ]
#             compiledFrame = pd.DataFrame(columns=emptyColumn)

#             df = df[(~df["MODEL CODE"].isin(['120HP1000M', '60CAT0203M']))]
#             df = df[(~df["TYPE"].isin(['T', 'D', 'A']))]
#             df = df[(~df["PASS/NG"].isin([0]))]

#             previous_values = {
#                 '50Hz_WATTAGE': None,
#                 '50Hz_AIR_VOLUME': None,
#                 '50Hz_CLOSED_PRESSURE': None,
#                 '50Hz_AMPERAGE': None,
#                 '60Hz_WATTAGE': None,
#                 '60Hz_AIR_VOLUME': None,
#                 '60Hz_CLOSED_PRESSURE': None,
#                 '60Hz_AMPERAGE': None
#             }
#             previous_date = None

#             for a in range(len(df)):
#                 tempdf = df.iloc[[a]]
#                 current_date = tempdf["DATE"].values[0]
#                 model_code = tempdf["MODEL CODE"].values[0]
                
#                 current_values = {
#                     '50Hz_WATTAGE': tempdf["50Hz WATTAGE"].values[0],
#                     '50Hz_AIR_VOLUME': tempdf["50Hz AIR VOLUME"].values[0],
#                     '50Hz_CLOSED_PRESSURE': tempdf["50Hz CLOSED PRESSURE"].values[0],
#                     '50Hz_AMPERAGE': tempdf["50Hz AMPERAGE"].values[0],
#                     '60Hz_WATTAGE': tempdf["60Hz WATTAGE"].values[0],
#                     '60Hz_AIR_VOLUME': tempdf["60Hz AIR VOLUME"].values[0],
#                     '60Hz_CLOSED_PRESSURE': tempdf["60Hz CLOSED PRESSURE"].values[0],
#                     '60Hz_AMPERAGE': tempdf["60Hz AMPERAGE"].values[0]
#                 }
                
#                 is_new_date = (current_date != previous_date) if previous_date is not None else True
                
#                 fluctuations = {}
#                 for key in current_values:
#                     if current_values[key] == 0:
#                         fluctuations[key] = 0
#                     elif is_new_date:
#                         fluctuations[key] = 5.00
#                     elif previous_values[key] is None:
#                         fluctuations[key] = 5.00
#                     else:
#                         fluctuations[key] = abs(previous_values[key] - current_values[key])
                
#                 dataFrame = {
#                     "DATE": current_date,
#                     "TIME": tempdf["TIME"].values[0],
#                     "MODEL CODE": model_code,
#                     "TYPE": tempdf["TYPE"].values[0],
#                     "BARCODE": tempdf["BARCODE"].values[0],
#                     "SERIAL No.": tempdf["SERIAL No."].values[0],
#                     "PASS/NG": tempdf["PASS/NG"].values[0],
#                     "50Hz WATTAGE": current_values['50Hz_WATTAGE'],
#                     "50Hz WATTAGE FLUCTUATED": fluctuations['50Hz_WATTAGE'],
#                     "50Hz AIR VOLUME": current_values['50Hz_AIR_VOLUME'],
#                     "50Hz AIR VOLUME FLUCTUATED": fluctuations['50Hz_AIR_VOLUME'],
#                     "50Hz CLOSED PRESSURE": current_values['50Hz_CLOSED_PRESSURE'],
#                     "50Hz CLOSED PRESSURE FLUCTUATED": fluctuations['50Hz_CLOSED_PRESSURE'],
#                     "50Hz AMPERAGE": current_values['50Hz_AMPERAGE'],
#                     "50Hz AMPERAGE FLUCTUATED": fluctuations['50Hz_AMPERAGE'],
#                     "60Hz WATTAGE": current_values['60Hz_WATTAGE'],
#                     "60Hz WATTAGE FLUCTUATED": fluctuations['60Hz_WATTAGE'],
#                     "60Hz AIR VOLUME": current_values['60Hz_AIR_VOLUME'],
#                     "60Hz AIR VOLUME FLUCTUATED": fluctuations['60Hz_AIR_VOLUME'],
#                     "60Hz CLOSED PRESSURE": current_values['60Hz_CLOSED_PRESSURE'],
#                     "60Hz CLOSED PRESSURE FLUCTUATED": fluctuations['60Hz_CLOSED_PRESSURE'],
#                     "60Hz AMPERAGE": current_values['60Hz_AMPERAGE'],
#                     "60Hz AMPERAGE FLUCTUATED": fluctuations['60Hz_AMPERAGE']
#                 }
                
#                 previous_values = current_values.copy()
#                 previous_date = current_date
#                 dataList.append(dataFrame)

#             compiledFrame = pd.concat([compiledFrame, pd.DataFrame(dataList)], ignore_index=True)
#             output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
#             compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
            
#             # Update the display
#             self.update_values()
            
#         except Exception as e:
#             print(f"Error processing file: {e}")
    
#     def create_section(self, title, columns):
#         frame = ttk.Frame(self.main_frame)
#         frame.pack(fill=tk.X, pady=5)
#         ttk.Label(frame, text=title, font=('Arial', 12, 'bold')).pack(anchor='w')
#         for col in columns:
#             self.create_status_row(frame, col)
    
#     def create_status_row(self, parent, column_name):
#         row_frame = ttk.Frame(parent)
#         row_frame.pack(fill=tk.X, pady=2)
        
#         ttk.Label(row_frame, text=f"{column_name.replace(' FLUCTUATED', '')}:", 
#                  width=25, anchor='w').pack(side=tk.LEFT)
        
#         self.status_vars[column_name] = tk.StringVar()
#         self.status_labels[column_name] = ttk.Label(
#             row_frame, 
#             textvariable=self.status_vars[column_name],
#             font=('Arial', 10, 'bold'),
#             width=10
#         )
#         self.status_labels[column_name].pack(side=tk.LEFT)
        
#         ttk.Button(
#             row_frame, 
#             text="Reset", 
#             width=8,
#             command=lambda: self.reset_fluctuation(column_name)
#         ).pack(side=tk.RIGHT)
    
#     def update_values(self):
#         try:
#             last_row = compiledFrame.iloc[-1]
#             for column in self.status_vars:
#                 value = last_row[column]
#                 status = 1 if value > 5 else 0
#                 self.status_vars[column].set(f"= {status}")
#                 color = "red" if status == 1 else "green"
#                 self.status_labels[column].configure(foreground=color)
#         except:
#             pass
    
#     def reset_fluctuation(self, column_name):
#         try:
#             compiledFrame.at[compiledFrame.index[-1], column_name] = 0
#             self.status_vars[column_name].set("= 0")
#             self.status_labels[column_name].configure(foreground="green")
#             compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
#         except:
#             pass
    
#     def on_closing(self):
#         self.observer.stop()
#         self.observer.join()
#         self.root.destroy()

# # Initialize global variables
# compiledFrame = pd.DataFrame()
# output_path = ""

# # Create and run the GUI
# root = tk.Tk()
# app = FluctuationMonitor(root)
# root.protocol("WM_DELETE_WINDOW", app.on_closing)
# root.mainloop()











# %%

# WORKING, WITH TKINTER, REAL TIME MONITORING, WITH  RED BOX FLUCTUATION DETECTED

import pandas as pd
import tkinter as tk
from tkinter import ttk
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
    
    def on_modified(self, event):
        if event.src_path.endswith('.csv'):
            self.callback()

class FluctuationMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluctuation Status Monitor")
        self.root.geometry("600x600")
        
        self.status_vars = {}
        self.status_labels = {}
        
        # Main container frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        ttk.Label(self.main_frame, text="Fluctuation Status Monitor", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Add the large status box
        self.status_box = tk.Canvas(self.main_frame, width=800, height=250, 
                                   bg="gray", highlightthickness=2, 
                                   highlightbackground="black")
        self.status_box.pack(pady=20)
        # THE VALUE OF 400 AND 125 HERE COMES FROM (self.status_box = tk.Canvas(self.main_frame, width=800, height=250,)  BEFORE 4 LINES ABOVE THIS LINES OF CODE
        # SO 800/2=400 AND 250/2=125
        self.status_text = self.status_box.create_text(400, 125, text="NO FLUCTUATION DETECTED", 
                                                     font=('Arial', 16, 'bold'), fill="white", anchor="center")
        
        # Detailed measurements frame
        self.details_frame = ttk.Frame(self.main_frame)
        self.details_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create display sections
        self.create_section("50Hz Measurements", [
            "50Hz WATTAGE FLUCTUATED",
            "50Hz AIR VOLUME FLUCTUATED",
            "50Hz CLOSED PRESSURE FLUCTUATED",
            "50Hz AMPERAGE FLUCTUATED"
        ])
        
        ttk.Separator(self.details_frame, orient='horizontal').pack(fill='x', pady=10)
        
        self.create_section("60Hz Measurements", [
            "60Hz WATTAGE FLUCTUATED",
            "60Hz AIR VOLUME FLUCTUATED",
            "60Hz CLOSED PRESSURE FLUCTUATED",
            "60Hz AMPERAGE FLUCTUATED"
        ])
        
        # Control buttons
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Refresh Values", 
                  command=self.process_and_update).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset All", 
                  command=self.reset_all_fluctuations).pack(side=tk.LEFT, padx=5)
        
        # Initialize file monitoring
        self.file_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\log507_ATU006_2507.csv"
        self.last_modified = os.path.getmtime(self.file_path)
        
        event_handler = FileChangeHandler(self.check_file_update)
        self.observer = Observer()
        self.observer.schedule(event_handler, os.path.dirname(self.file_path))
        self.observer.start()
        
        # Initial processing
        self.process_and_update()
        
        # Schedule periodic checks (fallback)
        self.root.after(1000, self.periodic_check)
    
    def update_status_box(self, has_fluctuation):
        """Update the large status box based on fluctuation presence"""
        if has_fluctuation:
            self.status_box.configure(bg="red")
            self.status_box.itemconfig(self.status_text, text="FLUCTUATION DETECTED!")
        else:
            self.status_box.configure(bg="gray")
            self.status_box.itemconfig(self.status_text, text="NO FLUCTUATION DETECTED")
    
    def periodic_check(self):
        self.check_file_update()
        self.root.after(1000, self.periodic_check)
    
    def check_file_update(self):
        try:
            current_modified = os.path.getmtime(self.file_path)
            if current_modified > self.last_modified:
                self.last_modified = current_modified
                self.process_and_update()
        except:
            pass
    
    def process_and_update(self):
        global compiledFrame, output_path
        
        try:
            # Re-run the data processing
            dataList = []
            pd.set_option('display.max_columns', None)

            try:
                df = pd.read_csv(self.file_path, encoding='latin1')
            except UnicodeDecodeError:
                df = pd.read_csv(self.file_path, encoding='ISO-8859-1', error='replace')

            df.columns = df.columns.str.strip()
            df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])
            df = df.sort_values('DATETIME')

            emptyColumn = [
                "DATE", "TIME", "MODEL CODE", "TYPE", "BARCODE", "SERIAL No.", "PASS/NG",
                "50Hz WATTAGE", "50Hz WATTAGE FLUCTUATED",
                "50Hz AIR VOLUME", "50Hz AIR VOLUME FLUCTUATED",
                "50Hz CLOSED PRESSURE", "50Hz CLOSED PRESSURE FLUCTUATED",
                "50Hz AMPERAGE", "50Hz AMPERAGE FLUCTUATED",
                "60Hz WATTAGE", "60Hz WATTAGE FLUCTUATED",
                "60Hz AIR VOLUME", "60Hz AIR VOLUME FLUCTUATED",
                "60Hz CLOSED PRESSURE", "60Hz CLOSED PRESSURE FLUCTUATED",
                "60Hz AMPERAGE", "60Hz AMPERAGE FLUCTUATED"
            ]
            compiledFrame = pd.DataFrame(columns=emptyColumn)

            df = df[(~df["MODEL CODE"].isin(['120HP1000M', '60CAT0203M']))]
            df = df[(~df["TYPE"].isin(['T', 'D', 'A']))]
            df = df[(~df["PASS/NG"].isin([0]))]

            previous_values = {
                '50Hz_WATTAGE': None,
                '50Hz_AIR_VOLUME': None,
                '50Hz_CLOSED_PRESSURE': None,
                '50Hz_AMPERAGE': None,
                '60Hz_WATTAGE': None,
                '60Hz_AIR_VOLUME': None,
                '60Hz_CLOSED_PRESSURE': None,
                '60Hz_AMPERAGE': None
            }
            previous_date = None

            for a in range(len(df)):
                tempdf = df.iloc[[a]]
                current_date = tempdf["DATE"].values[0]
                model_code = tempdf["MODEL CODE"].values[0]
                
                current_values = {
                    '50Hz_WATTAGE': tempdf["50Hz WATTAGE"].values[0],
                    '50Hz_AIR_VOLUME': tempdf["50Hz AIR VOLUME"].values[0],
                    '50Hz_CLOSED_PRESSURE': tempdf["50Hz CLOSED PRESSURE"].values[0],
                    '50Hz_AMPERAGE': tempdf["50Hz AMPERAGE"].values[0],
                    '60Hz_WATTAGE': tempdf["60Hz WATTAGE"].values[0],
                    '60Hz_AIR_VOLUME': tempdf["60Hz AIR VOLUME"].values[0],
                    '60Hz_CLOSED_PRESSURE': tempdf["60Hz CLOSED PRESSURE"].values[0],
                    '60Hz_AMPERAGE': tempdf["60Hz AMPERAGE"].values[0]
                }
                
                is_new_date = (current_date != previous_date) if previous_date is not None else True
                
                fluctuations = {}
                for key in current_values:
                    if current_values[key] == 0:
                        fluctuations[key] = 0
                    elif is_new_date:
                        fluctuations[key] = 5.00
                    elif previous_values[key] is None:
                        fluctuations[key] = 5.00
                    else:
                        fluctuations[key] = abs(previous_values[key] - current_values[key])
                
                dataFrame = {
                    "DATE": current_date,
                    "TIME": tempdf["TIME"].values[0],
                    "MODEL CODE": model_code,
                    "TYPE": tempdf["TYPE"].values[0],
                    "BARCODE": tempdf["BARCODE"].values[0],
                    "SERIAL No.": tempdf["SERIAL No."].values[0],
                    "PASS/NG": tempdf["PASS/NG"].values[0],
                    "50Hz WATTAGE": current_values['50Hz_WATTAGE'],
                    "50Hz WATTAGE FLUCTUATED": fluctuations['50Hz_WATTAGE'],
                    "50Hz AIR VOLUME": current_values['50Hz_AIR_VOLUME'],
                    "50Hz AIR VOLUME FLUCTUATED": fluctuations['50Hz_AIR_VOLUME'],
                    "50Hz CLOSED PRESSURE": current_values['50Hz_CLOSED_PRESSURE'],
                    "50Hz CLOSED PRESSURE FLUCTUATED": fluctuations['50Hz_CLOSED_PRESSURE'],
                    "50Hz AMPERAGE": current_values['50Hz_AMPERAGE'],
                    "50Hz AMPERAGE FLUCTUATED": fluctuations['50Hz_AMPERAGE'],
                    "60Hz WATTAGE": current_values['60Hz_WATTAGE'],
                    "60Hz WATTAGE FLUCTUATED": fluctuations['60Hz_WATTAGE'],
                    "60Hz AIR VOLUME": current_values['60Hz_AIR_VOLUME'],
                    "60Hz AIR VOLUME FLUCTUATED": fluctuations['60Hz_AIR_VOLUME'],
                    "60Hz CLOSED PRESSURE": current_values['60Hz_CLOSED_PRESSURE'],
                    "60Hz CLOSED PRESSURE FLUCTUATED": fluctuations['60Hz_CLOSED_PRESSURE'],
                    "60Hz AMPERAGE": current_values['60Hz_AMPERAGE'],
                    "60Hz AMPERAGE FLUCTUATED": fluctuations['60Hz_AMPERAGE']
                }
                
                previous_values = current_values.copy()
                previous_date = current_date
                dataList.append(dataFrame)

            compiledFrame = pd.concat([compiledFrame, pd.DataFrame(dataList)], ignore_index=True)
            output_path = r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\OTHER PROJECT\fluctuatedQC_CSV.csv"
            compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
            
            # Update the display
            self.update_display()
            
        except Exception as e:
            print(f"Error processing file: {e}")
    
    def update_display(self):
        """Update both the status box and detailed measurements"""
        try:
            last_row = compiledFrame.iloc[-1]
            has_fluctuation = False
            
            # Check all fluctuation columns
            for column in self.status_vars:
                value = last_row[column]
                status = 1 if value > 5 else 0
                self.status_vars[column].set(f"= {status}")
                color = "red" if status == 1 else "green"
                self.status_labels[column].configure(foreground=color)
                
                if status == 1:
                    has_fluctuation = True
            
            # Update the large status box
            self.update_status_box(has_fluctuation)
            
        except Exception as e:
            print(f"Error updating display: {e}")
    
    def create_section(self, title, columns):
        frame = ttk.Frame(self.details_frame)
        frame.pack(fill=tk.X, pady=5)
        ttk.Label(frame, text=title, font=('Arial', 12, 'bold')).pack(anchor='w')
        for col in columns:
            self.create_status_row(frame, col)
    
    def create_status_row(self, parent, column_name):
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=2)
        
        ttk.Label(row_frame, text=f"{column_name.replace(' FLUCTUATED', '')}:", 
                 width=25, anchor='w').pack(side=tk.LEFT)
        
        self.status_vars[column_name] = tk.StringVar()
        self.status_labels[column_name] = ttk.Label(
            row_frame, 
            textvariable=self.status_vars[column_name],
            font=('Arial', 10, 'bold'),
            width=10
        )
        self.status_labels[column_name].pack(side=tk.LEFT)
        
        ttk.Button(
            row_frame, 
            text="Reset", 
            width=8,
            command=lambda: self.reset_fluctuation(column_name)
        ).pack(side=tk.RIGHT)
    
    def reset_fluctuation(self, column_name):
        try:
            compiledFrame.at[compiledFrame.index[-1], column_name] = 0
            self.status_vars[column_name].set("= 0")
            self.status_labels[column_name].configure(foreground="green")
            compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
            
            # Check if we need to update the status box after reset
            self.update_display()
        except:
            pass
    
    def reset_all_fluctuations(self):
        """Reset all fluctuation values to 0"""
        try:
            for column in self.status_vars:
                compiledFrame.at[compiledFrame.index[-1], column] = 0
                self.status_vars[column].set("= 0")
                self.status_labels[column].configure(foreground="green")
            
            compiledFrame.to_csv(output_path, index=False, encoding='utf-8-sig')
            self.update_status_box(False)  # Set status box to gray
        except:
            pass
    
    def on_closing(self):
        self.observer.stop()
        self.observer.join()
        self.root.destroy()

# Initialize global variables
compiledFrame = pd.DataFrame()
output_path = ""

# Create and run the GUI
root = tk.Tk()
app = FluctuationMonitor(root)
root.protocol("WM_DELETE_WINDOW", app.on_closing)
root.mainloop()

#%%