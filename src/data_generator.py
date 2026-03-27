import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start='2022-01-01', periods=500)

df = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 500, size=len(dates)),
    'Price': np.random.randint(10, 50, size=len(dates)),
    'Promotion': np.random.choice([0, 1], size=len(dates)),
    'Store': np.random.choice(['Store_A', 'Store_B'], size=len(dates)),
    'Product': np.random.choice(['Coffee', 'Maggi', 'KitKat'], size=len(dates))
})

df.to_csv('../data/sales_data.csv', index=False)
print("✅ Data generated successfully!")