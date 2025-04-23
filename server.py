import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
from calculatorTask import CalculatorTask

class CalculatorServiceServicer(calculator_pb2_grpc.CalculatorServiceServicer):
    def SendRequest(self, request, context):
        try:
            res = CalculatorTask().calculate(request.payload)
            return calculator_pb2.Result(result=str(res))
        except Exception as e:
            return calculator_pb2.Result(error_code=400, error_message=str(e))
    def SendPing(self, request, context):
        return calculator_pb2.Ping(count=request.count+1)
    
def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(CalculatorServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    run()
    