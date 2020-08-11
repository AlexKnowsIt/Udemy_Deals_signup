FROM python:3


COPY . ./
RUN pip3 install -r requirements.txt

CMD [ "./wait-for-it.sh", "firefox:4444", "--", "python3", "-u", "UdemyPicker_docker.py" ]