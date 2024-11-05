# Steps:

1. Start the opentelemetry-collector container (gRPC server) with the following command:
```
docker run -p 4317:4317 -p 4318:4318 --rm -v <full path to collector-config.yaml>:/etc/otelcol/config.yaml otel/opentelemetry-collector
```

2. Initialize a virtual environment and install dependencies from requirements.txt.

3. Run the gRPC client script:
```
python grpc_client.py
```
