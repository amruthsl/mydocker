import platform
import sys
import numpy as np
import pandas as pd

print("=" * 50)
print("DOCKER LEARNING PROJECT")
print("=" * 50)

print(f"Python Version : {platform.python_version()}")
print(f"Python Executable : {sys.executable}")
print(f"NumPy Version : {np.__version__}")
print(f"Pandas Version : {pd.__version__}")

temperatures = np.array([30, 32, 28, 35, 31])

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temperature": temperatures
})

print("\nTemperature Data")
print(df)

print("\nAverage Temperature:", df["Temperature"].mean())

print("=" * 50)