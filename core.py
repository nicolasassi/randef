from authors import Authors
from titles import Titles
import re
import json
import random
from os import listdir

def regular(author_class, title_class, iters=1, max_authors=7, max_names=5, max_surnames=4):
    for _ in range(iters):
        for authors in range(1, max_authors):
            for names in range(1, max_names):
                for surnames in range(1, max_surnames):
                    authors_list = list()
                    refs = list()
                    for _ in range(authors):
                        author_done = '{}, {}'.format(' '.join(author_class.format_surnames(author_class.get_surnames(surnames))),
                        ' '.join(author_class.format_names(author_class.get_names(names))))
                        refs.append({'author': author_done})
                        authors_list.append(author_done)
                    title = title_class.format_title(title_class.pick_title())
                    refs.append({'title': title})
                    authors_list_str = '; '.join(authors_list)
                    if authors_list_str.endswith("."):
                        yield ('{} {}.'.format('; '.join(authors_list), title), refs)
                    else:
                        yield ('{}. {}.'.format('; '.join(authors_list), title), refs)

def et_al(author_class, title_class, iters=1, max_names=5, max_surnames=4):
    for _ in range(iters):
            for names in range(1, max_names):
                    for surnames in range(1, max_surnames):
                        refs = list()
                        author_done = '{}, {} et al'.format(' '.join(author_class.format_surnames(author_class.get_surnames(surnames))),
                        ' '.join(author_class.format_names(author_class.get_names(names))))
                        refs.append({'author': author_done})
                        title = title_class.format_title(title_class.pick_title())
                        refs.append({'title': title})
                        yield ('{}. {}.'.format(author_done, title), refs)

def title_only(title_class, iters=1):
    for _ in range(iters):
            title = title_class.format_title(title_class.pick_title_for_no_author())
            yield ('{}.'.format(title), [{'title': title}])

def previously_cited_author(author_class, title_class, iters=1, max_punct=12):
    for _ in range(iters):
        for puncts in range(6, max_punct):
            author_done =  ''.join(author_class.get_cited_author(puncts))
            title = title_class.format_title(title_class.pick_title())
            yield ('{}. {}.'.format(author_done, title), [{'author': author_done},
            {'title': title}])

def research_org_as_author(author_class, title_class, iters=1, max_research_orgs=4):
    for _ in range(iters):
        for reseach_orgs in range(1, max_research_orgs):
            research_org = author_class.format_research_orgs(
                author_class.get_research_orgs(reseach_orgs))
            author_done = '. '.join(research_org)
            title = title_class.format_title(title_class.pick_title())
            if author_done.endswith("."):
                yield ('{} {}.'.format(author_done, title), [{'author': author_done},
                {'title': title}])
            else:
                yield ('{}. {}.'.format(author_done, title), [{'author': author_done},
                {'title': title}])

def state_owned_research_orgs(author_class, title_class, iters=1, max_research_orgs=4):
    for _ in range(iters):
        for reseach_orgs_length in range(1, max_research_orgs):
            research_org = author_class.format_public_admin(
                author_class.get_public_admin_orgs(reseach_orgs_length))
            author_done = '. '.join(research_org)
            title = title_class.format_title(title_class.pick_title())
            if author_done.endswith("."):
                yield ('{} {}.'.format(author_done, title), [{'author': author_done},
                {'title': title}])
            else:
                yield ('{}. {}.'.format(author_done, title), [{'author': author_done},
                {'title': title}])

def with_partcipation_tag(author_class, title_class, iters=1, max_authors=7, max_names=5, max_surnames=4):
    for _ in range(iters):
        for authors in range(1, max_authors):
            for names in range(1, max_names):
                for surnames in range(1, max_surnames):
                    authors_list = list()
                    refs = list()
                    if random.randint(0, 1) == 0:
                        updated = True
                    else:
                        updated = False
                    for _ in range(authors):
                        if random.randint(1, 100) in range(33):
                            author_done = '{}, {} {}'.format(' '.join(author_class.format_surnames(author_class.get_surnames(surnames))),
                            ' '.join(author_class.format_names(author_class.get_names(names))), author_class._make_paticipation_tag(updated))
                        else:
                            author_done = '{}, {}'.format(' '.join(author_class.format_surnames(author_class.get_surnames(surnames))),
                        ' '.join(author_class.format_names(author_class.get_names(names))))
                        refs.append({'author': author_done})
                        authors_list.append(author_done)
                    title = title_class.format_title(title_class.pick_title())
                    refs.append({'title': title})
                    authors_list_str = '; '.join(authors_list)
                    if authors_list_str.endswith("."):
                        yield ('{} {}.'.format('; '.join(authors_list), title), refs)
                    else:
                        yield ('{}. {}.'.format('; '.join(authors_list), title), refs)

def make_author_title(each_poss=1):
    authors = Authors()
    titles = Titles()
    for ref in regular(authors, titles, iters=each_poss):
        yield ref
    for ref in et_al(authors, titles, iters=each_poss):
        yield ref
    for ref in title_only(titles, iters=each_poss):
        yield ref
    for ref in previously_cited_author(authors, titles, iters=each_poss):
        yield ref
    for ref in research_org_as_author(authors, titles, iters=each_poss):
        yield ref
    for ref in state_owned_research_orgs(authors, titles, iters=each_poss):
        yield ref
    for ref in with_partcipation_tag(authors, titles, iters=each_poss):
        yield ref


def clean(text):
    found = re.findall(r'[\\\(\)\.\-\^\'\"\*\+\[\]\$\?\<\>\=\{\}\_]', text)
    for f in set(found):
        text = text.replace(f, r'\{}'.format(f))
        # text = re.sub(f, '\{}'.format(f), text)
    return text

def re_func(ref, match):
    f = re.search('{}'.format(clean(match.lower())), ref.lower())
    try:
        return f.start(), f.end()
    except:
        raise ValueError


import datetime
now = datetime.datetime.now()
with open('noice8.jsonl', 'a+', encoding='utf-8') as f:
    for text, ref in make_author_title(10000):
        ents = {'entities': []}
        ents['text'] = text
        try:
            for vs in ref:
                for k, v in vs.items():
                    start, end = re_func(text, v)
                    ents['entities'].append((start, end, k.upper()))
        except ValueError:
            continue
        f.write(json.dumps(ents, ensure_ascii=False)+'\n')
print(datetime.datetime.now()-now)

# files = listdir('done')
# with open('super_noicet.jsonl', 'w+', encoding='utf-8') as f:
#     for file in files:
#         with open('done/{}'.format(file), 'r', encoding='utf-8', newline='') as fr:
#             for line in fr.readlines():
#                 f.write(line)