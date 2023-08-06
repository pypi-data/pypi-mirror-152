
## TempEmail_py 
>inspired by https://pypi.org/project/minuteinbox-py/ 

##You can do with this package

* Create custom email
* get created email messages
* verify email is created or not
* delete your create email

## Description
>Create custom temporary e-mails and receive e-mails with MinuteInbox using python!. you can use these email in your projects

import library
```{python}
from TempEmail import TempEmail
```

## Exmaples
Create Custom email and receive mails
```{python}
custom_email="demoemail"
email,session,cookies,flag=create_email(custom_email)
if flag:
	while True:
		data=get_inbox(session,cookies)
		if data:
			print(data)
			break
		else:
			print("Waiting.....") 
		time.sleep(1)
```


email verify
```{python}
res=verify_email_isCreated(custom_email,session,cookies)
print(res) '''return true if email is created otherwise false
```

delete email 
```{python}
delete_mail(session,cookies,email) #return True if email is delete
```
 
## Disclaimer
I'm not associated in any way with MinuteInbox.com, if requested by them I will take down this repository. In this case please prove your Identity and send me an E-Mail. You can check my profile to find it.
