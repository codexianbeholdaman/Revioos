import matplotlib.pyplot as plt
import _all_revioos

revs_per_title = {}
for x in _all_revioos.all_revioos:
    title = x['TITLE']
    neue_x = {**x}
    del neue_x['TITLE']

    if title in revs_per_title:
        revs_per_title[title].append(neue_x)
    else:
        revs_per_title[title] = [neue_x]

titles = revs_per_title.keys()
sizes = [len(revs_per_title[title]) for title in titles]
ratings = [sum([x['RATING'] for x in revs_per_title[title]])/len(revs_per_title[title]) for title in titles]

fig, ax = plt.subplots(1, 1, figsize = (18, 18))
ax.scatter(ratings, sizes)
_ = [ax.annotate(title, (x, y)) for title, x, y in zip(titles, ratings, sizes)]
ax.set_xlim([0, 10])

ax.set_title("RPG ratings")
ax.set_ylabel("Amount of ratings")
ax.set_xlabel("Average rating")
plt.savefig('rpgs.png', bbox_inches='tight')
