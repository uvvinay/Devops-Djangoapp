#use official python image from docker

FROM python:3.12.3

WORKDIR /CRMPOJECT

#working directory
COPY crmproject/ ./
COPY requirements.txt ./
COPY templates/ ./
COPY /accountsapp/ ./
COPY templates/ .accounts/login/ ./

#install requirement packeges
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [  "manage.py","runserver" ]
