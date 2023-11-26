# Automate process of creating AWS labs on ACloudGuru

# Pip Requirements: 
```
pip install selenium
pip3 install selenium

```

# Generate AWS Sandbox Credentials on ACloudGuru and save to .bashrc
```
$ python3 acloudguru.py 
Login successful
Username: cloud_user
Password: fLn^]1o(A39E5z)KmaIZ
URL: https://611144235625.signin.aws.amazon.com/console?region=us-east-1
access_key_id: AKIAY4SYI7JUX2KZPDMN
secret_access_key: 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
Environment variables added to .bashrc


# AWS Credentials set by script
export AWS_USERNAME="cloud_user"
export AWS_PASSWORD="fLn^]1o(A39E5z)KmaIZ"
export AWS_URL="https://611144235625.signin.aws.amazon.com/console?region=us-east-1"
export AWS_ACCESS_KEY_ID="AKIAY4SYI7JUX2KZPDMN"
export AWS_SECRET_ACCESS_KEY="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"

```