FROM python:3

WORKDIR .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#  API
CMD python -m unittest /api/tests/auth_tests.py

# UI
CMD python -m unittest /ui/tests/login_tests.py