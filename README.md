A blogsite created in django for understanding and learning django concepts.

For installing this site on your computer install the following modules using pip command or whatever you are comfortable with inside the project.
1.pyhton-social-auth
2.django-wysiwyg
3.ckeditor
4.django-crispyforms

For implementing the facebook authentication functionality register your app on facebook and then save the following contents inside the config.py
1.SOCIAL_AUTH_FACEBOOK_KEY = 'your_fb_app_key'
2.SOCIAL_AUTH_FACEBOOK_SECRET = 'your_fb_secret_key'
3.SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/welcome/'

As facebook works with real urls only so facebook will show error if you try to run this app using localhost or 127.0.0.1:8000
So make an entry into your /etc/hosts file like this:- "127.0.0.1  test1.com"

Feel free to create pull requests and improve the project.
