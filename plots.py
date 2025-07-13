import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import glob
import os
import json

# --- Configuration ---
# Set the path to your project folder.
# NOTE: The path from your MATLAB script has been used. Update if needed.
FOLDER_PATH = r'E:\Eshwar\Projects\Realestate\swindon'
FILE_PATTERN = os.path.join(FOLDER_PATH, '*buy.csv')
POSTCODE_JSON_PATH = os.path.join(FOLDER_PATH, 'outcode mappings.json')

# --- Load Postcode Lookup Data ---
# This corresponds to 'load PClookup.mat'. 
# Note: This data is loaded but not used in the active part of the script,
# matching the commented-out code in your original MATLAB file.
try:
    with open(POSTCODE_JSON_PATH, 'r') as f:
        pc_lookup_data = json.load(f)
    pc_lookup_df = pd.DataFrame(pc_lookup_data)
    # print("Postcode lookup table loaded successfully.")
    # print(pc_lookup_df.head())
except FileNotFoundError:
    print(f"Warning: Postcode JSON file not found at {POSTCODE_JSON_PATH}")
    pc_lookup_df = None


# --- Process Each CSV File ---
csv_files = glob.glob(FILE_PATTERN)
print(f"Found {len(csv_files)} CSV files to process.")

# Variable to hold the last dataframe for the final plot
sn_home = None 

for i, file_path in enumerate(csv_files):
    file_name = os.path.basename(file_path)
    print(f"Processing file ({i+1}/{len(csv_files)}): {file_name}")

    # Read the CSV file into a pandas DataFrame
    sn_home = pd.read_csv(file_path)

    # --- Data Cleaning and Preparation ---
    
    # Calculate price in thousands of GBP
    sn_home['kGBP'] = sn_home['price'] / 1000
    
    # Clean up the 'type' column
    replacements = {'for sale': '', 'bedroom': '', 'house': ''}
    sn_home['type_cleaned'] = sn_home['type'].replace(replacements, regex=True).str.strip()

    # --- Create and Save Histogram for 4-Bedroom Properties ---
    
    # Filter for 4-bedroom properties
    df_4br = sn_home[sn_home['number_bedrooms'] == 4].copy()

    if not df_4br.empty:
        # Create the histogram
        fig_hist = px.histogram(
            df_4br,
            x='kGBP',
            title=f"Price Distribution for 4-Bedroom Homes ({file_name[:10]})",
            labels={'kGBP': 'Price (£k)'},
            text_auto=True # Automatically add counts on top of bars
        )

        # Update layout to match MATLAB script
        total_count = len(df_4br)
        fig_hist.update_layout(
            xaxis_range=[200, 500],
            yaxis_range=[0, 60],
            title_text=f"Price Distribution for 4-BR Homes (Total: {total_count}) - {file_name[:10]}",
            bargap=0.1
        )
        fig_hist.update_traces(textposition='outside')

        # Define and save the output file
        output_filename = f"1-{file_name[:10]}.png"
        output_filepath = os.path.join(FOLDER_PATH, output_filename)
        
        print(f"  -> Saving histogram to {output_filepath}")
        fig_hist.write_image(output_filepath)
    else:
        print("  -> No 4-bedroom properties found in this file. Skipping histogram.")


    # --- Commented-out Plot (Translated from MATLAB) ---
    # This section corresponds to the commented-out box plot in your .m file.
    # It shows price variation by postcode.
    #
    # fig_box_pc = px.box(
    #     sn_home, 
    #     x='PostCode', 
    #     y='kGBP', 
    #     points='all',  # Equivalent to scatter overlay
    #     color='number_bedrooms', # Color points by number of bedrooms
    #     title="Post Code Variation",
    #     labels={'kGBP': 'Price (£k)', 'PostCode': 'Postcode'}
    # )
    # fig_box_pc.update_layout(yaxis_range=[0, 500])
    # # output_filepath_pc = os.path.join(FOLDER_PATH, f"2-{file_name[:10]}.png")
    # # fig_box_pc.write_image(output_filepath_pc)
    # fig_box_pc.show()


print("\nLoop finished. Generating final plot from the last processed file.")

# --- Final Plot (after loop) ---
# This plot is generated using the data from the LAST csv file in the folder,
# matching the logic of the original script.
if sn_home is not None:
    fig_final_box = px.box(
        sn_home.sort_values('type_cleaned'), 
        x='type_cleaned', 
        y='kGBP', 
        points="all", # 'all' adds a scatter plot overlay (stripplot)
        title='Price Variation by Property Type',
        labels={'kGBP': 'Price (£k)', 'type_cleaned': 'Property Type'}
    )
    
    fig_final_box.show()
else:
    print("No data was loaded, cannot generate final plot.")