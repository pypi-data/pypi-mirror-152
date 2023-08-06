#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Francesco Murdaca
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This is Thoth Messaging module for AdviseJustificationMessage."""

import logging

from .message_base import MessageBase, BaseMessageContents
from pydantic import StrictStr, StrictInt

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.advise-reporter.advise-justification"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of advise justification message Kafka topic."""

    message: StrictStr
    justification_type: StrictStr
    count: StrictInt
    adviser_version: StrictStr
    version: StrictStr = "v1"


advise_justification_message = MessageBase(base_name=base_name, model=MessageContents)
