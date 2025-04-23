import sys
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run(task="ping", payload=""):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)
        if task.lower() == "ping":
            response = stub.SendPing(calculator_pb2.Ping(count=1))
            print (f"Ping response: {response.count}")
        elif payload != "":
            response = stub.SendRequest(calculator_pb2.Payload(payload=payload))
            if response.error_code:
                print (f"Error returned from calculator service. Error code={response.error_code}, message={response.error_message}")
            else:
                print (f"Result={response.result}")
        else:
            print ("Invalid input")
if __name__ == "__main__":
    if len(sys.argv) == 1:
        run()
    else:
        run("calculate", sys.argv[1])




