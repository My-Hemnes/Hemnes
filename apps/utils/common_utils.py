# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""Util functions."""
#
import base64, hashlib, json, os, re, \
    time, uuid, xmltodict, yaml

from datetime import datetime
from functools import reduce
from requests import Session
from apps.configs.constants import AppsConf


def read_yml(filename):
    """Read yaml file"""
    content = {}
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = yaml.full_load(f)
    return content


def jobpool_init(jobpool_conf):
    """初始化系统公共区"""
    dir_list = list()

    jobpool_conf["job_dir"] = jobpool_conf.get("job_dir", "/".join([AppsConf.HEMNES_HOME, "jobpool"]))
    dir_list.append(jobpool_conf["job_dir"])

    job_dir = jobpool_conf["job_dir"]
    jobpool_conf["cache_dir"] = "/".join([job_dir, jobpool_conf.get("cache_name", "Cache")])
    dir_list.append(jobpool_conf["cache_dir"])
    jobpool_conf["log_dir"] = "/".join([job_dir, jobpool_conf.get("log_name", "Log")])
    dir_list.append(jobpool_conf["log_dir"])
    jobpool_conf["worker_dir"] = "/".join([job_dir, jobpool_conf.get("worker_name", "Worker")])
    dir_list.append(jobpool_conf["worker_dir"])
    jobpool_conf["store_dir"] = "/".join([job_dir, jobpool_conf.get("store_name", "Store")])
    dir_list.append(jobpool_conf["store_dir"])

    # 创建不存在的公共工作区域
    for dir_path in dir_list:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)


# Time format protocol
TIME_ISO8601 = "%Y-%m-%dT%H:%M:%SZ"
TIME_ISO8601_MS = "%Y-%m-%dT%H:%M:%S.%fZ"

session = Session()


def get_file_md5_digest(filename, block=64 * 1024):
    """Calculate md5 hexdigest of content."""
    with open(filename, "rb") as r:
        md5 = hashlib.md5()
        while True:
            data = r.read(block)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()


def get_content_md5_digest(content):
    """Calculate md5 hexdigest of content."""
    md5 = hashlib.md5()
    try:
        md5.update(to_bytes(content))
    except Exception as e:
        raise e
    return md5.hexdigest()


def get_content_sha1_digest(content):
    """Calculate sha1 hexdigest of content."""
    sha1 = hashlib.sha1()
    sha1.update(to_bytes(content))
    return sha1.hexdigest()


def gen_uuid():
    """Generate uuid."""
    return uuid.uuid1().hex


def get_unixtime():
    """Get unixtime.

    :arg int unixtime: UNIX time
    :return unixtime
    """
    return int(time.time())


def get_utctime():
    """Get formatted time (UTC time).

    Note: Time Zone was 0
    :return UTC time
    """
    return time.strftime(TIME_ISO8601, time.gmtime())


def get_gmttime():
    """Get formatted time (GMT time).

    :return GMT time
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())


def get_gmttime_from_unixtime(unix_time=None):
    """Get formatted time (GMT time).

    :arg string unix_time: unix time
    :return GMT time
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime(float(unix_time or time.time())))


def get_unixtime_from_gmttime(gmt_time=None):
    """Get unixtime from GMT time.

    :arg string gmt_time: GMT time
    :return unixtime
    """
    formatd = time.gmtime() if gmt_time is None \
        else time.strptime(gmt_time, "%a, %d %b %Y %H:%M:%S GMT")
    return int(time.mktime(formatd))


def get_unixtime_from_strftime(formats, strtime):
    """Get unixtime from format time.

    :arg string formats: format string
    :arg string strtime: format time
    :return unixtime
    """
    return int(time.mktime(time.strptime(strtime, formats)))


def get_format_time(formats, unixtime=None, delay=None):
    """Get format time from unix time.

    :arg string formats: format string
    :arg integer unixtime: time stamp
    :arg integer delay: the seconds delay
    :return format time
    """
    timestamp = unixtime or time.time()
    if delay:
        timestamp += delay
    locatime = datetime.fromtimestamp(timestamp)
    return locatime.strftime(formats)


def to_str(bytes_or_str):
    """Encode bytes or str to str type."""
    return bytes_or_str.decode("utf-8") if isinstance(bytes_or_str, bytes) else bytes_or_str


def to_bytes(bytes_or_str):
    """Encode bytes or str to str type."""
    return bytes_or_str.encode("utf-8") if isinstance(bytes_or_str, str) else bytes_or_str


def base64_urlsafe_encode(digest):
    """Encode url string.

    :arg string digest: url content
    :return string url encoded
    """
    encode = base64.urlsafe_b64encode(to_bytes(digest)).strip()
    return to_str(encode)


def base64_urlsafe_decode(digest):
    """Decode url string.

    :arg string digest: url content
    :return string url decoded
    """
    decode = base64.urlsafe_b64decode(digest).strip()
    return to_str(decode)


def base64_encode(digest):
    """Encode string use base64.

    :arg string digest: encode content
    :return string encoded
    """
    encode = base64.b64encode(to_bytes(digest)).strip()
    return to_str(encode)


def base64_decode(digest):
    """Decode string use base64.

    :arg string digest: decode content
    :return string decoded
    """
    decode = base64.b64decode(digest).strip()
    return to_str(decode)


def base16_encode(digest):
    """Encode string use base64.

    :arg string digest: encode content
    :return string encoded
    """
    encode = base64.b16encode(to_bytes(digest)).strip()
    return to_str(encode)


def base16_decode(digest):
    """Decode string use base64.

    :arg string digest: decode content
    :return string decoded
    """
    decode = base64.b16decode(digest).strip()
    return to_str(decode)


def is_valid_base64_encode(digest):
    """Verify the base64 encode string."""
    pattern = re.compile(r"[A-Z]")
    if pattern.match(digest):
        return True
    return False


def is_contain_zh(string):
    """Verify the word is include ZH."""
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    if pattern.search(to_str(string)):
        return True
    return False


def safe_pathname(string):
    """Check and process the ZH directory and filename."""
    encode = to_str(string)
    return encode.replace(" ", "")


def sub_special(info, space=False):
    """Re Filter secial string"""
    # space-True; 过滤空格|space-False; 不过滤空格
    if space:
        return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", info)
    sub_info = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\u0020])", "", info)
    return sub_info


def xml_to_dict(xml_str):
    """transform xml to dict"""
    if not isinstance(xml_str, str):
        assert AssertionError("Argument type is not str")
    data_ordered_dict = xmltodict.parse(xml_str)
    data_json = json.dumps(data_ordered_dict, indent=4)
    data_dict = json.loads(data_json)
    return data_dict


def dict_to_xml(data_dict):
    """transform dict to xml"""
    if not isinstance(data_dict, dict):
        assert AssertionError("Argument type is not dict")
    return xmltodict.unparse(data_dict, pretty=True, encoding='utf-8')


def reduce_list_attr(name, list_data):
    """列表对象根据属性 name 去重"""
    lam_analy = lambda y, x: y if (x[name] in [i[name] for i in y]) \
        else (lambda z, u: (z.append(u), z))(y, x)[1]
    return reduce(lam_analy, list_data, [])
