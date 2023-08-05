# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rime_sdk.protos.project import project_pb2 as protos_dot_project_dot_project__pb2


class ProjectManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProject = channel.unary_unary(
                '/rime.ProjectManager/CreateProject',
                request_serializer=protos_dot_project_dot_project__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.CreateProjectResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/rime.ProjectManager/GetProject',
                request_serializer=protos_dot_project_dot_project__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.GetProjectResponse.FromString,
                )
        self.UpdateProject = channel.unary_unary(
                '/rime.ProjectManager/UpdateProject',
                request_serializer=protos_dot_project_dot_project__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.UpdateProjectResponse.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/rime.ProjectManager/DeleteProject',
                request_serializer=protos_dot_project_dot_project__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.DeleteProjectResponse.FromString,
                )
        self.ListProjects = channel.unary_unary(
                '/rime.ProjectManager/ListProjects',
                request_serializer=protos_dot_project_dot_project__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.ListProjectsResponse.FromString,
                )
        self.ServeAvailableColumnsForProject = channel.unary_unary(
                '/rime.ProjectManager/ServeAvailableColumnsForProject',
                request_serializer=protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectRequest.SerializeToString,
                response_deserializer=protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectResponse.FromString,
                )


class ProjectManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateProject(self, request, context):
        """CRUD operations for projects.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServeAvailableColumnsForProject(self, request, context):
        """Serve available columns for a project derived from model tasks.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=protos_dot_project_dot_project__pb2.CreateProjectRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.CreateProjectResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=protos_dot_project_dot_project__pb2.GetProjectRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.GetProjectResponse.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=protos_dot_project_dot_project__pb2.UpdateProjectRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.UpdateProjectResponse.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=protos_dot_project_dot_project__pb2.DeleteProjectRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.DeleteProjectResponse.SerializeToString,
            ),
            'ListProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProjects,
                    request_deserializer=protos_dot_project_dot_project__pb2.ListProjectsRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.ListProjectsResponse.SerializeToString,
            ),
            'ServeAvailableColumnsForProject': grpc.unary_unary_rpc_method_handler(
                    servicer.ServeAvailableColumnsForProject,
                    request_deserializer=protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectRequest.FromString,
                    response_serializer=protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.ProjectManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/CreateProject',
            protos_dot_project_dot_project__pb2.CreateProjectRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/GetProject',
            protos_dot_project_dot_project__pb2.GetProjectRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/UpdateProject',
            protos_dot_project_dot_project__pb2.UpdateProjectRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.UpdateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/DeleteProject',
            protos_dot_project_dot_project__pb2.DeleteProjectRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.DeleteProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/ListProjects',
            protos_dot_project_dot_project__pb2.ListProjectsRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.ListProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServeAvailableColumnsForProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.ProjectManager/ServeAvailableColumnsForProject',
            protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectRequest.SerializeToString,
            protos_dot_project_dot_project__pb2.ServeAvailableColumnsForProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
