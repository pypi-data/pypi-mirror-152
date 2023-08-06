#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Kevin Postlethwait
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


"""This is Thoth Messaging module for HashMismatchMessage."""

import logging
from typing import List

from pydantic import StrictStr

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.package-update.hash-mismatch"


class MessageContents(BaseMessageContents):
    """Class used to represent a contents of a hash-mismatch message Kafka topic."""

    index_url: StrictStr
    package_name: StrictStr
    package_version: StrictStr
    missing_from_source: List[StrictStr]
    missing_from_database: List[StrictStr]
    version: StrictStr = "v1"


hash_mismatch_message = MessageBase(base_name=base_name, model=MessageContents)
