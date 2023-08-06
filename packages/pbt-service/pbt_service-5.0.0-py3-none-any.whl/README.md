[![N|Solid](https://294904.selcdn.ru/git/logo.png)](https://portalbilet.ru/)

# Service core

### Development
:warning: Dont use this commands for K8s.

##### Run
:memo: Create `.env` in <strong>$PROJECT_DIR</strong>

See example in `env.example`

```
python -m service develop
# or
python -m service develop --host 127.0.0.1 --port 9090
```

##### Tests
:memo: Create `.env.test` in <strong>$PROJECT_DIR</strong>

See example in `env.example`

```
python -m service tests
```

#### Migrations
Create a new migration:
```
python -m service make_migration example
```

Apply migrations:
```
python -m service migrate
```

Example rollback to exact revision:
```
python -m service rollback 689e54b32fa9
```


Use cli `alembic` as usual for other cases, but dont forget pass env variables before.

####  i18n

Add static translates for language.
Dont forget add language code in pyproject.toml i18n section before:

At first, init i18n static translates:
```shell script
python -m service i18n_init
```

Consider new language codes with `pyproject.toml`
```
[i18n]
locales = [
    "ru_RU",
    "en_US",
]
```

Add russian and english for example:
```shell script
python -m service i18n_add ru_RU
python -m service i18n_add en_US
```
