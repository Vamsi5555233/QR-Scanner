#QR Code Generator
import qrcode


def generate_qr_code(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data (URL or any text) to the QR code object
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image object from the QR code object
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")


# Example usage
if __name__ == "__main__":
    data = input("Enter the URL or text to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code image (e.g., qr_code.png): ")
    generate_qr_code(data, filename)
