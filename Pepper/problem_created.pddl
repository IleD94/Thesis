(define 
    (problem official_problem)
    (:domain official_domain) 
    (:objects 

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
    Ilenia - agent
    robot - agent    
)
    (:init
        (isAt t2 Ilenia room)
        (isEmpathic Ilenia)
        (isAt t1 robot room)
        (isEnd end)
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
        (disjuncted_r room elsewhere)
        (disjuncted_r elsewhere room)
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
        (isIn t8 ball emptySpace)
        (isIn g1 ball box1)
        (isIn g3 ball box1)
        (isIn g4 ball box2)
        (isIn g5 ball emptySpace)
        
    )
    (:goal (and
        (ok8)
    )  
)    
)