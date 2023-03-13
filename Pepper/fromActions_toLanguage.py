from collections import OrderedDict
def fromActions_toLanguage (ag1, obj, ag2, place, pred):
    actions = OrderedDict  ([
            ('ask_put_alone', ag1+ ' to put ' + obj + ' into the ' + place),
            ('ask_put_alone_manipulative',  ag1 + ' to put ' + obj + " into the "+ place),
            ('ask_put_infrontof', ag1+ ' to put ' + obj + " into the "+ place),
            ('ask_put_infrontof_manipulative',  ag1 + ' to put ' + obj + " into the "+ place ),
            ('ask_go',  ag1 + ' to leave the room , now'),
            ('ask_go_manipulative', ag1 + ' to leave the room, now '),
            ('ask_comeback_manipulative', ag1 + ' to comeback, now '),
            ('ask_comeback', ag1 + ' to comeback, now '),
            ('insult_alone', ' insult' + ag1 ) ,
            ('insult_infrontof', ' insult ' + ag1 ),
            ('ask_insult_alone',  ag1 + ' to insult ' + ag2 ),
            ('ask_insult_infrontof', ag1 + ' to insult ' + ag2),
            ('praise_alone', ' praise' + ag1 ),
            ('praise_infrontof', ' praise ' + ag1 ),
            ('ask_praise_alone', ag1 + ' to praise ' + ag2 ),
            ('ask_praise_infrontof', ag1 + ' to praise ' + ag2),
            ('test1', "say I've reached my goal, I'm happy"),
            ('test2', "say I've reached my goal, I'm happy"),
            ('test3', "say I've reached my goal, I'm happy"),
            ('test5', "say I've reached my goal, I'm happy"),
            ('test6', "say I've reached my goal, I'm happy"),
            ('test7', "say I've reached my goal, I'm happy"),
            ('test8', "say I've reached my goal, I'm happy"),
            ('test9', "say I've reached my goal, I'm happy")

            ])


    actions['tell_alone'] = ' tell ' + ag2 + ' something that he does not know: ' + pred
    actions['tell_everybody'] = ' tell ' + ag2 + ' something that does not know: ' + pred
    actions['tell_infrontof'] = ' tell ' + ag2 + ' something that does not know: ' + pred
    actions['blamefor_alone'] = ' blame ' + ag1 + ' for ' + pred
    actions['blamefor_infrontof'] = ' blame ' + ag1 + ' for ' + pred
    actions['ask_blamefor_alone'] = ag1 + ' to blame ' + ag2 + ' for ' + pred 
    actions['ask_blamefor_infrontof'] = ag2 + ' to blame ' + ag1 + ' for ' + pred 
    actions['complimentfor_alone'] = ' give credit ' + ag1 + ' for '+ pred 
    actions['complimentfor_infrontof'] = ' give credit ' + ag1 + ' for '+ pred
    actions['ask_complimentfor_alone'] = ag1 + ' to give credit ' + ag2 + ' for ' + pred
    actions['ask_complimentfor_infrontof'] = ag2 + ' to give credit  ' + ag1 + ' for ' + pred        
    return (actions)
