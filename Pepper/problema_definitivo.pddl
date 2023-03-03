(define (problem problema_definitivo) (:domain dominio_definitivo)
(:objects
    robot - agent
    anne - agent
    sally - agent
    box1 - thing
    box2 - thing
    emptySpace - thing
    ball - thing
    room - place
    elsewhere - place
    start - id
    end - id
    t1 - id
    t2 - id
    t3 - id
    t4 - id
    t5 - id
    t6 - id
    t7 - id
    t8 - id
    t9 - id
    t10 - id
    t11 - id 
    t12 - id
    t13 - id
    t14 - id
    t15 - id
    t16 - id
    t17 - id
    t18 - id
    t19 - id
    t20 - id
    t21 - id
    t22 - id

    g1 - id
    g2 - id
    g3 - id
    g4 - id
    g5 - id
)

(:init
    (isEnd end)
    
    ; All the start ids
    (isStart t1)
    (isStart t2)
    (isStart t3)
    (isStart t4)
    (isStart t5)
    (isStart t6)
    (isStart t7)
    (isStart t8)
    (isStart t9)
    (isStart t10)
    (isStart t11)
    (isStart t12)
    (isStart t13)
    (isStart t14)
    (isStart t15)
    (isStart t16)

    ; All the free ids
    (free t17)
    (free t18)
    (free t19)
    (free t20)
    (free t21)
    (free t22) 

    ; This disjunction is useful to avoid reusing the free ids in some actions
    (disjuncted_id t17 t18)
    (disjuncted_id t17 t19)
    (disjuncted_id t17 t20)
    (disjuncted_id t17 t21)
    (disjuncted_id t17 t22)

    (disjuncted_id t18 t19)
    (disjuncted_id t18 t20)
    (disjuncted_id t18 t21)
    (disjuncted_id t18 t22)
   
    (disjuncted_id t19 t20)
    (disjuncted_id t19 t21)
    (disjuncted_id t19 t22)

    (disjuncted_id t20 t21)
    (disjuncted_id t20 t22)

    (disjuncted_id t21 t22)

    ; This disjunction is useful to avoid reusing the same agent in some actions
    (disjuncted_a sally anne)
    (disjuncted_a sally robot)  
    (disjuncted_a anne sally)
    (disjuncted_a anne robot)
    (disjuncted_a robot sally)
    (disjuncted_a robot anne)

    ; This disjunction is useful to avoid reusing the same "thing" in some actions
    (disjuncted ball box1)
    (disjuncted box1 ball)
    (disjuncted ball box2)
    (disjuncted box2 ball)
    (disjuncted emptySpace ball)
    (disjuncted ball emptySpace)
    (disjuncted box2 box1)
    (disjuncted box1 box2)
    (disjuncted box1 emptySpace)
    (disjuncted emptySpace box1)
    (disjuncted box2 emptySpace)
    (disjuncted emptySpace box2)  
    (disjuncted room box1)
    (disjuncted box1 room)
    (disjuncted room emptySpace)
    (disjuncted emptySpace room)
    (disjuncted box2 room)
    (disjuncted room box2) 

    ; This disjunction is useful to avoid reusing the same place in some actions
    (disjuncted_r room elsewhere)
    (disjuncted_r elsewhere room)
 
    ;--- Scene
    (isAt t1 robot room)
    (isAt t2 anne room)
    (isAt t3 sally room)

    (Know t4 anne t2)
    (Know t5 anne t3)
    (Know t6 sally t2)
    (Know t7 sally t3)

    (isIn t8 ball emptySpace)
    (Know t9 anne t8)
    (Know t10 sally t8)

    ; Willingness of the agents about changin room or putting the ball into the box

    (Willing t11 anne t8)
    (Willing t12 sally t8)
    (Willing t13 anne t2)
    (NotSureIfWilling t14 sally t3)

    (Desire t15 sally g1)
    (isIn g1 ball box1)
    (Desire t16 anne g2)
    (isAt g2 sally elsewhere)

    ;(isEmpathic sally)
    (isNeutral sally); for goal ok4
    (isNeutral anne)
    ;(isEmpathic anne); for goal ok5
)


; To test the various goal, uncomment the (ok1,2,3,4,5,6) to activate the test actions:
; ok1 -> activates test1
; ok2 -> activates test2 
; ....

(:goal  
    (and 
        ;(ok1)     ;description: Want Sally to know something that is true that Anne doesn't know
        ;(ok2)     ;description: Want to blame Sally because the ball is in the box1 while Anne ignores that she has been blamed
        ;(ok3)     ;description: Tell agent 1 that he/she has been insulted by agent 2 
        (ok4)     ;description: Want to make Sally sad without insulting her
        ;(ok5)     ;description: Want to make Sally and Anne happy for something while they both ignore the emotional state of the other one
        ;(ok6)     ;description: Want to make Sally happy for something and angry because Anne has been insulted, while making Anne sad for something that isn't the insult
        ;(ok7)     ;description: Want to make Sally sad by insulting Anne
        ;(ok8)     ;description: Want an agent to know where the ball is while tolding this information to other one. Both should be out of the room at the end
        ;(ok9)     ;description: Want to make Sally sad. She and the other agent should be out of the room at the end 
        ;(ok10)    ;description: Want to make Sally surprised about a verified information, without blaming another agent, and both should be out of the room at the end 
        ;(ok11)
    )
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)