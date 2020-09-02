FROM python:3

# RUN git clone https://gist.github.com/bc90582aadd7d466fef67aed524d886d.git MyDealzInput
# WORKDIR /Programmierung/MyDealzInput
COPY ./run_docker.py ./
COPY ./wait-for-it.sh ./
COPY ./requirements.txt ./
COPY ./cookies.json ./
COPY ./UdemyPicker.py ./

RUN pip3 install -r requirements.txt

CMD [ "ls MydealzInput" ]
# CMD [ "./wait-for-it.sh", "firefox:4444", "--", "python3", "-u", "run_docker.py" ]