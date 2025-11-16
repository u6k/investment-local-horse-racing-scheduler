import os
import re
from datetime import datetime, timedelta

import local_horse_racing_scheduler.utils as utils

L = utils.get_logger(__name__)


start_time_pattern = r"(\d{2}):(\d{2})発走"
start_date_pattern = r"(\d{4})年(\d{1,2})月(\d{1,2})日"


def add_crawl_race_jobs(scheduler):
    L.debug("#add_crawl_race_jobs: start")

    s3_client = utils.S3Client()

    target_date = datetime.now()
    key_calendar = f"feed/calendar/calendar_{target_date.strftime("%Y%m%d")}.json"
    L.debug(f"reading...{key_calendar}")

    list_calendar = s3_client.get_json(key_calendar)

    for item in list_calendar:
        if item["url"][0].endswith("#race_info"):
            race_url = item["url"][0].replace("#race_info", "")
            race_id = item["race_id"][0]

            start_time_re = re.search(start_time_pattern, item["race_data1"][0])
            start_date_re = re.search(start_date_pattern, item["race_data3"][0])

            if start_time_re is None or start_date_re is None:
                continue

            start_hour = int(start_time_re.group(1))
            start_minute = int(start_time_re.group(2))
            start_year = int(start_date_re.group(1))
            start_month = int(start_date_re.group(2))
            start_day = int(start_date_re.group(3))
            start_datetime = datetime(start_year, start_month, start_day, start_hour, start_minute, 0)

            L.debug(f"{start_datetime=}")

            for before_minutes in [30, 20, 15, 10, 5, 2]:
                crawl_datetime = start_datetime - timedelta(minutes=before_minutes)

                L.debug(f"add post_crawl_at_race job: {crawl_datetime=}, {race_url=}, {race_id=}, {target_date=}, {before_minutes=}")
                scheduler.add_job(
                    post_crawl_at_race,
                    "date",
                    run_date=crawl_datetime,
                    misfire_grace_time=None,
                    args=[crawl_datetime, race_url, race_id, target_date, before_minutes],
                )


def post_crawl_at_race(crawl_datetime, race_url, race_id, target_date, before_minutes):
    L.debug(f"#post_crawl_at_race: start: {crawl_datetime=}, {race_url=}, {race_id=}, {target_date=}, {before_minutes=}")
    try:
        json_name = f"race_{race_id}_before_{before_minutes}minutes.json"
        msg = f'{{"start_url":"{race_url}","AWS_S3_FEED_URL":"s3://{os.environ.get("AWS_S3_BUCKET")}/feed/racelist/{target_date.strftime("%Y%m%d")}/{json_name}","RECACHE_RACE":"True","RECACHE_DATA":"False"}}'

        utils.post_message(msg)
        L.debug(f"{msg=}")
    except:  # noqa
        L.exception("post_crawl_at_race")


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
