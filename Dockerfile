FROM python:3

RUN git clone https://gist.github.com/bc90582aadd7d466fef67aed524d886d.git MyDealzInput
COPY . ./
RUN pip3 install -r requirements.txt

CMD [ "./wait-for-it.sh", "firefox:4444", "--", "python3", "-u", "run_docker.py" ]