
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
            ('(isIn', pred [2] +' is in ' + pred [3]),
            ('(Know', pred [1] + " knows something"),
            ('(insulted', pred [2] + " was insulted by " + pred [3]),
            ('(praised', pred [2] + " was praised by " + pred [3]),
            ])
    
    if (len (pred))>4:
        predicates['(blamed'] = pred [2] + " was blamed by " + pred [4]
        predicates ['(givenCredit'] = pred [2] + " was given credit by " + pred [4]
            
    mypred = predicates.get(pred[0])
    return mypred