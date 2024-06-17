### SiakadPlus

This School Managemet System

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app siakadplus
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/siakadplus
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit


===============================

# apps

- siakadplus
- siakadplus_admin
- siakadplus_guardian


## siakadplus_admin

Doctype
- school
    if school create, that will:
    - [done] create new site with school name
    - [done] install siakadplus app to the site
    - [done] automatic setup widzard
    - add user with role school admin 
    [done] admin can nonactive the site (school)
    [done] download backup data school
    delete and import data school use backup