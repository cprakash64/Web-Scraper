from datetime import datetime
import instaloader

# insta loader downloads some posts with hashtag funny

L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, "funny").get_posts()

SINCE = datetime(2021, 7, 20)  # further from today, inclusive
UNTIL = datetime(2021, 7, 21)  # closer to today, not inclusive

k = 0  # initiate k
# k_list = []  # uncomment this to tune k

for post in posts:
    postdate = post.date

    if postdate > UNTIL:
        continue
    elif postdate <= SINCE:
        k += 1
        if k == 50:
            break
        else:
            continue
    else:
        L.download_post(post, "funny")
        # if you want to tune k, uncomment below to get your k max
        # k_list.append(k)
        k = 0  # set k to 0