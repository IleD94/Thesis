
from collections import OrderedDict
def fromPredicates_toLanguage (pred):
    predicates = OrderedDict  ([
            ('(isEcstasy_joy_serenity', pred [2]+ ' is happy '),
            ('(isGrief_sadness_pensiveness',  pred [2] + ' is sad '),
            ('(isRage_anger_annoyance', pred [2] + ' is angry '),
            ('(isTerror_fear_apprehension', pred [2] + ' is scared ' ),
            ('(isAmazement_surprise_distraction',  pred [2] + ' is surprised '),
            ('(isLoathing_disgust_boredom', pred [2] + ' is disgusted '),
            ('(isSadic', pred [1] + ' is sadic '),
            ('(isNarcissist', pred [1] + ' is narcissist '),
            ('(isPsychopath', pred [1] + ' is Psychopath '),
            ('(isDependent',  pred [1] + 'is Dependent' ),
            ('(isEmpathic',  pred [1] + ' is empathic'),
            ('(isNeutral', pred [1] + ' is Neutral' ),
            ('isIn', pred [2] +' is in' + pred [3]),
            ('(Know', pred [1] + "knows something"),
            ])
    return predicates.get(pred[0])