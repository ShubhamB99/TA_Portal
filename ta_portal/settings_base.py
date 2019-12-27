
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ay0lu)jff!uh=a1389s9m2ps#q)+019g*-f&##9jdh&zkv*wv8'

BASE_URL = 'https://gymkhana.iitb.ac.in/~ugacademics/TA_PORTAL/'
STATIC_BASE_URL = 'https://gymkhana.iitb.ac.in/~ugacademics/TA_PORTAL/'

#ALLOWED_HOSTS = ['temp-iitb.radialapps.com']

SSO_TOKEN_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
SSO_STUDENT_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,sex,username,email,program,contacts,insti_address,secondary_emails,mobile,roll_number'
SSO_FACULTY_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,sex,username,email,program'
SSO_CLIENT_ID = 'z3E7yusTYcwJVy1o3AsFVro2EC18ntwAnBEIJLM4'
SSO_CLIENT_ID_SECRET_BASE64 = 'ejNFN3l1c1RZY3dKVnkxbzNBc0ZWcm8yRUMxOG50d0FuQkVJSkxNNDpRbHpjUlliVkxtMWhNRlBYNm5jd3Y0Qzc1b1V4UlRydXZ3NG1zb1hVa0c1eTdpQzhncjJyMm5rbndyZUQzRmlFM1l4V2diMXdYMjJFU3VPWDk4ZVY4RExobEtzbzZBMlhsNkhEWHpNVEtFRTZqOFlVNEN0ZGV6SmJOUmxscVI4RA=='

# Flip for broken external server certificates
SSO_BAD_CERT = False
