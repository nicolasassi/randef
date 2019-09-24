# -*- coding: utf-8 -*-

from refgen import RefGen

class Titles(RefGen):

    def __init__(self):
        super(Titles, self).__init__()

    def pick_title(self):
        return self._pick_title_categories()

    @staticmethod
    def format_title(title):
        if title.endswith('.'):
            return title[:-1]
        else:
            return title


    def pick_title_for_no_author(self):
        title = self._pick_title_categories()[0]
        title_parts = title.split(' ')
        if len(title_parts) > 1:
            if title_parts[0].lower() in ['o', 'a', 'os', 'as', 'der', 'die', 'le',
            'les', 'el', 'la', 'los', 'las']:
                start_title = ' '.join(title_parts[:2]).upper()
                return '{} {}'.format(start_title, ' '.join(title_parts[2:]))
            else:
                return '{} {}'.format(title_parts[0].upper(), ' '.join(title_parts[1:]))
        return title.upper()

    @staticmethod
    def get_categories_list(categories):
        return categories.split(';')
