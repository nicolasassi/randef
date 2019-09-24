import sqlite3
import pandas as pd

conn = sqlite3.connect('db/sources.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE TITLES([generated_id] INTEGER PRIMARY KEY,[title] text, [categories] text)''')

# Create table - COUNTRY
c.execute('''CREATE TABLE COUNTRIES([generated_id] INTEGER PRIMARY KEY,[country_name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE DOIs([generated_id] INTEGER PRIMARY KEY, [doi] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE RESEARCH_ORGANIZATIONS([generated_id] INTEGER PRIMARY KEY, [organization_name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE LINKS([generated_id] INTEGER PRIMARY KEY, [link] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE NAMES([generated_id] INTEGER PRIMARY KEY, [name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE CITIES([generated_id] INTEGER PRIMARY KEY, [city_name] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE SURNAMES([generated_id] INTEGER PRIMARY KEY, [surname] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE GRADUATIONS([generated_id] INTEGER PRIMARY KEY, [graduation_name] text, [country] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE EDITORS([generated_id] INTEGER PRIMARY KEY, [editor] text)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE SOURCES([generated_id] INTEGER PRIMARY KEY, [source] text)''')

conn.commit()

read_countries = pd.read_csv("sources/countries.csv")
read_countries.to_sql('COUNTRIES', conn, if_exists='append', index = False)

read_cities = pd.read_csv("sources/cities.csv")
read_cities.to_sql('CITIES', conn, if_exists='append', index = False)

read_dois = pd.read_csv("sources/dois.csv")
read_dois.to_sql('DOIs', conn, if_exists='append', index = False)

read_editors = pd.read_csv("sources/eds.csv")
read_editors.to_sql('EDITORS', conn, if_exists='append', index = False)

read_grads = pd.read_csv("sources/grads.csv")
read_grads.to_sql('GRADUATIONS', conn, if_exists='append', index = False)

read_links = pd.read_csv("sources/links.csv")
read_links.to_sql('LINKS', conn, if_exists='append', index = False)

read_names = pd.read_csv("sources/names.csv")
read_names.to_sql('NAMES', conn, if_exists='append', index = False)

read_sources = pd.read_csv("sources/sources.csv")
read_sources.to_sql('SOURCES', conn, if_exists='append', index = False)

read_research_orgs = pd.read_csv("sources/research_orgs.csv")
read_research_orgs.to_sql('RESEARCH_ORGANIZATIONS', conn, if_exists='append', index = False)

read_surnames = pd.read_csv("sources/surnames.csv")
read_surnames.to_sql('SURNAMES', conn, if_exists='append', index = False)

read_title_categories = pd.read_csv("sources/title_categories.csv")
read_title_categories.to_sql('TITLES', conn, if_exists='append', index = False)