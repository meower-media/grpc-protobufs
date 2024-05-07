#!/bin/bash

# Python
python -m pip install grpcio-tools
python -m grpc_tools.protoc -I ./server --python_out=output/py --pyi_out=output/py --grpc_python_out=output/py ./server/server_service.proto
python -m grpc_tools.protoc -I ./uploads --python_out=output/py --pyi_out=output/py --grpc_python_out=output/py ./uploads/uploads_service.proto

# Golang
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
protoc -I=./server --go_out=./output/go ./server/server_service.proto
protoc -I=./uploads --go_out=./output/go ./uploads/uploads_service.proto
