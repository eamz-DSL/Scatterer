To use the "scatter_images" Python script in VSCode, follow these steps:

-Install Python: Ensure Python is installed on your system. You can download and install Python 
from the official Python website. Make sure to add Python to your system's PATH during installation.

-Install Pillow Library: Open a terminal in VSCode and install the Pillow library using pip. 
Pillow is required for image processing in the script.

        
          pip install Pillow


-Prepare Input Images: Place the images you want to scatter in a folder on your system. 
Supported image formats include JPG, JPEG, PNG, and GIF. (while it DOES support GIFs, it will not scatter multiple moving images while keeping them animated)

-Open VSCode: Launch VSCode on your system.

-Open the Script: Open the "scatter_images.py" script in VSCode. You can do this by navigating to the 
script file using the file explorer or by using the "File" > "Open File" option in VSCode.

-Configure Script Parameters: Edit the script file if necessary. The script expects input for the path 
to the input folder containing the images and the number of scattered images to generate. 
Ensure these parameters are correctly set based on your requirements.

-Run the Script: To run the script, ensure the cursor is within the script file, then press Ctrl + F5 or 
navigate to the "Run" menu and select "Run Without Debugging". Follow the prompts in the VSCode terminal 
to provide the input folder path and the number of scattered images to generate.

View Output: Once the script finishes execution, the scattered images will be saved in a folder named "scattered_images" 
within the input folder specified. You can locate this folder in the file explorer within VSCode or using your system's file explorer.

Adjust Parameters: You can adjust parameters within the script file, such as the density of the scatter 
and the range of image adjustments, to customize the output according to your preferences.



Feedback or Issues: For any feedback or issues with the script, you can reach out to the script author or seek assistance in relevant forums or communities.


This readme provides a basic guide on how to use the script within the VSCode environment. Adjustments may be necessary based on your specific setup or requirements.

EAMZ Darkstonelabs
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░▒░░░░▒░░░▒░░▒░░░░▒░░░▒▒░░█▓░░▓▒▒▒▓▓▒░▒█▒░░▒░░░▒░░░░░░░▒░░░▒░░░░░▒░░▒░░░░░░░░░░░░
░░░░░░▒░░░▒▒░░▒▒░░░░░░░▒░░░░▒░░▒▒░░░▓▓░░▒▒░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░▒░░░░░░░░░░
░░░░▒▒░░░░░░▒░░░░░░░▒▒░░░░░░▒▓░░▒░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▒░░░▒░░░░▒░░░▒░░░░▒░░░▓▓▓████████░░░░░░░░▒▒██████░░░░░░░░░░░░░░░░░░░░░░░░░
░░▒░░▒░░░▒░░░░░░░░░░░░░░░░░█████▓░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░▓████░░░░░░▒░░░░░░░░░░░░░
░░░░░░░░░░▒░░░░░▓▓▒░░░░░▒██▓▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓██▒░░░░░░░░░░░▒░░░░░
░░▒░░░▒░░░░▒░░██▒░▒░░░░██▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒█▓░░░░░▒░░░░░░░░░░
░░░░▒░░░▒▒░░▒█░░█▒░░░░██▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░████░░░░▒░░▒█▒░░░
░░▒░░░▒░░░░░░░██░░▒██▒░░░░░░░░░░░░░░░░░░░░░░░▒░▒░░░▒░▒░░░░▒▒░░░░░░░░░░▓░░▒░░░░██░░▒░
░░░░▒▒░░▒▒░░▓█▒░▒██▒▒▓▒▓██▒▓▒░▒▓▒▓▓▒█░░░▒░▒░░░░░░░░▒░░░▒▒▒░▒░░▒░░░░░▒▒██░░░░░░░█░░░░
░░░░░░░░░░░░▒░░██▒▓█▓▒██▓▓▓▓▓▓█░▒▓░▓▒▓██▒▓██▓████▓▓█▒█▓█▒█▓▓▓▒███████▓█░░░░░░░█▓░░░░
░░▒░░░░░░░░░▒███░░░░░░█▒░░▓█▒██▓█░▓██▓█▒▓██▒▓▓▒█▓▓▓█▓██▓▒▒▒▒▓▓▓▒▓▓▓██░██▓▒▓░▒█▒▓▓▒░░
░▓▒█▓▓▓▒▒█▓░▒█░░░░▒▒▒░░░░░░░░░░░▒░░░░▒░░░▒░░░▒░▒░░░░░░░░░░░▒▓▒░░▓▒▒░░░███████▒▒▓▒██░
░░▓░░█▒▓▒░░▓██░░▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▒░░░▒▒░░▒░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░█░░░░░█▓░▓▓░▓░
▒▓░█▓░░▒▓█▓▓█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒███▓▒░░▒▒░░░░░░░▒█▓░░░░
░▒█▓▒█▓▓▓▓▒██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████████░░█▒░░█▓▓▓░░░
░▒░▒▓▒▓▒▓█░▒█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓██▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒░░░░▒░░▒░░▒█░░█▒░░░░
░▒▓▒░░▒▒▒▒░█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██████▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒█▓░░░░░▓█░░▒▓░░░▓▓▒░▒▓░
░▒▒▒▒▓▓░▒▒░█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░████░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█░░█▓▒█░░███▓▓▒▓▓█▓░▒▒░░
░█▒▒█░▓▓▒░▓█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░███▓░░▓████░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓███▒█░█▓░▓█▓█▓▓█░▓█░░▓▓░
░▒▓▒▒▒▓░█▒██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░░░█▒░░░▒░░░░░▒▒▒▒▒▒▒▒▒▒▒░░█▒▓▒▓▒▓█▓░░█░░▓░▒▒█▒▒▒▒▒░
░▒░▒▓░▓▓░▓█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒░░░░█░██░█▒▒██▒░▒▒▒▒▒▒▒▒▒▒▒░░█░█░██░█▒░░▒█▓▓▒▓▒█▒▒▒█▓░
░▒█▓▒▓▒▒██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░█▓░█░█░█▒░█░░▒▒▒▒▒▒▒▒▒▒▒░██▒███░█▒░░▒█▒█▒▒▒█▓▒▒▒▓░
░▓░▒▓▒▒██░░▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█░▒█▒█▓█░█▒░▒▒░▒▒▒▒▒▒▒▒░░▓█▒░░██░░░▒█▓▒▓█▓▓▓▒█▓▒░
░▓██░███▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓█░▒█░░█░█▒░▒▒▒▒▒▒░▒▒▒▒▒░░░▒██░░░░░▒▓▓██▒██▓░▓█▓░
▒█▒▓█░░█░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░██░███▒█▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒░░▒██▒░█▓█▒░▒█▓▒░
░██░░▒▒██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░██▓▒██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░▒▒░██▓▒█▓▓▓▒▓▒░▒██░
░▓█▒░▒░░████░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▒░░░█▓█▓█▓▒▓▓▓▓▓▓▓░
░█▓▒▒░░░█▓▓▓███░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒█▓░▓█▒▓██▒█▓░▓▓░
░▓█▒░▒▓▓▒▓▓▒▓░▓█████░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒░▒██▒▒▓░░█▒░▒▓▒█░░█░
░▒▓██░▒░▒▓█░███▒██▒████████░░░▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒█▓▓█▓██▒░█▒▓░▓█▓▒░
░███▓▒░▒▒░███░▓█▒▒▓▒░▓▓██████░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒██▒▒▒▒░░░░██▒▒░█▓░░█▓▓████▒██░
▒▓▓▓▒░░░░▒█▒███▓██▓██▓█▒░▒░░░███▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░███▒▓█▓▒▒█▓░▒▒░▒░▓█▓▒░
░▓▓▓█▓▓▓▓▓▒▓░░██▓▓▓▓█▒▓█▓░▒▒░░▓█▓████░▒░░░░░░░░░░░▒▒▒▒▒░░░▒███▓▓▓▓▓▓▓▓▓░▒█▒▓██▓▓░░▒░
░▓▒▒▓█▒▒▓█▒▓▓▒░░▓███▓██▓▓██████▓█▓▒▓█████████████░░░░░░░███▒▒▓▒▒▓▒█▓▓▒▓▓█░▓▒░▓▓█▓░░░
░▒▒▒▒▒▒▓░▒░░░▒▓░░░░▒█▒▒██▓█▓▓▓█▓▓▓█▓█░▒███░░░░░▒█████████▓███▓█▒█▓▒▒▓░▒░▒▓▒▓▓▒█▒▓█▒░
░▒█▒░░▓▒▒▒░░░░░▒░░░░░▓▓▒▓░▒▒█▒▓▓█░▒░█░▓░░█░░░░░░░░░░░█░░░░░░░█▒▓░▒█░▒▓█▒▒▓▓░▒▒▒▒█░▓▒
░█░▒█▓█░░█▓█▒█████▒▓░▒▒▓▒██░▒▓█░▓▓▒░███████▒█▓▒▒░░▒▓█░▒░░░░░░▒███████████████░█▒▒▓▒░
░▓█▓░▓▓█▓▓▓█▒░▒█░░▓▓▒█▓██▓▒█▓░▒▓▓░▒▒█▒░░░░█▒██░███▒██░██░░░░░░░▒▒░░░░░░░░▒▒▒█████▓▓░
▒▓▒▓▓▒▓▒▓██░▒▓▒░▒▓▒██▓▒▒░▓▓░▒▓▓▒█████▓░░░░██▒░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░▓▒░
░▒█▒▓▒▒▒▓░▒█▒░▓█░▒█▓░█▓██▒▓██▒██░░░░██░░░░░░░▓██▓████▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░██░
░▒▒█▓▓█▒▓█▒░▒▓▒░▓█▒▓▓░█░▒█▒▒▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
░▒░░░▒░▒▒░█░░░▒▓▓▓▓░▒░██▓░▒██▓░░░░░░░░░░▓███░██░░░██░░░███▒▒█░▓█░░░░░░░░░░░░░░░░░░░░
░▒▓▓░█░▒█▓▓██▓█████████████▒█░░░░░░░░░░░▓█░█░██░░████░█░░░░▒██▓░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░