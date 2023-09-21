# bibliotecas 
# funçao que converte texto a qr
# salvar o qr como uma img
# iniciar

import qrcode

def genereate_qrcode(text):
    
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROT_CORRECT_L,
        box_size= 10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")
    
url = input('Entre com sua url: ')    
genereate_qrcode(url)