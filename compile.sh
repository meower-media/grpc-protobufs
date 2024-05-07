#!/bin/bash

# Python
python -m pip install grpcio-tools
python -m grpc_tools.protoc -I ./auth --python_out=output/py --pyi_out=output/py --grpc_python_out=output/py ./auth/auth_service.proto
python -m grpc_tools.protoc -I ./uploads --python_out=output/py --pyi_out=output/py --grpc_python_out=output/py ./uploads/uploads_service.proto

# Golang
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
protoc -I=./auth --go_out=./output/go ./auth/auth_service.proto
protoc -I=./uploads --go_out=./output/go ./uploads/uploads_service.proto
