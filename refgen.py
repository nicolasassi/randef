from sources import Sources
import random
import string


class RefGen(Sources):

    months = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'maio', 6: 'jun', 7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
    year_types = ['regular', 'uncertain', 'right_decade', 'prob_year', 'aprox_decade', 'circa_decade', 'between_decades']
    source_types = ['periodic', 'journal', 'magazine']
    help_types = ['tradução', 'prefácio', 'notas', 'atualização', 'atualizações' 'ilustação',
    'ilustrações', 'revisão', 'revisões', 'edição', 'edições', 'direção', 'coeditor', 'coedição', 'coord.', 'assist.', 'coordenação', 'assistência']
    work_types = ['Dissertação', 'Tese', 'Trabalho de conclusão de courso', 'TCC', 'Projeto de pesquisa']
    br_grad_types = ['Mestrado', 'Doutorado', 'Graduação', 'Pós-graduação', 'Tecnólogo', 'Licenciatura', 'Bacharelado', 'Especialização', 'PhD']
    event_type = ['anais', 'atas', 'resultados', 'proceedings']

    def __init__(self):
        super(RefGen, self).__init__()

    @staticmethod
    def make_edition(type):
        if type == 'regular':
            ed = random.randint(1, 30)
            return '{}. ed'.format(ed)
        else:
            ed = random.randint(1, 30)
            return '{}th. ed'.format(ed)

    @staticmethod
    def make_year(type):
        year = random.randint(1600, 2030)
        if type == 'regular':
            return str(year)
        if type == 'uncertain':
            return '[{}]'.format(str(year))
        if type == 'right_decade':
            return '[{}-]'.format(str(year)[:4])
        if type == 'prob_year':
            return '[{}?]'.format(str(year))
        if type == 'prob_decade':
            return '[{}-?]'.format(str(year)[:4])
        if type == 'aprox_decade':
            return '[da. {}]'.format(str(year))
        if type == 'circa_decade':
            return '[ca. {}]'.format(str(year))
        if type == 'between_decades':
            increment = random.randint(1, 10)
            return '[{} ou {}]'.format(str(year), str(year+increment))

    def make_city(self, loco=True, add_casual_state=True, add_casual_complement=True):
        if loco:
            city = self._pick_city()
            if add_casual_state:
                if random.randint(1, 100) <= 2:
                    state = [random.choice(string.ascii_letters).upper() for _ in range(2)]
                    return '{}, {}'.format(city.title(), ''.join(state))
            if add_casual_complement:
                if random.randint(1, 100) <= 2:
                    complement = self._pick_city()
                    return '{} ({})'.format(city, complement)
            return '{}, '.format(city.title())
        else:
            return '[S.l.]'

    @staticmethod
    def make_pag():
        pag = random.randint(1, 1000)
        return '{} p'.format(pag)

    @staticmethod
    def make_pags():
        pags = [random.randint(1, 2000) for _ in range(2)]
        return 'p. {} '.format('-'.join(pags))

    @staticmethod
    def make_folhas():
        f = random.randint(30, 300)
        return 'f. {}'.format(f)

    @staticmethod
    def make_vol():
        vol = random.randint(1, 30)
        return 'v. {}'.format(vol)

    @staticmethod
    def make_cap():
        vol = random.randint(1, 50)
        return 'cap. {}'.format(vol)

    @staticmethod
    def make_num():
        n = random.randint(1, 50)
        return 'n. {}'.format(n)

    @staticmethod
    def _get_second_month(month):
        second_month = month+random.randint(1, 4)
        if second_month < 12:
            return second_month
        else:
            return int(str(second_month)[-1])

    def make_date(self, type):
        year = random.randint(1600, 2030)
        month = random.randint(1, 12)
        if type == 'periodic':
            second_month = self._get_second_month(month)
            return '{}./{}. {}'.format(self.months[month], self.months[second_month], year)
        if type == 'journal':
            day = random.randint(1, 31)
            return '{} {}. {}'.format(day, self.months[month], year)
        if type == 'magazine':
            return '{}. {}'.format(self.months[month], year)

    def get_editor(self, nomine=True):
        if nomine:
            return self._pick_editor()
        else:
            return '[s.n.]'

    def make_complementary_help(self, amount):
        author = '{} {}'.format(self._pick_name().title(),
                                self._pick_surname().title())
        start = random.choice(self.help_types).title()
        if amount == 1:
            return '{}: {}'.format(start, author)
        if amount == 2:
            choice = random.choice(self.help_types)
            return '{} e {} de {}'.format(start, choice, author)
        if amount == 3:
            choice1 = random.choice(self.help_types)
            choice2 = random.choice(self.help_types)
            return '{}, {} e {} de {}'.format(start, choice1, choice2, author)

    def make_complementary_collections(self, with_n=True):
        if with_n:
            return '({}, {})'.format(self._pick_surname().title(), str(random.randint(1, 300)))
        else:
            return '({})'.format(self._pick_surname().title())

    @staticmethod
    def make_complementary_notes():
        notes = ['No prelo']  # add more notes
        return '{}'.format(notes[0])

    def make_academic_type(self):
        return random.choice(self.work_types)

    def make_graduation_in(self):
        grad = self._pick_graduation()
        return '({} em {})'.format(random.choice(self.br_grad_types), grad)

    def add_advisor(self):
        advisor = '{} {}'.format(
            self._pick_name().title(), self._pick_surname().title())
        if random.randint(0, 1) == 0:
            return 'Orientador: {}'.format(advisor)
        else:
            return 'Orientadora: {}'.format(advisor)

    def academic_event(self, type):
        if type == 'deprecated':
            return '{}...'.format(random.choice(self.event_type))
        if type == 'updated':
            return '{} [...]'.format(random.choice(self.event_type))

    def make_e_reference(self, type):
        link = self._pick_link()
        date = self.make_date('journal')
        if type == 'deprecated':
            return 'Disponível em: <{}>. Acesso em: {}'.format(link, date)
        if type == 'updated':
            return 'Disponível em: {}. Acesso em: {}'.format(link, date)

    def make_doi(self):
        doi = self._pick_doi()
        return 'DOI {}'.format(doi)
