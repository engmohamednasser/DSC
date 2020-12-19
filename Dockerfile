From python:3.8

ADD test.py .

RUN pip install --upgrade pip && \
    pip install numpy

CMD ["python" ,"./test.py"]
