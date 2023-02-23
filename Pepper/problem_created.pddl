(define 
    (problem thesis_problem3)
    (:domain thesis_domain3) 
    (:objects 
        box1 - thing
        box2 - thing
        ball - thing
        emptySpace - thing
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
        t23 - id
        Giovanni - agent
        Ilenia - agent
        robot - agent    
)
    (:init
        (isAt t2 Ilenia room)
        (isAt t3 Giovanni room)
        (isAt t1 robot room)
        (hasStartAgent robot)
        (isEnd end)
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
        (isStart t23)
        (free t17)
        (free t18)
        (free t19)
        (free t20)
        (free t21)
        (free t22)
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
        (disjuncted room box1)
        (disjuncted box1 room)
        (disjuncted room emptySpace)
        (disjuncted emptySpace room)
        (disjuncted box2 room)
        (disjuncted room box2)
        (isIn t8 ball emptySpace)
        (Know t4 Ilenia t2)
        (Know t6 Giovanni t2)
        (Know t9 Ilenia t8)
        (Know t5 Ilenia t3)
        (Know t7 Giovanni t3)
        (Know t10 Giovanni t8)
        (Willing t11 Ilenia t8)
        (Willing t12 Giovanni t8)
        (Willing t13 Ilenia t2)
        (NotSureIfWilling t14 Giovanni t3)
        (Ignore t15 Giovanni t16)
        (Ignore t23 Ilenia t16)
        (disjuncted_a Ilenia Giovanni)
        (disjuncted_a Giovanni Ilenia)
        (disjuncted_a Giovanni robot)
        (disjuncted_a Ilenia robot)
        (disjuncted_a robot Giovanni)
        (disjuncted_a robot Ilenia)
        
    )
    (:goal (and
        (ok)
    )  
)    
)