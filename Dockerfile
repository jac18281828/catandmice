ARG VERSION=102221

FROM jac18281828/pythondev:${VERSION} 

# build project
ARG PROJECT=catandmice
WORKDIR /workspaces/${PROJECT}

COPY bin bin/
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD /bin/bash -c "bin/catandmice.py {1..9} 1{0..9}"
