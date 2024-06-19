import parsers
import all_pages
import bs4

delimiter = '====='

all_posts = bs4.BeautifulSoup(all_pages.all_pages[0]).find_all("div", class_="message-content js-messageContent")
all_revioos = []
for post in all_posts:
    post_content = post.get_text()
    if post_content.count(delimiter)%2 == 1 or post_content.count(delimiter) == 0:
        continue
    
    for counter in range(post_content.count(delimiter)//2):
        low = post_content.find(delimiter)
        up = post_content[low+1:].find(delimiter)
        full_revioo = post_content[low:low+up+5]

        try:
            parsed_entry = parsers.post_processing(full_revioo)
            all_revioos.append(parsed_entry[0])
        finally:
            post_content = post_content[up:]

with open('_all_revioos.py', 'w') as revioos_file:
    revioos_file.write(f'{all_revioos = }')
