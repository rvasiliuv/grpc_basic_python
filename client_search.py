import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel_2 = grpc.insecure_channel('localhost:50053')

# create a stub (client)
stub_2 = calculator_pb2_grpc.SearchEngineStub(channel_2)

search_request = calculator_pb2.SearchRequest(query = 'This is a search query')

search_response = stub_2.GetSearchAnswer(search_request)

# finally
print(search_response)