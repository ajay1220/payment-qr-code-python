import qrcode

# taking upi id as a input
upi_id = input ("Enter your UPI ID =")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defing the payment URL based on the UPI ID and the payment app
# you can modify the URL based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234'

#create QR coder for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr cord to image file 

phonepe_qr.save ('phonepe_qr.png')
paytm_qr.save ('patm_qr.png')
google_pay_qr.save ('google_pay_qr.png')

# display the qr codes ( you may need to intall pil/ pillow library)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

