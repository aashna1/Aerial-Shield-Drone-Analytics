"""
export.py

Exports the generated dataset.
"""

import pandas as pd
import os


def export_dataset(data):

    df = pd.DataFrame(data)

    os.makedirs("output", exist_ok=True)

    csv_path = os.path.join("output", "Aerial_Shield_Drone_Data.csv")

    excel_path = os.path.join("output", "Aerial_Shield_Drone_Data.xlsx")

    df.to_csv(csv_path, index=False)

    df.to_excel(excel_path, index=False)

    print(f"\nDataset exported successfully!")
    print(f"CSV   : {csv_path}")
    print(f"Excel : {excel_path}")

    return df