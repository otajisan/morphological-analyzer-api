# morphological-analyzer-api
Morphological Analyzer API (Python x FastAPI)


# Development

- Prepare environment

```bash
pip install pipenv
pipenv sync --dev

# update Pipfile.lock if needed
pipenv install --dev

# use pipenv
pipenv shell

# install packages
poetry install

# download unidic
python -m unidic download
```

- Then, run by poetry as follows

```bash
poetry run uvicorn api.main:app --reload
```

- PyCharm configuration
  - PyCharm -> Preferences -> Projects -> Python Interpreter
  - Add `venv` path as follows

```bash
/{path}/{to}/morphological-analyzer-api/venv
```

  - Run -> Edit Configurations
  - set values as follows

| key         | value|
|-------------|------|
| Script path | `/{path}/{to}/morphological-analyzer-api/.venv/bin/uvicorn` |
| Parameters | `api.main:app --reload` |

# Use AWS Unidic

```bash
aws s3  --no-sign-request cp s3://cotonoha-dic/unidic.zip ./
unzip unidic.zip
```

- and modify `TextAnalyzer` class as follows

```python
class TextAnalyzer:
    FUGASHI_TAGGER_ARGS = '-d /<path>/<to>/morphological-analyzer-api/unidic'
    tagger = Tagger(FUGASHI_TAGGER_ARGS)
...
```

# References
- [FastAPI](https://fastapi.tiangolo.com/ja/)
  - [Directory Layout](https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#file-structure)