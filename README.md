# QR Code Generator

This Python script generates QR codes from text or URLs. The QR codes can be scanned using a QR code reader or mobile device to access encoded data.

## Features

- Generates QR codes from URLs or any text input.
- Customizable appearance (error correction level, box size, border).
- Saves QR codes as image files (PNG format).

## Prerequisites

- Python 3.x
- `qrcode` and `Pillow` libraries

## Installation

1. Clone the Repository (if applicable):

   ```bash
   git clone [REPOSITORY_URL]
   cd [REPOSITORY_NAME]
2. Create and Activate a Virtual Environment (if not already created):
   python -m venv .venv
.\.venv\Scripts\Activate.ps1  # For PowerShell

3. Install Required Libraries:
   pip install qrcode[pil]
   pip install qrcode

**Usage:

1. Run the Script:
   python app.py
   
2.Follow the Prompts:

   Enter the URL or text to encode in the QR code: Type in the URL or text you want to encode.
   Enter the filename to save the QR code image: Specify the filename (e.g., qr_code.png).
   Example input:

   Data: https://www.example.com
   Filename: example_qr.png
   
3.Check the Output: The QR code image will be saved with the specified filename.

Example
To generate a QR code for https://www.google.com, you would:

Run the script.
Enter https://www.google.com when prompted for data.
Enter google_qr.png as the filename.
The generated QR code image (google_qr.png) will encode the URL. Scanning this QR code will open Google’s homepage.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to submit issues, enhancements, or pull requests to improve this project.

Contact
For any questions or feedback, please reach out to [Vamsi] at satyavoluvamsikrishna@gmail.com

Thanks

  


