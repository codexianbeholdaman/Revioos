import parsers
import _all_pages
import bs4

delimiter = '====='

page = bs4.BeautifulSoup(_all_pages.all_pages[0])
all_posts = page.find_all("div", class_="message-content js-messageContent")
all_users = page.find_all("article", class_="message message--post js-post js-inlineModContainer")

all_revioos = []
for post, author_plus in zip(all_posts, all_users):
    author = author_plus['data-author']
    post_content = post.get_text()
    if post_content.count(delimiter)%2 == 1 or post_content.count(delimiter) == 0:
        continue
    
    for counter in range(post_content.count(delimiter)//2):
        low = post_content.find(delimiter)
        up = post_content[low+1:].find(delimiter)
        full_revioo = post_content[low:low+up+5]

        try:
            parsed_entry = parsers.post_processing(full_revioo)
            all_revioos.append({**parsed_entry[0], 'AUTHOR':author})
        finally:
            post_content = post_content[up:]

with open('_all_revioos.py', 'w') as revioos_file:
    revioos_file.write(f'{all_revioos = }')
