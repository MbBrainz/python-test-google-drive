#Deriving the latest base image
FROM python:latest



#Labels as key value pair
LABEL Maintainer="MbBrainz.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
# COPY src/ app.py ./
ADD src .

# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

RUN pip install -r drive/requirements.txt
RUN pip install -r simulation/ABM-project-group8/requirements.txt
# run specific simulation from within package
# RUN cd simulation/ABM-project-group8/ && python -m polarization.experiments.experiments

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
# run upload files
CMD [ "python", "./main.py"]