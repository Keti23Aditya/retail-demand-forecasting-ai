import matplotlib.pyplot as plt

def plot_result(actual, forecast):
    plt.figure(figsize=(10,5))
    plt.plot(actual, label="Actual")
    plt.plot(forecast, label="Forecast")
    plt.legend()
    plt.title("Sales Forecast")
    plt.savefig("../outputs/forecast.png")
    plt.show()