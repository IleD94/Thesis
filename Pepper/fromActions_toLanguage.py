from collections import OrderedDict
def fromActions_toLanguage (ag1, obj, ag2, place, action):
    actions = OrderedDict  ([
            ('ask_put_alone', ag1+ ' put ' + obj + ' into the '+ place + ', because '+ ag2 + ' is not here '),
            ('ask_put_alone_manipulative',  ag1 + ' put ' + obj + " into the "+ place + ' when '+ ag2 + 'is not here '),
            ('ask_put_infrontof', ag1+ ' put ' + obj + " into the "+ place + ' considering  '+ ag2 + 'is here '),
            ('ask_put_infrontof_manipulative',  ag1 + ' put ' + obj + " into the "+ place + ' in front of '+ ag2 ),
            ('ask_go',  ag1 + ' go out, now'),
            ('ask_go_manipulative', ag1 + ' go out, now '),
            ('ask_comeback_manipulative', ag1 + ' comeback, now '),
            ('ask_comeback', ag1 + ' comeback, now'),
            ('insult_alone', ' insult' + ag1 + ' when ' + ag2 + ' is not here '),
            ('insult_infrontof', ' insult ' + ag1 + ' in font of ' + ag2 ),
            ('ask_insult_alone',  ag1 + ' insult ' + ag2+ ', when ' + ag2 + ' is not here '),
            ('ask_insult_infrontof', ag1 + ' insult ' + ag2+ ' in front of ' + ag2 ),
            ('praise_alone', ' praise' + ag1 + ' when ' + ag2 + ' is not here '),
            ('praise_infrontof', ' praise ' + ag1 + ' in font of ' + ag2 ),
            ('ask_praise_alone', ag1 + ' praise ' + ag2+ ' when ' + ag2 + ' is not here '),
            ('ask_praise_infrontof', ag1 + ' praise ' + ag2+ ' in front of ' + ag2),
            ('test', "say I've reached my goal, I'm happy")
            ])
    
    actions['tell_alone'] = ' tell ' + ag2 + ' when is alone that ' + actions.get(action)
    actions['tell_everybody'] = ' tell ' + ag2 + ' in front of everybody that ' + actions.get(action)
    actions['tell_infrontof'] = ' tell ' + ag2 + ' in front of ' + ag1 + ' that ' + actions.get(action)
    actions['blamefor_alone'] = ' blame ' + ag1 + ' for ' + actions.get(action) + ' when ' + ag2 + ' is not here '
    actions['blamefor_infrontof'] = ' blame ' + ag1 + ' for ' + actions.get(action) + ' in front of ' + ag2
    actions['ask_blamefor_alone'] = ag1 + ' blame ' + ag2 + ' for ' + actions.get(action) + ' when ' + ag2 + ' is not here ' 
    actions['ask_blamefor_infrontof'] = ag1 + ' blame ' + ag2 + ' for ' + actions.get (action) + ' in front of ' + ag2
    actions['complimentfor_alone'] = ' compliment ' + ag1 + ' for '+ actions.get (action) + ' when ' + ag2 + ' is not here '
    actions['complimentfor_infrontof'] = ' compliment ' + ag1 + ' for '+ actions.get (action) + ' in front of ' + ag2
    actions['ask_complimentfor_alone'] = ag1 + ' compliment ' + ag2 + ' for ' + actions.get (action) + ' when ' + ag2 + ' is not here '
    actions['ask_complimentfor_infrontof'] = ag1 + ' compliment ' + ag2 + ' for ' + actions.get (action) + ' in front of ' + ag2        
    return (actions)
