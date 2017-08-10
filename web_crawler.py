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


def get_page(url): #得到一个url的全部字符串
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


# seed = get_all_links(get_page('http://www.baidu.com'))

def crawl_web_1(seed, max_page):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        # depth-first-search :意味着我们将首先处理最后一条链接
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_page:
            crawled.append(page)
            union(tocrawl, get_all_links(get_page(page)))
            # tocrawl = tocrawl + get_all_links(get_page(page))
    return crawled


def crawl_web_2(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and depth <= max_depth:
            crawled.append(page)
            union(next_depth, get_all_links(get_page(page)))
        if not tocrawl: # 直到tocrawl为空, 即这一层已经全部纳入crawled
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            union(tocrawl, get_all_links(get_page(page)))
            # tocrawl = tocrawl + get_all_links(get_page(page))
    return crawled

print get_all_links(get_page("http://www.baidu.com"))
print crawl_web_1("http://www.baidu.com", 2)
print crawl_web_2("http://www.baidu.com", 1) # 由于depth = 1的每一个页面都要crawl next_depth, 所耗时间过长
# print crawl_web_1("http://www.baidu.com", 2)




















