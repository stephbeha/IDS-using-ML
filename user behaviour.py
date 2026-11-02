import statistics

def detect_anomaly(user_data):
    """
    Detect anomalies in user behavior based on download size deviations.
    
    Args:
        user_data (dict): A dictionary containing user behavior data, including "login_times" and "download_sizes".
    """
    
    # Assume we have a "baseline" dictionary that contains historical user behavior data
    baseline = {
        "login_times": [10, 15, 20, 25, 30],  # Ensure there are at least two data points
        "download_sizes": [100, 200, 150, 180, 220]
    }
    
    # Calculate the mean and standard deviation of the baseline download sizes
    baseline_mean = mean(baseline["download_sizes"])
    baseline_std_dev = stdev(baseline["download_sizes"])
    
    # Calculate the deviation of the current download size from the baseline
    download_size = user_data["download_size"]
    download_deviation = abs(download_size - baseline_mean)
    
    # Set a threshold for the maximum allowed deviation
    max_download_size_deviation = 2  # Adjust this value as needed
    
    # Use the standard deviation as the dynamic threshold, if possible
    try:
        if download_deviation > max_download_size_deviation * stdev(baseline["login_times"]):
            # Detect anomaly
            print(f"Potential anomaly detected. Download size deviation: {download_deviation}")
    except statistics.StatisticsError:
        # If there are not enough data points to calculate the standard deviation,
        # use the mean instead
        if download_deviation > max_download_size_deviation * mean(baseline["login_times"]):
            # Detect anomaly
            print(f"Potential anomaly detected. Download size deviation: {download_deviation}")

def mean(data):
    """
    Calculate the mean of a list of numbers.
    
    Args:
        data (list): A list of numbers.
    
    Returns:
        float: The mean of the data.
    """
    return sum(data) / len(data)

def stdev(data):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        data (list): A list of numbers.
    
    Returns:
        float: The standard deviation of the data.
    """
    if len(data) < 2:
        raise statistics.StatisticsError('stdev requires at least two data points')
    
    mean_value = mean(data)
    variances = [(x - mean_value) ** 2 for x in data]
    variance = sum(variances) / (len(data) - 1)
    return variance ** 0.5

# Example usage
user_data = {
    "download_size": 250,
    # Other user behavior data can be added here
}
detect_anomaly(user_data)