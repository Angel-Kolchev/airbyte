#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_google_business_profile_performance import SourceGoogleBusinessProfilePerformance

if __name__ == "__main__":
    source = SourceGoogleBusinessProfilePerformance()
    launch(source, sys.argv[1:])
