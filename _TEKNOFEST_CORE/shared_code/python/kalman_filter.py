#!/usr/bin/env python3
"""
TEKNOFEST Elite Engineering Core
Basic Kalman Filter Implementation
"""

class KalmanFilter:
    """
    1D Kalman Filter for sensor noise reduction.
    Ideal for filtering GPS data, altitude sensors, or battery voltage.
    """
    
    def __init__(self, initial_state=0.0, initial_estimate_error=1.0, process_noise=0.01, measurement_noise=0.1):
        self.state = initial_state           # x
        self.estimate_error = initial_estimate_error # P
        self.process_noise = process_noise   # Q
        self.measurement_noise = measurement_noise # R
        
    def update(self, measurement):
        """
        Predict and Update cycle of Kalman Filter.
        """
        # --- Predict Step ---
        # x_pred = x
        # P_pred = P + Q
        self.estimate_error += self.process_noise
        
        # --- Update Step ---
        # Kalman Gain (K) = P_pred / (P_pred + R)
        kalman_gain = self.estimate_error / (self.estimate_error + self.measurement_noise)
        
        # Update State (x) = x_pred + K * (measurement - x_pred)
        self.state = self.state + kalman_gain * (measurement - self.state)
        
        # Update Estimate Error (P) = (1 - K) * P_pred
        self.estimate_error = (1 - kalman_gain) * self.estimate_error
        
        return self.state

# --- Example Usage ---
if __name__ == "__main__":
    import random
    
    kf = KalmanFilter(initial_state=25.0, measurement_noise=2.0)
    
    true_value = 25.0 # Constant temperature but noisy sensor
    print(f"🌡️ Filtering Temperature: Target {true_value}°C")
    
    for i in range(10):
        noisy_measurement = true_value + random.uniform(-2, 2)
        filtered_value = kf.update(noisy_measurement)
        print(f"Step {i}: Raw={noisy_measurement:.2f}, Filtered={filtered_value:.4f}")
