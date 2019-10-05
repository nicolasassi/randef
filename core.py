# -*- coding: utf-8 -*-

from authors import Authors
from titles import Titles
import re
import json
import random
from refgen import RefGen

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
                        if random.randint(1, 100) in range(20):
                            yield ('{} {}.'.format('; '.join(authors_list), title), refs)
                        else:
                            yield ('{}. {}.'.format('; '.join(authors_list), title), refs)
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
                if random.randint(1, 100) in range(20):
                    yield ('{} {}.'.format(author_done, title), [{'author': author_done},
                    {'title': title}])
                else:
                    yield ('{}. {}.'.format(author_done, title), [{'author': author_done},
                    {'title': title}])
            else:
                yield ('{}. {}.'.format(author_done, title), [{'author': author_done},
                {'title': title}])

def with_participation_tag(author_class, title_class, iters=1, max_authors=7, max_names=5, max_surnames=4):
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
                        if random.randint(1, 100) in range(20):
                            yield ('{} {}.'.format('; '.join(authors_list), title), refs)
                        else:
                            yield ('{}. {}.'.format('; '.join(authors_list), title), refs)
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
    for ref in with_participation_tag(authors, titles, iters=each_poss):
        yield ref


def standard(refgen):
    ref_ref = list()
    edition = refgen.make_edition(random.choice(refgen.edition_types))
    ref_ref.append({'edition': edition})
    if random.randint(1, 100) in range(90):
        city = refgen.make_city()
    else:
        city = refgen.make_city(loco=False)
    ref_ref.append({'city':city})
    if random.randint(1, 100) in range(90):
        editor = refgen.get_editor()
    else:
        editor = refgen.get_editor(nomine=False)
    ref_ref.append({'editor':editor})
    if random.randint(1, 100) in range(90):
        year = refgen.make_year('regular')
    else:
        year = refgen.make_year(random.choice(refgen.year_types[1:]))
    ref_ref.append({'year': year})
    return '{}. {}: {}, {}.'.format(edition, city, editor, year), ref_ref

def standard_plus_vol_cap_num_pag(refgen):
    ref = ''
    ref_ref = list()
    if random.randint(1, 100) in range(10):
        vol = refgen.make_vol()
        ref_ref.append({'vol': vol})
        ref += ' {}.'.format(vol)
    if random.randint(1, 100) in range(10):
        cap = refgen.make_cap()
        ref_ref.append({'cap': cap})
        ref += ' {}.'.format(cap)
    if random.randint(1, 100) in range(10):
        num = refgen.make_num()
        ref_ref.append({'num': num})
        ref += ' {}.'.format(num)
    if random.randint(1, 100) in range(30):
        if random.randint(1, 100) in range(50):
            page = refgen.make_pag()
            ref_ref.append({'page': page})
            ref += ' {}.'.format(page)
        else:
            pages = refgen.make_pags()
            ref_ref.append({'pages': pages})
            ref += ' {}.'.format(pages)
    return ref, ref_ref

def academic(refgen):
    ref_ref = list()
    adv = refgen.add_advisor()
    ref_ref.append({'advisor': adv})
    if random.randint(1, 100) in range(90):
        year = refgen.make_year('regular')
    else:
        year = refgen.make_year(random.choice(refgen.year_types[1:]))
    ref_ref.append({'year': year})
    f = refgen.make_folhas()
    ref_ref.append({'folhas': f})
    ac_type = refgen.make_academic_type()
    grad_in = refgen.make_graduation_in()
    author = Authors()
    where = author.get_research_orgs(1)[0]
    ref_ref.append({'what_where':'{} {} - {}'.format(ac_type, grad_in, where)})
    if random.randint(1, 100) in range(90):
        city = refgen.make_city()
    else:
        city = refgen.make_city(loco=False)
    ref_ref.append({'city': city})
    if random.randint(1, 100) in range(90):
        year2 = refgen.make_year('regular')
    else:
        year2 = refgen.make_year(random.choice(refgen.year_types[1:]))
    ref_ref.append({'year': year})
    return ' {}. {}. {}. {} {} - {}, {}, {}.'.format(adv, year, f, ac_type, grad_in, where, city, year2), ref_ref

def finish(refgen):
    things = ''
    ref_ref = list()
    things_that_could_go = [
        {'link': refgen.make_e_reference}, {'doi': refgen.make_doi}, {'notes':refgen.make_complementary_notes}]
    how_many = random.randint(1, 3)
    choices = random.sample(things_that_could_go, how_many)
    for choice in choices:
        k = list(choice.keys())[0]
        if k == 'link':
            if random.randint(1, 2) == 1:
                value = list(choice.values())[0]('updated')
            else:
                value = list(choice.values())[0]('deprecated')
        else:
            value = list(choice.values())[0]()
        ref_ref.append({k: value})
        things += ' {}.'.format(value)
    return things, ref_ref

def clean(text):
    found = re.findall(r'[\\\(\)\.\-\^\'\"\*\+\[\]\$\?\<\>\=\{\}\_]', text)
    for f in set(found):
        text = text.replace(f, r'\{}'.format(f))
        # text = re.sub(f, '\{}'.format(f), text)
    return text

punct = re.compile(r"[\!\\\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\]\¨\^\_\x60\{\|\}\~]")

def is_punct(token):
    if punct.match(token):
        return True
    return False

def find_last_punct(match, start):
    last_token = 0
    for i, m in enumerate(match):
        if i == start:
            return last_token
        if is_punct(m):
            last_token = i
    return last_token

def find_next_punct(match, end):
    next_token = len(match)
    for i, m in enumerate(match):
        if i < end:
            continue
        if is_punct(m):
            return i
    return next_token

def re_func(ref, match):
    try:
        f = re.search('{}'.format(clean(match.lower())), ref.lower())
        return find_last_punct(ref, f.start()), find_next_punct(ref, f.end())
    except:
        raise ValueError

import datetime
now = datetime.datetime.now()
refgen = RefGen()
with open('noice.jsonl', 'w+', encoding='utf-8') as f:
    for text, ref in make_author_title(1000):
        if random.randint(1, 100) in range(90):
            ap, ref_ref = standard(refgen)
            text += ' {}'.format(ap)
            ref.extend(ref_ref)
            if random.randint(1, 2) == 1:
                ap, ref_ref = standard_plus_vol_cap_num_pag(refgen)
                text += '{}'.format(ap)
                ref.extend(ref_ref)
        else:
            ap, ref_ref = academic(refgen)
            text += ' {}'.format(ap)
            ref.extend(ref_ref)
        if random.randint(1, 100) in range(20):
            ap, ref_ref = finish(refgen)
            text += '{}'.format(ap)
            ref.extend(ref_ref)
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