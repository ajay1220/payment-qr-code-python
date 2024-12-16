import qrcode
import urllib.parse

# Taking UPI ID and other details as input
upi_id = input("Enter your UPI ID: ")
recipient_name = input("Enter recipient's name: ")
amount = input("Enter amount: ")
currency = input("Enter currency (e.g., INR): ")
message = input("Enter transaction message: ")

# URL encoding the recipient's name and message
encoded_recipient_name = urllib.parse.quote(recipient_name)
encoded_message = urllib.parse.quote(message)

# Defining the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn={encoded_recipient_name}&am={amount}&cu={currency}&tn={encoded_message}'
paytm_url = f'upi://pay?pa={upi_id}&pn={encoded_recipient_name}&am={amount}&cu={currency}&tn={encoded_message}'
google_pay_url = f'upi://pay?pa={upi_id}&pn={encoded_recipient_name}&am={amount}&cu={currency}&tn={encoded_message}'

# Create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code to image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')  # Fixed typo here
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (you may need to install the Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()