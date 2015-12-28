#!/bin/sh

if [ -d "implementation" ]
then
	if [ -f "implementation/secret_settings.py" ]
    then
        echo "File secret_settings.py already exists. Please delete or rename and retry.\n"
    else
        printf "\"\"\"Settings which MUST NOT be included in version control.\"\"\"

SECRET_KEY = 'SET ME'
ENCRYPTED_LOOKUP_SECRET_KEY = 'SET ME'
" > implementation/secret_settings.py
    fi
else
	echo "Directory ./implementation not found. Are you in the django project root?\n"
fi
