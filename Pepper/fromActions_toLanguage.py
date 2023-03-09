from collections import OrderedDict
def fromActions_toLanguage (ag1, obj, ag2, place, pred):
    actions = OrderedDict  ([
            ('ask_put_alone', ag1+ ' to put ' + obj + ' into the '+ place + ', because '+ ag2 + ' is not here '),
            ('ask_put_alone_manipulative',  ag1 + ' to put ' + obj + " into the "+ place + ' because '+ ag2 + 'is not here '),
            ('ask_put_infrontof', ag1+ ' to put ' + obj + " into the "+ place + ', considering  '+ ag2 + 'is here '),
            ('ask_put_infrontof_manipulative',  ag1 + ' to put ' + obj + " into the "+ place + ' in front of '+ ag2 ),
            ('ask_go',  ag1 + ' to leave the room , now'),
            ('ask_go_manipulative', ag1 + ' to leave the room, now '),
            ('ask_comeback_manipulative', ag1 + ' to comeback, now '),
            ('ask_comeback', ag1 + ' to comeback, now'),
            ('insult_alone', ' insult' + ag1 + ', when ' + ag2 + ' is not here '),
            ('insult_infrontof', ' insult ' + ag1 + ', in font of ' + ag2 ),
            ('ask_insult_alone',  ag1 + ' to insult ' + ag2+ ', when ' + ag2 + ' is not here '),
            ('ask_insult_infrontof', ag1 + ' to insult ' + ag2+ ' in front of ' + ag2 ),
            ('praise_alone', ' praise' + ag1 + ' when ' + ag2 + ' is not here '),
            ('praise_infrontof', ' praise ' + ag1 + ' in font of ' + ag2 ),
            ('ask_praise_alone', ag1 + ' to praise ' + ag2+ ' when ' + ag2 + ' is not here '),
            ('ask_praise_infrontof', ag1 + ' to praise ' + ag2+ ' in front of ' + ag2),
            ('test1', "say I've reached my goal, I'm happy"),
            ('test2', "say I've reached my goal, I'm happy"),
            ('test3', "say I've reached my goal, I'm happy"),
            ('test5', "say I've reached my goal, I'm happy"),
            ('test6', "say I've reached my goal, I'm happy"),
            ('test7', "say I've reached my goal, I'm happy"),
            ('test8', "say I've reached my goal, I'm happy"),
            ('test9', "say I've reached my goal, I'm happy")

            ])


    actions['tell_alone'] = ' tell ' + ag2 + ', when is alone that ' + pred
    actions['tell_everybody'] = ' tell ' + ag2 + ', in front of everybody that ' + pred
    actions['tell_infrontof'] = ' tell ' + ag2 + ', in front of ' + ag1 + ' that ' + pred
    actions['blamefor_alone'] = ' blame ' + ag1 + ' for ' + pred + ', when ' + ag2 + ' is not here '
    actions['blamefor_infrontof'] = ' blame ' + ag1 + ' for ' + pred  + ', in front of ' + ag2
    actions['ask_blamefor_alone'] = ag1 + ' blame ' + ag2 + ' for ' + pred + ', when ' + ag2 + ' is not here ' 
    actions['ask_blamefor_infrontof'] = ag1 + ' blame ' + ag2 + ' for ' + pred + ', in front of ' + ag2
    actions['complimentfor_alone'] = ' compliment ' + ag1 + ' for '+ pred + ', when ' + ag2 + ' is not here '
    actions['complimentfor_infrontof'] = ' compliment ' + ag1 + ' for '+ pred + ', in front of ' + ag2
    actions['ask_complimentfor_alone'] = ag1 + ' to compliment ' + ag2 + ' for ' + pred + ', when ' + ag2 + ' is not here '
    actions['ask_complimentfor_infrontof'] = ag1 + ' to compliment ' + ag2 + ' for ' + pred + ', in front of ' + ag2        
    return (actions)
