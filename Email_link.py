import imaplib, email

#---------------- Helper function email confirmation ---------------
'''
Function authenticates with gmail server and
retrieves Email confirmation link from the mail
mail id 
To make this work:
1. IMAP access should be on gmail account
2. Less secure access should be on (For working in all cases)
'''
def email_confirmation():
    # -------------- Gmail automation -------------------
    # 1. IMAP4 instance
    M = imaplib.IMAP4_SSL('imap.gmail.com')

    # 2. Login attempt
    try:
        M.login('USER_EMAIL', 'USER_PASS')
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "

    # 3. retrieve mail
    #M.select("cs2043")  # inbox
    M.select("inbox")
    response, Inbox = M.search(None, '(FROM "mail id")')

    if response == 'OK':
        mails = Inbox[0].split()  # mail id
        latest_mail = mails[-1]
        resp, data = M.fetch(latest_mail, "(RFC822)") # complete content
        raw_email_body = data[0][1]
        email_body = raw_email_body.decode('utf-8')
        mail = email.message_from_string(email_body)

        #walk through the content
        for part in mail.walk():
            if part.get_content_type() == "text/html":
                body = part.get_payload(decode=True)
                for word in body.split(' '):
                    if word.startswith('href="https://--website--'):
                        print word
                        link = word[6:-1]
                        return link
            else:
                continue


        print "No link found"
        M.close()

    M.logout()
