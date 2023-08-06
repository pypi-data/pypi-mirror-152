# -*-coding:utf-8-*-
# Author: Eason.Deng
# Github: https://github.com/holbos-deng
# Email: 2292861292@qq.com
# CreateDate: 2022/5/23 14:42
# Description:
import re
import jionlp as jio
from math import ceil
from datetime import datetime
from nlp_time.utils import text_pre, around_today
from dateutil.relativedelta import relativedelta
from typing import Union


def get_time(text: str, tend_future=True):
    time_text, time_tuple = "", ("", "")
    try:
        text = text_pre(text)
        now = datetime.now()
        time_obj = jio.ner.extract_time(text) or {}
        if not time_obj:
            return "", time_tuple
        time_obj = time_obj[0]
        time_text = time_obj.get("text") or ""
        time_dict = time_obj.get("detail") or {}
        time_tuple = time_dict.get("time") or ["", ""]
        if "inf" in time_tuple[0]:
            t1 = None
        else:
            t1 = datetime.strptime(time_tuple[0], TIME_FORMAT)
        if "inf" in time_tuple[1]:
            t2 = None
        else:
            t2 = datetime.strptime(time_tuple[1], TIME_FORMAT)
        if time_dict.get("type", "") == "time_point":
            if re.findall(RE_WEEK, text):
                if tend_future:
                    if t1 and t1 < now:
                        t1 = t1 + relativedelta(weeks=1)
                        t2 = t2 + relativedelta(weeks=1)
                else:
                    if t1 and t1 > now:
                        t1 = t1 - relativedelta(weeks=1)
                        t2 = t2 - relativedelta(weeks=1)
        if isinstance(t1, datetime):
            t1 = t1.strftime(TIME_FORMAT)
        if isinstance(t2, datetime):
            t2 = t2.strftime(TIME_FORMAT)
        time_tuple = (t1, t2)
    except ValueError as _:
        pass
    return time_text, time_tuple


def get_text(time: Union[datetime, str, int]):
    now = datetime.now()
    if isinstance(time, str):
        time = datetime.strptime(time, TIME_FORMAT)
    elif isinstance(time, int):
        time = datetime.fromtimestamp(time)
    duration = now - time
    today_zero = now - relativedelta(hour=0, minute=0, second=0, microsecond=0)
    zero_duration = today_zero - time
    days_span_today_zero = ceil(zero_duration.days + zero_duration.seconds / SECONDS_ONE_DAY)
    reply = []
    if not duration.days:
        if duration.seconds < 60:
            return f"{duration.seconds}秒前"
        if duration.seconds < 600:
            return f"{int(duration.seconds / 60)}分钟前"
        if days_span_today_zero:
            reply.append(around_today(days_span_today_zero))
    else:
        if -2 <= days_span_today_zero <= 2:
            reply.append(around_today(days_span_today_zero))
        elif time.year != now.year:
            month_year = now.year - time.year
            if month_year:
                _m = {1: "去", -1: "明"}
                reply.append(f"{_m.get(month_year, time.year)}年")
            reply.append(f"{time.month}月")
            reply.append(f"{time.day}号")
        elif time.month != now.month:
            month_span = now.month - time.month
            if month_span:
                _m = {1: "上个", -1: "下个"}
                reply.append(f"{_m.get(month_span, time.month)}月")
            reply.append(f"{time.day}号")
        else:
            week_span = time.day - (now.day - now.weekday())
            if -7 <= week_span < 0:
                reply.append(f"上周{WEEK_DAY_DICT.get(week_span + 7 + 1)}")
            elif 7 <= week_span < 14:
                reply.append(f"下周{WEEK_DAY_DICT.get(week_span - 7 + 1)}")
            elif 0 <= week_span < 7:
                reply.append(f"本周{WEEK_DAY_DICT.get(week_span + 1)}")
            else:
                reply.append(f"{time.day}号")
    if 0 <= time.hour < 6:
        reply.append("凌晨")
    elif 6 <= time.hour < 8:
        reply.append("早上")
    elif 8 <= time.hour < 11:
        reply.append("上午")
    elif 11 <= time.hour < 13:
        reply.append("中午")
    elif 13 <= time.hour < 18:
        reply.append("下午")
    elif 18 <= time.hour:
        reply.append("晚上")
    reply.append(f"{time.hour}点")
    if time.minute > 0:
        reply.append(f"{time.minute}分".zfill(3))
    return "".join(reply)


SECONDS_ONE_DAY = 60 * 60 * 24
WEEK_DAY_DICT = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "日"}
WEEK_DAY_STRS = "一二三四五六日天末"
RE_WEEK = rf"(?<!这个)(?<!这|本)(?:周|星期)([\d{WEEK_DAY_STRS}])"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
