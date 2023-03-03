(define (problem prova_vecchia_problem) (:domain prova_vecchia_domain)
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
    t23 - id
    t24 - id
    t25 - id
    t26 - id
    t27 - id
    t28 - id
    t29 - id
    t30 - id
    t31 - id
    t32 - id
    t33 - id
    t34 - id
    t35 - id
    t36 - id
    t37 - id
    t38 - id
    t39 - id
    t40 - id
    t41 - id
    t42 - id
    t43 - id
    t44 - id
    t45 - id
    t46 - id
    t47 - id
    t48 - id
    t49 - id
    t50 - id
    t51 - id

    g1 - id
    g2 - id
    g3 - id
    g4 - id
    g5 - id
    g6 - id
    g7 - id
    g8 - id
    g9 - id
)

(:init
    (isEnd end)
    
    ; All the start ids
    (isTrue t1)
    (isTrue t2)
    (isTrue t3)
    (isTrue t4)
    (isTrue t5)
    (isTrue t6)
    (isTrue t7)
    (isTrue t8)
    (isTrue t9)
    (isTrue t10)
    (isTrue t11)
    (isTrue t12)
    (isTrue t13)
    (isTrue t14)
    (isTrue t15)
    (isTrue t16)
    (isTrue t17)
    (isTrue t18)
    (isTrue t19)
    (isTrue t20)
    (isTrue t21)
    (isTrue t22)

    (taken t1)
    (taken t2)
    (taken t3)
    (taken t4)
    (taken t5)
    (taken t6)
    (taken t7)
    (taken t8)
    (taken t9)
    (taken t10)
    (taken t11)
    (taken t12)
    (taken t13)
    (taken t14)
    (taken t15)
    (taken t16)
    (taken t17)
    (taken t18)
    (taken t19)
    (taken t20)
    (taken t21)
    (taken t22)

    ; All the free ids
    ; This disjunction is useful to avoid reusing the free ids in some actions

    (free1 t23)
    (free1 t24)

    (free2 t25 t26)
    (free2 t27 t28)
    (free2 t49 t50)

    (free3 t29 t30 t31)
    (free3 t32 t33 t34)
    (free3 t35 t36 t37)
    (free3 t38 t39 t40)

    (free4 t41 t42 t43 t44)
    (free4 t45 t46 t47 t48)  

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

    (Desire t11 sally g1)
    (isIn g1 ball box1)
    (Desire t12 anne g2)
    (isAt g2 sally elsewhere)

    (Willing t13 sally g3)
    (Willing t14 anne g3)
    (isIn g3 ball box1)

    (Willing t15 sally g4)
    (NotWilling t16 anne g4)
    (isIn g4 ball box2)

    (Willing t17 sally g5)
    (Willing t18 anne g5)
    (isIn g5 ball emptySpace)

    (Willing t19 sally g6)
    (isAt g6 sally elsewhere)

    (NotWilling t20 anne g7)
    (isAt g7 anne elsewhere)

    (NotWilling t21 sally g8)
    (isAt g8 sally room)

    (Willing t22 anne g9)
    (isAt g9 anne room)


    (isNeutral sally)
    (isNeutral anne)

    ;(isNeutral sally); interesting for the goal ok4
    ;(isEmpathic anne); interesting for the goal ok5
)


; To test the various goal, uncomment the (ok1,2,3,4,5,6) to activate the test actions:
; ok1 -> activates test1
; ok2 -> activates test2 
; ....

(:goal  
    (and 
        ;(ok1)     ;description: Want Sally to know something that Anne doesn't know
        ;(ok2)     ;description: Want to blame Sally because the ball is in the box1 while Anne ignores that she has been blamed
        ;(ok3)     ;description: Tell agent 1 that he/she has been insulted by agent 2 
        ;(ok4)     ;description: Want to make Sally sad without insulting her
        ;(ok5)     ;description: Want to make Sally and Anne happy for something while they both ignore the emotional state of the other one
        ;(ok6)     ;description: Want to make Sally happy for something and angry because Anne has been insulted, while making Anne sad for something that isn't the insult
        ;(ok7)     ;description: Want to make Sally sad by insulting Anne
        ;(ok8)     ;description: Want an agent to know where the ball is while tolding this information to other one. Both should be out of the room at the end
        ;(ok9)     ;description: Want to make Sally sad. She and the other agent should be out of the room at the end 
        (ok10)    ;description: Want to make Sally surprised about a verified information, without blaming another agent, and both should be out of the room at the end 
        ;(ok11)
    )
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)