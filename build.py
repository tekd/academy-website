from os import path, getcwd
from sys import stdout
from yaml import load
from slugify import slugify
from datetime import date
from staticjinja import make_site
from dateutil.parser import parse

from govlabstatic.cli import Manager

ROOT_DIR = path.abspath(path.dirname(__file__))

# We define constants for the deployment.
searchpath = path.join(ROOT_DIR, 'templates')
outputpath = path.join(ROOT_DIR, 'site')

# We load the data we want to use in the templates.
PEOPLE = load(open('data/people.yaml'))
CLINICS = load(open('data/clinics.yaml'))
LIBRARY = load(open('data/library.yaml'))
COACHING = load(open('data/coaching.yaml'))
PROJECTS = load(open('data/project-gallery.yaml'))
WORKSHOPS = load(open('data/workshops.yaml'))

for p in PEOPLE:
    p['fullName'] = '%s %s' % (p['name']['first'], p['name']['last'])

PEOPLE = sorted(PEOPLE, key=lambda x: x['name']['last'])

for item in COACHING:
    item['start_date'] = parse(item['date']['start']).date()
    item['outdated'] = item['start_date'] < date.today()

COACHING = sorted(COACHING, key=lambda x: x['start_date'])

def loadAcademyData():
    return {
        'people': PEOPLE,
        'clinics': CLINICS,
        'projects': PROJECTS,
        'coaching': COACHING,
        'workshops': WORKSHOPS
    }

def debug(text):
    print('text')

    stdout.flush()

    return ''


def isEmpty(seq):
    return len([k for k in seq]) == 0


def nameTest(name, value):
    return '%s %s' % (name['first'], name['last']) == value


filters = {
    'slug': lambda x: slugify(x.lower()),
    'debug': debug,
    'byName': lambda x: [p for p in PEOPLE if p.name == x],
    'isEmpty': isEmpty
}

def render_coaching_detail_pages(env, template, **kwargs):
    '''
    staticjinja rule for generating all individual coaching detail pages.
    '''

    template = env.get_template('_coaching-detail-page.html')

    for index, coaching_class in enumerate(COACHING):
        filename = '%s-detail.html' % slugify(coaching_class['name'].lower())
        template.stream(coaching_class=coaching_class, **kwargs).\
            dump(path.join(env.outpath, filename))


site = make_site(
    filters=filters,
    outpath=outputpath,
    contexts=[
        (r'.*.html', loadAcademyData),
        (r'coaching-detail-pages.custom', loadAcademyData),
    ],
    rules=[
        (r'coaching-detail-pages.custom', render_coaching_detail_pages),
    ],
    searchpath=searchpath,
    staticpaths=['static', '../data'],
)

manager = Manager(
    site_name='govlabacademy.org',
    site=site,
    sass_src_path=path.join(ROOT_DIR, 'sass', 'styles.scss'),
    sass_dest_path=path.join(searchpath, 'static', 'styles',
                             'styles.css')
)

if __name__ == '__main__':
    manager.run()
