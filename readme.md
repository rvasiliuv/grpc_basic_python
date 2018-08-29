 
## gRPC related packages:
$ pip install grpcio
$ pip install grpcio-tools

## In your folder run the following in order to generate classes
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

## To run:
$ python server.py
$ python client.py

