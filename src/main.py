from preprocessing import load_data, preprocess
from model import train_model, make_forecast
from utils import plot_result

# Load data
df = load_data('../data/sales_data.csv')

# Preprocess
df = preprocess(df)

# Select sales
sales = df['Sales']

# Train model
model = train_model(sales)

# Forecast
forecast = make_forecast(model)

# Plot
plot_result(sales, forecast)

print("✅ Project executed successfully!")