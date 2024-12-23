import qrcode

def generate_qr_code(url):
    # Create a QR code from the URL
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction
        box_size=10,  # size of each box in the QR code grid
        border=4,  # thickness of the border
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image or show it
    img.save("qr_code.png")
    img.show()

# Input URL from the user
web_link = input("Enter the URL to generate QR code: ")
generate_qr_code(web_link)
