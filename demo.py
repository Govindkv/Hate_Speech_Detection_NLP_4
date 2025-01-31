from HSD.logger import logging
from HSD.exception import CustomException
import sys

from HSD.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hsd_govindkv", "dataset.zip","dataset")