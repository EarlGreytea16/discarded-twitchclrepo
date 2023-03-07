import datetime
import hashlib
import random
import sys
import os
import urllib.request
from threading import Thread
import requests
from bs4 import BeautifulSoup


# read file lines into a list then remove empty lines
def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '']
    return lines


# get this script's path's parent path
def parent_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# check link is twitchtracker or streamscharts
def link_checker(link):
    global streamername
    global vodID
    link = link.split('/')
    if link[2] == 'twitchtracker.com':
        streamername = link[3]
        vodID = link[5]
        return 1
    elif link[2] == 'streamscharts.com':
        streamername = link[4]
        vodID = link[6]
        return 2
    elif link[0] == 'twitchtracker.com':
        streamername = link[1]
        vodID = link[3]
        return 3
    elif link[0] == 'streamscharts.com':
        streamername = link[2]
        vodID = link[4]
        return 4
    else:
        print(
            'Check the link again. (An unsupported link has been entered '
            'or the link has an error.)')
        return 0


def linktimecheck_streamscharts(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    gelenveri = soup.find_all('time', 'ml-2 font-bold')

    try:
        time = gelenveri[0].text
    except Exception as e:
        print(f"{type(e).__name__} was raised: {e}", file=sys.stderr)
        return None

    if '\n' in time:
        time = time.replace('\n', '')
    if ',' in time:
        time = time.replace(',', '')

    print(f'Clock data: {time}', file=sys.stderr)
    print(f'Streamer name: {streamername} \nvodID: {vodID}', file=sys.stderr)

    time = time.split(' ')
    hoursandminut = time[3]
    hoursandminut = hoursandminut.split(':')
    day = int(time[0])
    month = time[1]
    year = int(time[2])
    hour = int(hoursandminut[0])
    minute = int(hoursandminut[1])

    def months(month):
        if month == 'Jan':
            return 1
        if month == 'Feb':
            return 2
        if month == 'Mar':
            return 3
        if month == 'Apr':
            return 4
        if month == 'May':
            return 5
        if month == 'Jun':
            return 6
        if month == 'Jul':
            return 7
        if month == 'Aug':
            return 8
        if month == 'Sep':
            return 9
        if month == 'Oct':
            return 10
        if month == 'Nov':
            return 11
        if month == 'Dec':
            return 12
        else:
            return 0

    month = months(month)
    second = 60

    timestamp = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(hour) + '-' + str(
        minute) + '-' + str(
        second)

    print(f'timestamp', timestamp, file=sys.stderr)
    return timestamp


def linktimecheck_twitchtracker(link):
    useragent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.5; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (X11; Linux i686; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.5; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.77",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 Edg/103.0.1264.77",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36']

    header = {
        'user-agent': f'{random.choice(useragent)}'
    }

    r = requests.get(link, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    gelenveri = soup.find_all('div', 'stream-timestamp-dt')

    try:
        time = gelenveri[0].text
    except Exception as e:
        print(f"{type(e).__name__} was raised: {e}")
        return None

    print(f'Clock data: {time}', file=sys.stderr)
    print(f'Streamer name: {streamername} \nvodID: {vodID}', file=sys.stderr)

    firstandsecond_time = gelenveri[0].text.split(' ')
    first_time = firstandsecond_time[0].split('-')
    second_time = firstandsecond_time[1].split(':')

    day = int(first_time[2])
    month = int(first_time[1])
    year = int(first_time[0])
    hour = int(second_time[0])
    minute = int(second_time[1])
    second = int(second_time[2])

    timestamp = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(hour) + '-' + str(
        minute) + '-' + str(
        second)

    print(f'timestamp', timestamp, file=sys.stderr)
    return timestamp


def totimestamp(dt, epoch=datetime.datetime(1970, 1, 1)):
    td = dt - epoch
    return (td.microseconds + (td.seconds + td.days * 86400) * 10 ** 6) / 10 ** 6


def find(timestamp, domain):
    timestamp = timestamp.split('-')
    year = int(timestamp[0])
    month = int(timestamp[1])
    day = int(timestamp[2])
    hour = int(timestamp[3])
    minute = int(timestamp[4])
    second = int(timestamp[5])

    def check(url):
        global find1cu
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            pass
        else:
            find1cu = url

    threads = []
    if second == 60:
        for i in range(60):
            seconds = i
            td = datetime.datetime(year, month, day, hour, minute, seconds)
            converted_timestamp = totimestamp(td)
            formattedstring = streamername + "_" + vodID + "_" + str(int(converted_timestamp))
            hash = str(hashlib.sha1(formattedstring.encode('utf-8')).hexdigest())
            requiredhash = hash[:20]
            finalformattedstring = requiredhash + '_' + formattedstring
            url = f"{domain}/{finalformattedstring}/chunked/index-dvr.m3u8"
            threads.append(Thread(target=check, args=(url,)))
        for i in threads:
            i.start()
        for i in threads:
            i.join()
    else:
        td = datetime.datetime(year, month, day, hour, minute, second)
        converted_timestamp = totimestamp(td)
        formattedstring = streamername + "_" + vodID + "_" + str(int(converted_timestamp))
        hash = str(hashlib.sha1(formattedstring.encode('utf-8')).hexdigest())
        requiredhash = hash[:20]
        finalformattedstring = requiredhash + '_' + formattedstring
        url = f"{domain}/{finalformattedstring}/chunked/index-dvr.m3u8"
        threads.append(Thread(target=check, args=(url,)))
        for i in threads:
            i.start()
        for i in threads:
            i.join()


domains = read_file_lines(parent_path() + '\\' + 'domains.txt')

print('Find the broadcast link you want from Twitchtracker or Streamscharts site.', file=sys.stderr)
inputlink = sys.argv[1]

linkCheck = link_checker(inputlink)

if linkCheck == 2 or linkCheck == 4:  # streamscharts
    print('Input Link is Streamscharts Link. \n'
          'Date and Time are checking..', file=sys.stderr)
    timestamp = linktimecheck_streamscharts(inputlink)
elif linkCheck == 1 or linkCheck == 3:  # twitchtracker
    print('Input Link is Twitchtracker Link. \n'
          'Date and Time are checking..', file=sys.stderr)
    timestamp = linktimecheck_twitchtracker(inputlink)
else:
    print('You entered an unsupported link or '
          'An unknown error has occurred.', file=sys.stderr)
    sys.exit(1)

if timestamp is None:
    print(
        'You probably got into cloudflare for bots.(could not find time data) '
        'There is nothing I can do for this error for now. \n'
        'Please fork if you can bypass this cloudflare. \n'
        'You will not get an error when you try again after a while. \n'
        'So try again after a while.', file=sys.stderr)
    sys.exit(1)

find1cu = 0

for domain in domains:
    if find1cu == 0:
        find(timestamp, domain)
    else:
        break

if find1cu == 0:
    print('No File Found on Twitch Servers.')
else:
    print(find1cu)
