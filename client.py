import sys
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run(task="ping", payload=""):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
        if task.lower() == "ping":
            try:
                response = stub.SendPing(calculator_pb2.Ping(count=1))
                print (f"Ping response: {response.count}")
            except grpc.RpcError as e:
                print(f"Error in receiving ping message: {e}")
        elif payload != "":
            try:
                response = stub.SendRequest(calculator_pb2.Payload(payload=payload))
                print (f"Result={response.result}")
            except grpc.RpcError as e:
                print(f"Error in receiving calculator task response: {e}")
        else:
            print ("Invalid input")
if __name__ == "__main__":
    if len(sys.argv) == 1:
        run()
    else:
        run("calculate", sys.argv[1])




