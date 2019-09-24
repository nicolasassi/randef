# -*- coding: utf-8 -*-

import os
from csv import reader
import random
import sqlite3

class Sources:

    data = dict()

    def __init__(self):
        with open('sources/utf8_chars', 'r', encoding='utf-8') as f:
            self.utf8_chars = [line.strip() for line in f.readlines()]
        conn = sqlite3.connect('db/sources.db')  # You can create a new database by changing the name within the quotes
        self.cursor = conn.cursor()
        tables = self.cursor.execute('''SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';''')
        tables = [table[0] for table in tables]
        self.table_count = dict()
        for table in tables:
            self.table_count[table] = self.cursor.execute('''SELECT COUNT(*) FROM {};'''.format(table)).fetchone()[0]


    def _pick_research_org(self):
        query = self.cursor.execute(
            '''SELECT organization_name FROM RESEARCH_ORGANIZATIONS WHERE generated_id = ?''', (str(random.randint(1, self.table_count['RESEARCH_ORGANIZATIONS'])),))
        return query.fetchone()[0]

    def _pick_surname(self):
        query = self.cursor.execute(
            '''SELECT surname FROM SURNAMES WHERE generated_id = ?''', (str(random.randint(1, self.table_count['SURNAMES'])),))
        return query.fetchone()[0]

    def _pick_name(self):
        query = self.cursor.execute(
            '''SELECT name FROM NAMES WHERE generated_id = ?''', (str(random.randint(1, self.table_count['NAMES'])),))
        return query.fetchone()[0]

    def _pick_country(self):
        query = self.cursor.execute(
            '''SELECT country_name FROM COUNTRIES WHERE generated_id = ?''', (str(random.randint(1, self.table_count['COUNTRIES'])),))
        return query.fetchone()[0]

    def _pick_city(self):
        query = self.cursor.execute(
            '''SELECT city_name FROM CITIES WHERE generated_id = ?''', (str(random.randint(1, self.table_count['CITIES'])),))
        return query.fetchone()[0]

    def _pick_title_categories(self):
        query = self.cursor.execute(
            '''SELECT title FROM TITLES WHERE generated_id = ?''', (str(random.randint(1, self.table_count['TITLES'])),))
        return query.fetchone()[0]

    def _pick_editor(self):
        query = self.cursor.execute(
            '''SELECT editor FROM EDITORS WHERE generated_id = ?''', (str(random.randint(1, self.table_count['EDITORS'])),))
        return query.fetchone()[0]

    def _pick_graduation(self):
        query = self.cursor.execute(
            '''SELECT graduation_name FROM GRADUATIONS WHERE generated_id = ?''', (str(random.randint(1, self.table_count['GRADUATIONS'])),))
        return query.fetchone()[0]


    def _pick_link(self):
        query = self.cursor.execute(
            '''SELECT link FROM LINKS WHERE generated_id = ?''', (str(random.randint(1, self.table_count['LINKS'])),))
        return query.fetchone()[0]


    def _pick_doi(self):
        query = self.cursor.execute(
            '''SELECT doi FROM DOIs WHERE generated_id = ?''', (str(random.randint(1, self.table_count['DOIs'])),))
        return query.fetchone()[0]


# s = Sources()
# import datetime
# now = datetime.datetime.now()
# for i in range(1, 10):
#     print(s._pick_doi())
# print(datetime.datetime.now()-now)