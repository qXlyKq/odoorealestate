{
    "name": "KNTU University Application",
    "version": "17.0.1.0.2",
    "category": "Learning",
    "license": "AGPL-3",
    "summary": "This application helps to orgenise learning classes",
    "author": "3PR PZS",
    "maintainers": ["3PR PZS"],
    "website": "kntu.net.ua",
    "depends": ['base'],
    "external_dependencies": {"python": []},
    "data": ["views/university.xml",
             "security/university_security.xml",
             "security/ir.model.access.csv",
             ],
    "qweb": [],
    "installable": True,
    "application": True,
}
