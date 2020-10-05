FROM python:3

WORKDIR .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome browser
RUN apt-get update && apt-get -y install google-chrome-stable

COPY . .

#  API
# CMD python -m unittest /api/tests/auth_tests.py

# UI
CMD python -m unittest /ui/tests/login_tests.py