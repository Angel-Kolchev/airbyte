#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceGoogleReviews

def run():
    source = SourceGoogleReviews()
    launch(source, sys.argv[1:])
