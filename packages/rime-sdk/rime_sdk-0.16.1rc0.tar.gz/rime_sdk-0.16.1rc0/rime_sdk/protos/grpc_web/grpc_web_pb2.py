# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/grpc_web/grpc_web.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eprotos/grpc_web/grpc_web.proto\x12\x04rime\x1a\x1bgoogle/protobuf/empty.proto\"Z\n\x1cResolveSingleTestCaseRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\x12\x0f\n\x07test_id\x18\x02 \x01(\t\x12\x14\n\x0ctest_case_id\x18\x03 \x01(\t\"Y\n\x1aResolveAllTestCasesRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\x12\x0f\n\x07test_id\x18\x02 \x01(\t\x12\x15\n\rtest_case_ids\x18\x03 \x03(\t\"D\n\x1cUnresolveAllTestCasesRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\x12\x0f\n\x07test_id\x18\x02 \x01(\t\"6\n\x1f\x41ggregateTestRunResolvedRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\"9\n AggregateTestRunResolvedResponse\x12\x15\n\rtest_case_ids\x18\x01 \x03(\t\"J\n\"AggregateSingleTestResolvedRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\x12\x0f\n\x07test_id\x18\x02 \x01(\t\"<\n#AggregateSingleTestResolvedResponse\x12\x15\n\rtest_case_ids\x18\x01 \x03(\t\"?\n\nTestConfig\x12\x12\n\x08\x63ontents\x18\x01 \x01(\x0cH\x00\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x08\n\x06\x63onfig\"@\n\x14GetTestConfigRequest\x12\x13\n\x0btest_run_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_name\x18\x02 \x01(\t\">\n\x15GetTestConfigResponse\x12%\n\x0btest_config\x18\x01 \x01(\x0b\x32\x10.rime.TestConfig2\x91\x05\n\x0eGRPCWebService\x12M\n\x0fResolveTestCase\x12\".rime.ResolveSingleTestCaseRequest\x1a\x16.google.protobuf.Empty\x12O\n\x11UnresolveTestCase\x12\".rime.ResolveSingleTestCaseRequest\x1a\x16.google.protobuf.Empty\x12O\n\x13ResolveAllTestCases\x12 .rime.ResolveAllTestCasesRequest\x1a\x16.google.protobuf.Empty\x12S\n\x15UnresolveAllTestCases\x12\".rime.UnresolveAllTestCasesRequest\x1a\x16.google.protobuf.Empty\x12r\n!AggregateTestRunResolvedTestCases\x12%.rime.AggregateTestRunResolvedRequest\x1a&.rime.AggregateTestRunResolvedResponse\x12{\n$AggregateSingleTestResolvedTestCases\x12(.rime.AggregateSingleTestResolvedRequest\x1a).rime.AggregateSingleTestResolvedResponse\x12H\n\rGetTestConfig\x12\x1a.rime.GetTestConfigRequest\x1a\x1b.rime.GetTestConfigResponseB\x18Z\x16ri/_gen/protos/grpcwebb\x06proto3')



_RESOLVESINGLETESTCASEREQUEST = DESCRIPTOR.message_types_by_name['ResolveSingleTestCaseRequest']
_RESOLVEALLTESTCASESREQUEST = DESCRIPTOR.message_types_by_name['ResolveAllTestCasesRequest']
_UNRESOLVEALLTESTCASESREQUEST = DESCRIPTOR.message_types_by_name['UnresolveAllTestCasesRequest']
_AGGREGATETESTRUNRESOLVEDREQUEST = DESCRIPTOR.message_types_by_name['AggregateTestRunResolvedRequest']
_AGGREGATETESTRUNRESOLVEDRESPONSE = DESCRIPTOR.message_types_by_name['AggregateTestRunResolvedResponse']
_AGGREGATESINGLETESTRESOLVEDREQUEST = DESCRIPTOR.message_types_by_name['AggregateSingleTestResolvedRequest']
_AGGREGATESINGLETESTRESOLVEDRESPONSE = DESCRIPTOR.message_types_by_name['AggregateSingleTestResolvedResponse']
_TESTCONFIG = DESCRIPTOR.message_types_by_name['TestConfig']
_GETTESTCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetTestConfigRequest']
_GETTESTCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['GetTestConfigResponse']
ResolveSingleTestCaseRequest = _reflection.GeneratedProtocolMessageType('ResolveSingleTestCaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOLVESINGLETESTCASEREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.ResolveSingleTestCaseRequest)
  })
_sym_db.RegisterMessage(ResolveSingleTestCaseRequest)

ResolveAllTestCasesRequest = _reflection.GeneratedProtocolMessageType('ResolveAllTestCasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOLVEALLTESTCASESREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.ResolveAllTestCasesRequest)
  })
_sym_db.RegisterMessage(ResolveAllTestCasesRequest)

UnresolveAllTestCasesRequest = _reflection.GeneratedProtocolMessageType('UnresolveAllTestCasesRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNRESOLVEALLTESTCASESREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.UnresolveAllTestCasesRequest)
  })
_sym_db.RegisterMessage(UnresolveAllTestCasesRequest)

AggregateTestRunResolvedRequest = _reflection.GeneratedProtocolMessageType('AggregateTestRunResolvedRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATETESTRUNRESOLVEDREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.AggregateTestRunResolvedRequest)
  })
_sym_db.RegisterMessage(AggregateTestRunResolvedRequest)

AggregateTestRunResolvedResponse = _reflection.GeneratedProtocolMessageType('AggregateTestRunResolvedResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATETESTRUNRESOLVEDRESPONSE,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.AggregateTestRunResolvedResponse)
  })
_sym_db.RegisterMessage(AggregateTestRunResolvedResponse)

AggregateSingleTestResolvedRequest = _reflection.GeneratedProtocolMessageType('AggregateSingleTestResolvedRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATESINGLETESTRESOLVEDREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.AggregateSingleTestResolvedRequest)
  })
_sym_db.RegisterMessage(AggregateSingleTestResolvedRequest)

AggregateSingleTestResolvedResponse = _reflection.GeneratedProtocolMessageType('AggregateSingleTestResolvedResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATESINGLETESTRESOLVEDRESPONSE,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.AggregateSingleTestResolvedResponse)
  })
_sym_db.RegisterMessage(AggregateSingleTestResolvedResponse)

TestConfig = _reflection.GeneratedProtocolMessageType('TestConfig', (_message.Message,), {
  'DESCRIPTOR' : _TESTCONFIG,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.TestConfig)
  })
_sym_db.RegisterMessage(TestConfig)

GetTestConfigRequest = _reflection.GeneratedProtocolMessageType('GetTestConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTESTCONFIGREQUEST,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetTestConfigRequest)
  })
_sym_db.RegisterMessage(GetTestConfigRequest)

GetTestConfigResponse = _reflection.GeneratedProtocolMessageType('GetTestConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTESTCONFIGRESPONSE,
  '__module__' : 'protos.grpc_web.grpc_web_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetTestConfigResponse)
  })
_sym_db.RegisterMessage(GetTestConfigResponse)

_GRPCWEBSERVICE = DESCRIPTOR.services_by_name['GRPCWebService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026ri/_gen/protos/grpcweb'
  _RESOLVESINGLETESTCASEREQUEST._serialized_start=69
  _RESOLVESINGLETESTCASEREQUEST._serialized_end=159
  _RESOLVEALLTESTCASESREQUEST._serialized_start=161
  _RESOLVEALLTESTCASESREQUEST._serialized_end=250
  _UNRESOLVEALLTESTCASESREQUEST._serialized_start=252
  _UNRESOLVEALLTESTCASESREQUEST._serialized_end=320
  _AGGREGATETESTRUNRESOLVEDREQUEST._serialized_start=322
  _AGGREGATETESTRUNRESOLVEDREQUEST._serialized_end=376
  _AGGREGATETESTRUNRESOLVEDRESPONSE._serialized_start=378
  _AGGREGATETESTRUNRESOLVEDRESPONSE._serialized_end=435
  _AGGREGATESINGLETESTRESOLVEDREQUEST._serialized_start=437
  _AGGREGATESINGLETESTRESOLVEDREQUEST._serialized_end=511
  _AGGREGATESINGLETESTRESOLVEDRESPONSE._serialized_start=513
  _AGGREGATESINGLETESTRESOLVEDRESPONSE._serialized_end=573
  _TESTCONFIG._serialized_start=575
  _TESTCONFIG._serialized_end=638
  _GETTESTCONFIGREQUEST._serialized_start=640
  _GETTESTCONFIGREQUEST._serialized_end=704
  _GETTESTCONFIGRESPONSE._serialized_start=706
  _GETTESTCONFIGRESPONSE._serialized_end=768
  _GRPCWEBSERVICE._serialized_start=771
  _GRPCWEBSERVICE._serialized_end=1428
# @@protoc_insertion_point(module_scope)
