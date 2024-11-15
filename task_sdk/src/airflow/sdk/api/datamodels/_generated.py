# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# generated by datamodel-codegen:
#   filename:  http://0.0.0.0:9091/execution/openapi.json
#   version:   0.26.3

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Literal

from pydantic import BaseModel, Field


class ConnectionResponse(BaseModel):
    """
    Connection schema for responses with fields that are needed for Runtime.
    """

    conn_id: Annotated[str, Field(title="Conn Id")]
    conn_type: Annotated[str, Field(title="Conn Type")]
    host: Annotated[str | None, Field(title="Host")] = None
    schema_: Annotated[str | None, Field(alias="schema", title="Schema")] = None
    login: Annotated[str | None, Field(title="Login")] = None
    password: Annotated[str | None, Field(title="Password")] = None
    port: Annotated[int | None, Field(title="Port")] = None
    extra: Annotated[str | None, Field(title="Extra")] = None


class IntermediateTIState(str, Enum):
    """
    States that a Task Instance can be in that indicate it is not yet in a terminal or running state
    """

    REMOVED = "removed"
    SCHEDULED = "scheduled"
    QUEUED = "queued"
    RESTARTING = "restarting"
    UP_FOR_RETRY = "up_for_retry"
    UP_FOR_RESCHEDULE = "up_for_reschedule"
    UPSTREAM_FAILED = "upstream_failed"
    DEFERRED = "deferred"


class TIEnterRunningPayload(BaseModel):
    """
    Schema for updating TaskInstance to 'RUNNING' state with minimal required fields.
    """

    state: Annotated[Literal["running"] | None, Field(title="State")] = "running"
    hostname: Annotated[str, Field(title="Hostname")]
    unixname: Annotated[str, Field(title="Unixname")]
    pid: Annotated[int, Field(title="Pid")]
    start_date: Annotated[datetime, Field(title="Start Date")]


class TIHeartbeatInfo(BaseModel):
    """
    Schema for TaskInstance heartbeat endpoint.
    """

    hostname: Annotated[str, Field(title="Hostname")]
    pid: Annotated[int, Field(title="Pid")]


class TITargetStatePayload(BaseModel):
    """
    Schema for updating TaskInstance to a target state, excluding terminal and running states.
    """

    state: IntermediateTIState


class TerminalTIState(str, Enum):
    """
    States that a Task Instance can be in that indicate it has reached a terminal state
    """

    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


class ValidationError(BaseModel):
    loc: Annotated[list[str | int], Field(title="Location")]
    msg: Annotated[str, Field(title="Message")]
    type: Annotated[str, Field(title="Error Type")]


class VariableResponse(BaseModel):
    """
    Variable schema for responses with fields that are needed for Runtime.
    """

    key: Annotated[str, Field(title="Key")]
    value: Annotated[str | None, Field(title="Value")] = None


class XComResponse(BaseModel):
    """
    XCom schema for responses with fields that are needed for Runtime.
    """

    key: Annotated[str, Field(title="Key")]
    value: Annotated[Any, Field(title="Value")]


class HTTPValidationError(BaseModel):
    detail: Annotated[list[ValidationError] | None, Field(title="Detail")] = None


class TITerminalStatePayload(BaseModel):
    """
    Schema for updating TaskInstance to a terminal state (e.g., SUCCESS or FAILED).
    """

    state: TerminalTIState
    end_date: Annotated[datetime, Field(title="End Date")]
