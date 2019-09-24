from refgen import RefGen
import random


class Authors(RefGen):

    possessives = ['de', 'da', 'do', 'dos', 'das']
    part_type = ['Ed', 'Coord', 'Ilust', 'Part', 'Desenv', 'Dir', 'Org', 'Comp']

    def __init__(self):
        super(Authors, self).__init__()

    @staticmethod
    def _add_casual_char(words_list, char, how_casual_rate=5):
        '''
            words_list: the list of words to add the casual char in
            char: the char to casually add
            how_casual_rate: the probability of 1-100 of this chart to appear
        '''
        if random.randint(1, 100) <= how_casual_rate:
            if len(words_list)-1 <= 1:
                where = 1
            else:
                where = random.randint(1, len(words_list)-1)
            words_list.insert(where, char)
            composed = ''.join(words_list[where-1:where+2])
            try:
                for _ in range(3):
                    words_list.remove(words_list[where-1])
                words_list.append(composed)
                return words_list
            except:
                return words_list
        return words_list

    def _add_casual_possessive(self, words_list, how_casual_rate=20):
        '''
            words_list: the list of words to add the casual char in
            how_casual_rate: the probability of 1-100 of this chart to appear
        '''
        if random.randint(1, 100) <= how_casual_rate:
            char = random.choice(self.possessives)
            where = random.randint(1, len(words_list))
            words_list.insert(where, char)
            return words_list
        return words_list

    def _add_casual_utf8_char(self, words_list, how_casual_rate=15):
        new_word_list = list()
        for word in words_list:
            if not word:
                continue
            if random.randint(1, 100) <= how_casual_rate:
                where = random.randint(0, len(word)-1)
                words = word.split(word[where])
                word = words[0]+random.choice(self.utf8_chars)+words[1]
                new_word_list.append(word)
            else:
                new_word_list.append(word)
        return new_word_list

    def _format_initials(self, names):
        names_initials = list()
        for name in names:
            if name == names[0]:
                if random.randint(0, 1) == 0:
                    names_initials.append(name[0]+'.')
                else:
                    names_initials.append(name)
                continue
            if name == names[-1] and not name in self.possessives:
                if random.randint(1, 10) in range(9, 11):
                    names_initials.append(name)
                else:
                    names_initials.append(name[0]+'.')
                continue
            if random.randint(1, 10) in range(1, 9) and name not in self.possessives:
                names_initials.append(name[0]+'.')
            else:
                names_initials.append(name)
        return names_initials

    def _add_location(self, public_admin_orgs):
        if random.randint(0, 1) == 0:
            country = self._pick_country()
            if random.randint(0, 1) == 0:
                public_admin_orgs.insert(0, country.upper())
            else:
                public_admin_orgs[0] = public_admin_orgs[0].upper()
                public_admin_orgs.insert(1, '({})'.format(country.title()))
                new = ' '.join(public_admin_orgs[:2])
                public_admin_orgs = public_admin_orgs[2:]
                public_admin_orgs.insert(0, new)
        else:
            city = self._pick_city()
            if random.randint(0, 1) == 0:
                if random.randint(0, 1) == 0:
                    public_admin_orgs.insert(
                        0, '{} (Estado)'.format(city.upper()))
                    new = ' '.join(public_admin_orgs[:2])
                    public_admin_orgs = public_admin_orgs[2:]
                    public_admin_orgs.insert(0, new)
                else:
                    public_admin_orgs.insert(
                        0, '{} (Cidade)'.format(city.upper()))
                    new = ' '.join(public_admin_orgs[:2])
                    new = ' '.join(public_admin_orgs[:2])
                    public_admin_orgs = public_admin_orgs[2:]
                    public_admin_orgs.insert(0, new)
            else:
                public_admin_orgs[0] = public_admin_orgs[0].upper()
                public_admin_orgs.insert(1, '({})'.format(city.title()))
                new = ' '.join(public_admin_orgs[:2])
                public_admin_orgs = public_admin_orgs[2:]
                public_admin_orgs.insert(0, new)
        return public_admin_orgs

    def get_surnames(self, n):
        return [self._pick_surname() for _ in range(n)]

    def format_surnames(self, surnames, add_casual_dash=True, add_casual_quote=True):
        surnames = self._add_casual_utf8_char(surnames)
        if len(surnames) > 1:
            if add_casual_dash:
                surnames = self._add_casual_char(surnames, '-', 5)
            elif add_casual_quote:
                surnames = self._add_casual_char(surnames, "'", 5)
        else:
            if random.randint(1, 100) <= 12:
                surnames.insert(0, random.choice(['A', 'E', 'I', 'O', 'U']))
                surnames = self._add_casual_char(surnames, "'", 100)
        return [surname.upper() for surname in surnames if surname]


    def get_research_orgs(self, n):
        return [self._pick_research_org() for _ in range(n)]

    def format_research_orgs(self, research_orgs):
        research_orgs.insert(0, research_orgs[0].upper())
        research_orgs.pop(1)
        return research_orgs
        # return [research_org for research_org in research_orgs]

    def get_names(self, n):
        return [self._pick_name().title() for _ in range(n)]

    def format_names(self, names, add_casual_possessive=True, add_casual_dash=True, add_casual_quote=True, return_initials=True):
        names = self._add_casual_utf8_char(names, how_casual_rate=15)
        if len(names) > 1:
            if add_casual_possessive:
                names = self._add_casual_possessive(names)
            if add_casual_quote:
                names = self._add_casual_char(names, "'", 3)
            if add_casual_dash:
                names = self._add_casual_char(names, "-", 3)
            if return_initials:
                names = self._format_initials(names)
        else:
            if random.randint(1, 100) <= 12:
                names.insert(0, random.choice(['A', 'E', 'I', 'O', 'U', ]))
                names = self._add_casual_char(names, "'", 100)
        return [name for name in names]

    def get_public_admin_orgs(self, n):
        return [self._pick_research_org() for _ in range(n)]

    def format_public_admin(self, public_admin_orgs):
        public_admin_orgs = self._add_location(public_admin_orgs)
        return public_admin_orgs

    def _build_authors_name(self):
        pass

    @staticmethod
    def get_cited_author(n):
        lines = list()
        for _ in range(n):
            lines.append('_')
        return [''.join(lines)]

    def _make_paticipation_tag(self, title=True):
        if title:
            return '({}.)'.format(random.choice(self.part_type))
        else:
            return '({}.)'.format(random.choice(self.part_type).lower())

# a = Authors()
# for _ in range(50):
#     # surnames = a._get_surnames(1)
#     # print(a._format_surnames(surnames))
#     # names = a.get_names(4)
#     # print(a.format_names(names))
#     # research_orgs = a.get_research_orgs(1)
#     # print(a.format_research_orgs(research_orgs))
#     # public_orgs = a.get_public_admin_orgs(1)
#     # print(a.format_public_admin(public_orgs))
