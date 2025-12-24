#!/usr/bin/env python3
"""
TEKNOFEST Elite Engineering Core
PID Controller Implementation
"""

import time

class PIDController:
    """
    Standard PID Controller (Proportional, Integral, Derivative)
    Used for UAV stabilization, autonomous driving, and industrial control.
    """
    
    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, setpoint=0.0, output_limits=(None, None)):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.output_limits = output_limits
        
        self._prev_error = 0.0
        self._integral = 0.0
        self._last_time = time.time()
        
    def compute(self, measurement):
        """Calculates the control output based on the current measurement."""
        now = time.time()
        dt = now - self._last_time
        if dt <= 0.0:
            dt = 1e-6 # Avoid division by zero
            
        error = self.setpoint - measurement
        
        # Proportional term
        p_term = self.Kp * error
        
        # Integral term
        self._integral += error * dt
        i_term = self.Ki * self._integral
        
        # Derivative term
        derivative = (error - self._prev_error) / dt
        d_term = self.Kd * derivative
        
        output = p_term + i_term + d_term
        
        # Apply output limits
        lower, upper = self.output_limits
        if lower is not None:
            output = max(lower, output)
        if upper is not None:
            output = min(upper, output)
            
        # Update states
        self._prev_error = error
        self._last_time = now
        
        return output

# --- Example Usage ---
if __name__ == "__main__":
    # Simulating a drone trying to reach altitude 100m
    drone_pid = PIDController(Kp=0.8, Ki=0.2, Kd=0.1, setpoint=100.0, output_limits=(0, 100))
    
    current_altitude = 10.0
    print(f"🚀 Launching! Target: {drone_pid.setpoint}m")
    
    for i in range(20):
        thrust = drone_pid.compute(current_altitude)
        # Simplified physics: thrust increases altitude
        current_altitude += (thrust * 0.1) 
        print(f"Time Step {i}: Altitude={current_altitude:.2f}m, Thrust={thrust:.2f}%")
        time.sleep(0.1)
