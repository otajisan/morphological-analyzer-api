# morphological-analyzer-api
Morphological Analyzer API (Python x FastAPI)

# Preview

```bash
curl -s -X POST -H 'Content-Type: application/json' http://localhost:8000/text/analyze/ -d '{"text": "吾輩は猫である"}'
[{"char_type":2,"feature":["代名詞","*","*","*","*","*","ワガハイ","我が輩","吾輩","ワガハイ","吾輩","ワガハイ","混","*","*","*","*","*","*","体","ワガハイ","ワガハイ","ワガハイ","ワガハイ","0","*","*","11321954766299648","41189"],"feature_raw":"代名詞,*,*,*,*,*,ワガハイ,我が輩,吾輩,ワガハイ,吾輩,ワガハイ,混,*,*,*,*,*,*,体,ワガハイ,ワガハイ,ワガハイ,ワガハイ,0,*,*,11321954766299648,41189","is_unk":false,"length":6,"posid":1,"rlength":6,"stat":0,"surface":"吾輩","white_space":""},{"char_type":6,"feature":["助詞","係助詞","*","*","*","*"," ハ","は","は","ワ","は","ワ","和","*","*","*","*","*","*","係助","ハ","ハ","ハ","ハ","*","動詞%F2@0,名詞%F1,形容詞%F2@-1","*","8059703733133824","29321"],"feature_raw":"助詞,係助詞,*,*,*,*,ハ,は,は,ワ,は,ワ,和,*,*,*,*,*,*,係助,ハ,ハ,ハ,ハ,*,\"動詞%F2@0,名詞%F1,形容詞%F2@-1\",*,8059703733133824,29321","is_unk":false,"length":3,"posid":1,"rlength":3,"stat":0,"surface":"は","white_space":""},{"char_type":2,"feature":["名詞","普通名詞","一般","*","*","*","ネコ","猫","猫","ネコ","猫","ネコ","和","*","*","*","*","*","*","体","ネコ","ネコ","ネコ","ネコ","1","C4","*","7918141678166528","28806"],"feature_raw":"名詞,普通名詞,一般,*,*,*,ネコ,猫,猫,ネコ,猫,ネコ,和,*,*,*,*,*,*,体,ネコ,ネコ,ネコ,ネコ,1,C4,*,7918141678166528,28806","is_unk":false,"length":3,"posid":1,"rlength":3,"stat":0,"surface":"猫","white_space":""},{"char_type":6,"feature":["助動詞","*","*","*","助動詞-ダ","連用形-一般","ダ","だ","で","デ","だ","ダ","和","*","*","*","*","*","*","助動","デ","ダ","デ","ダ","*","名詞%F1","*","6299110739157633","22916"],"feature_raw":"助動詞,*,*,*,助動詞-ダ,連用形-一般,ダ,だ,で,デ,だ, ダ,和,*,*,*,*,*,*,助動,デ,ダ,デ,ダ,*,名詞%F1,*,6299110739157633,22916","is_unk":false,"length":3,"posid":1,"rlength":3,"stat":0,"surface":"で","white_space":""},{"char_type":6,"feature":["動詞","非自立可能","*","*","五段-ラ行","連体形-一般","アル","有る","ある","アル","ある","アル","和","*","*","*","*","*","*","用","アル","アル","アル","アル","1","C3","*","334260158472897","1216"],"feature_raw":"動詞,非自立可能,*,*,五段-ラ行,連体形-一般,アル,有る,ある,アル,ある,アル,和,*,*,*,*,*,*,用,アル,アル,アル,アル,1,C3,*,334260158472897,1216","is_unk":false,"length":6,"posid":1,"rlength":6,"stat":0,"surface":"ある","white_space":""}]%
```

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

# Open API
- http://localhost:8000/docs

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
- [fugashi](https://pypi.org/project/fugashi/)