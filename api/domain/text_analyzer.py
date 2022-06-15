from fugashi import Tagger

from api.domain.analyzed_text_entity import AnalyzedTextEntity
from api.domain.input_text_entity import InputTextEntity


class TextAnalyzer:
    tagger = Tagger()

    def analyze(self, entity: InputTextEntity):
        results = []
        for word in self.tagger(entity.text):
            item = AnalyzedTextEntity(
                char_type=word.char_type,
                feature=word.feature,
                feature_raw=word.feature_raw,
                is_unk=word.is_unk,
                length=word.length,
                posid=word.posid,
                rlength=word.rlength,
                stat=word.stat,
                surface=word.surface,
                white_space=word.white_space
            )
            results.append(item)
        return results
