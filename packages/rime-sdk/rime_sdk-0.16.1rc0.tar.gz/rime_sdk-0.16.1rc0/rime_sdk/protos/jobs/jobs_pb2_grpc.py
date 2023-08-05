# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rime_sdk.protos.jobs import jobs_pb2 as protos_dot_jobs_dot_jobs__pb2


class JobManagerStub(object):
    """JobManager is an interface for interacting with job state in the DB.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpsertJob = channel.unary_unary(
                '/rime.JobManager/UpsertJob',
                request_serializer=protos_dot_jobs_dot_jobs__pb2.UpsertJobRequest.SerializeToString,
                response_deserializer=protos_dot_jobs_dot_jobs__pb2.UpsertJobResponse.FromString,
                )


class JobManagerServicer(object):
    """JobManager is an interface for interacting with job state in the DB.
    """

    def UpsertJob(self, request, context):
        """UpsertJob should NOT be exposed to external users.
        It should only be used by the data plane agent or the RIME engine.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JobManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpsertJob': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertJob,
                    request_deserializer=protos_dot_jobs_dot_jobs__pb2.UpsertJobRequest.FromString,
                    response_serializer=protos_dot_jobs_dot_jobs__pb2.UpsertJobResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.JobManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JobManager(object):
    """JobManager is an interface for interacting with job state in the DB.
    """

    @staticmethod
    def UpsertJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.JobManager/UpsertJob',
            protos_dot_jobs_dot_jobs__pb2.UpsertJobRequest.SerializeToString,
            protos_dot_jobs_dot_jobs__pb2.UpsertJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
