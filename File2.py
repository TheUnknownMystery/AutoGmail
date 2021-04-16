import smtplib

Prank = input("EnterPrankCaller")
with smtplib.SMTP('smtp.gmail.com', 587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.ehlo()

    smpt.login("you gmail here", "you password here")

    s = 'Introdunction'
    b = 'Hello'

    msg = f'Subject:{s}\n\n{b}'

    for i in range(1):
        smpt.sendmail("your gamil", Prank, msg)
