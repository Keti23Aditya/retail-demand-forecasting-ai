from statsmodels.tsa.arima.model import ARIMA

def train_model(data):
    model = ARIMA(data, order=(5,1,0))
    model_fit = model.fit()
    return model_fit

def make_forecast(model, steps=30):
    return model.forecast(steps=steps)