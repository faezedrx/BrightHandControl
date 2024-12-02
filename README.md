# Hand Gesture-Based Screen Brightness Control

This project demonstrates how to control screen brightness based on hand gestures using Python. It utilizes OpenCV for image processing, Mediapipe for hand detection, and a PowerShell script to adjust screen brightness on Windows.

## Features

- Detects hand gestures using the webcam.
- Adjusts screen brightness based on the openness of the hand.
- Reduces brightness when the hand is closed and increases it when the hand is open.

## Prerequisites

- **Python**: Ensure Python is installed on your system.
- **PowerShell**: For running the PowerShell script that adjusts screen brightness.

## Installation

### 1. Install Python Libraries

You need to install the following Python libraries:

```bash
pip install opencv-python mediapipe
```

### 2. Create and Configure PowerShell Script
You need to create a PowerShell script to control the screen brightness. Follow these steps:

  1. **Open a Text Editor**: Use any text editor like Notepad or Visual Studio Code.

  2. **Create a New File**: Name it `set_brightness.ps1`.

  3. **Add the PowerShell Script Code**: Copy and paste the following code into the file:

```powershell 
  param (
    [int]$brightness
)

  # Ensure brightness is between 0 and 100
  $brightness = [math]::Max(0, [math]::Min(100, $brightness))
  
  # Adjust the screen brightness
  (Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, $brightness)
```
4. **Save the File**: Save this file in the same directory as your Python script.
### 3. Adjust PowerShell Execution Policy
If you encounter issues running the PowerShell script, you might need to adjust the execution policy:

1. Open PowerShell as Administrator: Right-click the PowerShell icon and select "Run as Administrator".

2. Set Execution Policy: Run the following command:
   
  ```powershell 
  Set-ExecutionPolicy RemoteSigned
  ```
  Confirm the change by typing Y and pressing Enter.

### 4. Verify Webcam Access
Ensure that your webcam is properly connected and accessible. The script requires webcam access to detect hand gestures.

## Running the Script

1. Navigate to the directory containing your Python script and the `set_brightness.ps1` file.
   
2. Run the Python script using:
   
   ```bash
   python BrightHandControl.py
   ```
   
3. Control Brightness with Hand Gestures:
   - **Closed Hand**: Screen brightness will decrease.
   - **Open Hand**: Screen brightness will increase.

4. Exit: Press the 'q' key while the script window is active to stop the program.

## Code Explanation

- **Hand Detection**: Uses Mediapipe to detect hand landmarks and gestures.
- **Brightness Adjustment**: Calls a PowerShell script to adjust the brightness based on the detected hand gesture.


## Contact 📬

If you have any questions or need further assistance, feel free to contact us at [my email : faezeh.darbeheshti@gmail.com ](mailto:faezeh.darbeheshti@gmail.com).

    
