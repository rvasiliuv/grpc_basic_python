import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

# create a class to define the server functions, derived from calculator_pg2_grpc.CalculatorServer
class CalculatorServer(calculator_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type calculator_pb2.Number

    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

    def Sine(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.sine_of(request.value)
        return response


class SearchEngineServer(calculator_pb2_grpc.SearchEngineServicer):

    # calculator functions exposed here
    # data type is calculator.pb2_SearchRequest, SearchResponse

    def GetSearchAnswer(self, request, context):
        response = calculator_pb2.SearchResponse()
        response.response = calculator.search(request.query)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function 'add_CalculatorServicer_to_server to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServer(), server)
calculator_pb2_grpc.add_SearchEngineServicer_to_server(SearchEngineServer(), server)

# listen on port 50051
print('Starting Server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
print('Initialising port 50052 as well')
server.add_insecure_port('[::]:50052')
server.start()

# since server.start() will not block a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)