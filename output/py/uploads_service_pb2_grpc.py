# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import attachments_pb2 as attachments__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import icons_pb2 as icons__pb2
import moderation_pb2 as moderation__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in uploads_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UploadsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadIcon = channel.unary_unary(
                '/uploads.Uploads/UploadIcon',
                request_serializer=icons__pb2.UploadIconReq.SerializeToString,
                response_deserializer=icons__pb2.UploadIconResp.FromString,
                _registered_method=True)
        self.ClaimAttachment = channel.unary_unary(
                '/uploads.Uploads/ClaimAttachment',
                request_serializer=attachments__pb2.ClaimAttachmentReq.SerializeToString,
                response_deserializer=attachments__pb2.ClaimAttachmentResp.FromString,
                _registered_method=True)
        self.DeleteAttachment = channel.unary_unary(
                '/uploads.Uploads/DeleteAttachment',
                request_serializer=attachments__pb2.DeleteAttachmentReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.BlockFile = channel.unary_unary(
                '/uploads.Uploads/BlockFile',
                request_serializer=moderation__pb2.BlockFileReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UnblockFile = channel.unary_unary(
                '/uploads.Uploads/UnblockFile',
                request_serializer=moderation__pb2.UnblockFileReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class UploadsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadIcon(self, request, context):
        """Upload an icon & get its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClaimAttachment(self, request, context):
        """Claim & get details about an attachment by its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAttachment(self, request, context):
        """Delete an attachment by its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BlockFile(self, request, context):
        """Block file by its hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnblockFile(self, request, context):
        """Unblock file by its hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UploadsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadIcon': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadIcon,
                    request_deserializer=icons__pb2.UploadIconReq.FromString,
                    response_serializer=icons__pb2.UploadIconResp.SerializeToString,
            ),
            'ClaimAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.ClaimAttachment,
                    request_deserializer=attachments__pb2.ClaimAttachmentReq.FromString,
                    response_serializer=attachments__pb2.ClaimAttachmentResp.SerializeToString,
            ),
            'DeleteAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAttachment,
                    request_deserializer=attachments__pb2.DeleteAttachmentReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'BlockFile': grpc.unary_unary_rpc_method_handler(
                    servicer.BlockFile,
                    request_deserializer=moderation__pb2.BlockFileReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UnblockFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UnblockFile,
                    request_deserializer=moderation__pb2.UnblockFileReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uploads.Uploads', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Uploads(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadIcon(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/UploadIcon',
            icons__pb2.UploadIconReq.SerializeToString,
            icons__pb2.UploadIconResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClaimAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/ClaimAttachment',
            attachments__pb2.ClaimAttachmentReq.SerializeToString,
            attachments__pb2.ClaimAttachmentResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/DeleteAttachment',
            attachments__pb2.DeleteAttachmentReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BlockFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/BlockFile',
            moderation__pb2.BlockFileReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnblockFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/UnblockFile',
            moderation__pb2.UnblockFileReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
