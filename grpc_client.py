import grpc
from opentelemetry.proto.collector.logs.v1 import logs_service_pb2_grpc, logs_service_pb2
import time


def run():
    channel = grpc.insecure_channel('localhost:4317')
    stub = logs_service_pb2_grpc.LogsServiceStub(channel)
    request = logs_service_pb2.ExportLogsServiceRequest()
    resource_log = request.resource_logs.add()
    scope_log = resource_log.scope_logs.add()
    log_record = scope_log.log_records.add()
    log_record.time_unix_nano = time.time_ns()
    log_record.body.string_value = "Exporting the first log"
    response = stub.Export(request)
    print(response)


if __name__ == '__main__':
    run()
