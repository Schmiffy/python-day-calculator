FROM python:alpine3.14
COPY day_calculator.py day_calculator.py
ENTRYPOINT [ "python" ]
CMD [ "day_calculator.py" ]
