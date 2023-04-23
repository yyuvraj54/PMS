from tkinter import *
import os

def nextPage():
    root.destroy()
    

    


root = Tk()
root.title('User Agreement for Personnel Monitoring Application')
root.geometry('1200x600')

# Biggest one
#Contract = 'BY ACCESSING OR USING THE APPLICATION, YOU AGREE TO BE BOUND BY THE TERMS AND CONDITIONS OF THIS AGREEMENT. IF YOU DO NOT AGREE TO THE TERMS AND CONDITIONS OF THIS AGREEMENT, DO NOT USE OR ACCESS THE APPLICATION. \n1. PURPOSE OF THE APPLICATION: The Application is designed to monitor and track the attendance and location of personnel employed by the Government of India.\n2. USE OF THE APPLICATION: The User shall use the Application only for its intended purposes and in accordance with applicable laws and regulations. The User shall not use the Application to engage in any illegal or unethical activities, including but not limited to hacking, unauthorized access, or misuse of data.\n3. DATA PRIVACY: The Government of India shall ensure that all personal data collected by the Application is handled in accordance with applicable data protection laws and regulations. The User acknowledges and agrees that the Government may collect, use, and disclose personal data for the purposes of administering the Application.\n4. LIMITATION OF LIABILITY: The Government of India shall not be liable for any loss or damage suffered by the User or any third party arising from the use of the Application, including but not limited to any errors or omissions in the data provided by the Application.\n5. INTELLECTUAL PROPERTY: The Application and all intellectual property rights in the Application are owned by the Government of India. The User shall not reproduce, modify, or distribute any part of the Application without the prior written consent of the Government.\n6. TERMINATION: The Government of India may terminate this Agreement at any time without notice if the User breaches any of the terms and conditions of this Agreement.\n7. GOVERNING LAW: This Agreement shall be governed by and construed in accordance with the laws of India.\n8. ENTIRE AGREEMENT: This Agreement constitutes the entire agreement between the User and the Government of India with respect to the use of the Application and supersedes all prior agreements and understandings, whether written or oral.\n9. AMENDMENTS: The Government of India reserves the right to amend this Agreement at any time without notice by posting the amended terms on the Application.\n10. ACCEPTANCE OF AGREEMENT: By accessing or using the Application, the User acknowledges that they have read this Agreement, understand it, and agree to be bound by its terms and conditions.'
ContractHead='TERMS AND CONDITIONS:'

Contract = "\n\n1. Purpose of Agreement - This User Agreement is for the Personnel Monitoring Application of the Government of India.\n\n2. Application Usage - The Application is intended to monitor and track attendance and location of personnel employed by the Government of India.\nThe User shall use the Application only for its intended purposes and in accordance with applicable laws and regulations.\n\n3. Personal Data Protection - The Government of India shall ensure that all personal data collected by the Application is handled in accordance with applicable data protection laws and regulations.\nThe Government shall not be liable for any loss or damage arising from the use of the Application.\n\n4. Intellectual Property Rights - The Application and all intellectual property rights in the Application are owned by the Government of India.\nThe User agrees not to reproduce, modify or distribute any part of the Application without prior written consent.\n\n5. Termination of Agreement - The Government of India may terminate the Agreement if the User breaches any of the terms and conditions.\nThe User accepts the Agreement by accessing or using the Application."
# Smallest one
#Contract = "This User Agreement is between the User and the Government of India for the use of the Personnel Monitoring Application. The Application is intended to monitor and track attendance and location of personnel employed by the Government of India. The User agrees to use the Application only for its intended purposes and in accordance with applicable laws and regulations. The Government of India shall handle all personal data collected by the Application in accordance with applicable data protection laws and regulations. The Government shall not be liable for any loss or damage suffered by the User or any third party arising from the use of the Application. The Application and all intellectual property rights in the Application are owned by the Government of India. The User agrees not to reproduce, modify or distribute any part of the Application without prior written consent. The Government of India may terminate this Agreement at any time without notice if the User breaches any of the terms and conditions of this Agreement."
# Middle one
# Contract = "This User Agreement governs the use of the Personnel Monitoring Application by the User and is entered into with the Government of India. The Application is designed to monitor and track attendance and location of personnel employed by the Government of India. The User agrees to use the Application only for its intended purposes and in accordance with applicable laws and regulations. The Government of India shall ensure that all personal data collected by the Application is handled in accordance with applicable data protection laws and regulations. The User acknowledges and agrees that the Government may collect, use and disclose personal data for the purposes of administering the Application.\nThe Government shall not be liable for any loss or damage suffered by the User or any third party arising from the use of the Application, including but not limited to any errors or omissions in the data provided by the Application. The Application and all intellectual property rights in the Application are owned by the Government of India. The User agrees not to reproduce, modify or distribute any part of the Application without prior written consent.\nThe Government of India may terminate this Agreement at any time without notice if the User breaches any of the terms and conditions of this Agreement. This Agreement constitutes the entire agreement between the User and the Government of India with respect to the use of the Application and supersedes all prior agreements and understandings, whether written or oral. The User accepts this Agreement by accessing or using the Application. If you have any questions about this Agreement, please contact the Government of India at the contact information provided on the Application."
contractHead = Label(root, text=ContractHead, justify=CENTER)
contractHead.pack()
contract = Label(root, text=Contract, justify=LEFT,wraplength=800, height=28)
contract.pack()

login_btn = PhotoImage(file="Screens/images/agreenconblue.png")

# agree = Button(root, text=' Agree and Continue', background='#0063BF')
agree = Button(root, image=login_btn, borderwidth=0,command=nextPage)
agree.pack(pady=10)

# root.protocol("WM_DELETE_WINDOW", nextPage)
root.mainloop()
