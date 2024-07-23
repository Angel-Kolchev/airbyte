#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_google_reviews import SourceGoogleReviews

if __name__ == "__main__":
    source = SourceGoogleReviews()
    launch(source, sys.argv[1:])
