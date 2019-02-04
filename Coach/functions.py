

def signup_email_message(student):
    message = '''{name}, 
    
Your academic coach, {academic_coach}, has invited you to join Vana Learning! Vana is a platform that helps academic coaches,
students, and parents stay on the same page when it comes to school. In order to make your account, please go to the link
below and create your password. Your username has already been created for you.

Username: {username}
https://www.vanalearning.com/signup/{username}

Please let {academic_coach} know if you have any questions. 

Best of luck,
The Vana Learning Team
'''.format(name=student.name, academic_coach='Marni Pasch', username=student.username)
    return message

