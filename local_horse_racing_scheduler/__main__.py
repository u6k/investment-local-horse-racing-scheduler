import json
import os

from apscheduler.schedulers.blocking import BlockingScheduler

import local_horse_racing_scheduler.jobs as jobs
import local_horse_racing_scheduler.utils as utils

L = utils.get_logger(__name__)


if __name__ == "__main__":
    scheduler = BlockingScheduler()

    # 当日クロールをスケジュール登録
    cron_crawl_at_today = json.loads(os.environ.get("CRON_CRAWL_AT_TODAY"))
    L.debug(f"{cron_crawl_at_today=}")

    scheduler.add_job(
        jobs.post_crawl_at_today,
        "cron",
        misfire_grace_time=None,
        **cron_crawl_at_today,
    )

    # 昨日クロールをスケジュール登録
    cron_crawl_at_yesterday = json.loads(os.environ.get("CRON_CRAWL_AT_YESTERDAY"))
    L.debug(f"{cron_crawl_at_yesterday=}")

    scheduler.add_job(
        jobs.post_crawl_at_yesterday,
        "cron",
        misfire_grace_time=None,
        **cron_crawl_at_yesterday,
    )

    # スケジューラーを開始
    try:
        L.info("Starting scheduler")
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
        L.info("Shutting down scheduler")
