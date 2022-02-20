#For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

## old configuration:
EMAIL_USE_TLS = False
EMAIL_HOST = 'harenconstruction-com.mail.protection.outlook.com' # 'smtp.office365.com'
EMAIL_HOST_USER = 'jobs@harenconstruction.com'
#Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = 'Son26800' # 'Wadu4797' # 'HarenC123'
EMAIL_PORT = 25 #587

# noah configuration:
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.office365.com'
#EMAIL_HOST_USER = 'jobs@harenconstruction.com'
#EMAIL_HOST_PASSWORD = 'Son26800'
#EMAIL_PORT = 587

#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
