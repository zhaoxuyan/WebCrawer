# coding=utf-8
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url, end_quote = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_quote:]
        else:
            break
    return links


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)
    return a


seed = get_all_links(get_page('http://www.baidu.com'))


def crawl_web(seed):
    tocrawl = seed
    crawled = []
    while tocrawl:
        # depth-first-search :意味着我们将首先处理最后一条链接
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            union(tocrawl, get_all_links(get_page(page)))
            # tocrawl = tocrawl + get_all_links(get_page(page))
    return crawled

print crawl_web(seed)




















