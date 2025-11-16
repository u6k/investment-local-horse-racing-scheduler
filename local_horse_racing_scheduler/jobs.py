import os
from datetime import datetime, timedelta

import local_horse_racing_scheduler.utils as utils

L = utils.get_logger(__name__)


def post_crawl_at_today():
    L.debug("#post_crawl_at_today: start")
    try:
        date = datetime.now().strftime("%Y%m%d")
        msg = f'{{"start_url":"https://nar.netkeiba.com/top/race_list_sub.html?kaisai_date={date}","AWS_S3_FEED_URL":"s3://{os.environ.get("AWS_S3_BUCKET")}/feed/calendar/calendar_{date}.json","RECACHE_RACE":"True","RECACHE_DATA":"False"}}'

        utils.post_message(msg)
        L.debug(f"{msg=}")
    except:  # noqa
        L.exception("post_crawl_at_today")


def post_crawl_at_yesterday():
    L.debug("#post_crawl_at_yesterday: start")
    try:
        date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
        msg = f'{{"start_url":"https://nar.netkeiba.com/top/race_list_sub.html?kaisai_date={date}","AWS_S3_FEED_URL":"s3://{os.environ.get("AWS_S3_BUCKET")}/feed/calendar/calendar_{date}.json","RECACHE_RACE":"True","RECACHE_DATA":"False"}}'

        utils.post_message(msg)
        L.debug(f"{msg=}")
    except:  # noqa
        L.exception("post_crawl_at_yesterday")
