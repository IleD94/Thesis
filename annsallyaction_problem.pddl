(define (problem annsallyaction_problem) (:domain annsallyaction_domain)
(:objects

    robot - agent
    anne - agent
    sally - agent

    chest - cosa
    box - cosa
    ball - cosa

    room - place
    elsewhere - place



    first - phase
    second - phase
    third - phase
    fourth - phase
    fifth - phase

    start - id
    end - id

    one - id
    two - id
    three - id
    four - id
    five - id
    six - id
    seven - id
    eight - id
    nine - id
    ten - id
    eleven - id
    twelve - id
    thirteen - id
    fourteen - id
    fifteen - id
    sixteen - id
    seventeen - id
    eighteen - id
    nineteen - id
    twenty - id
    twentyone - id
    twentytwo - id
    twentythree - id
    twentyfour - id
    twentyfive - id
    twentysix - id
    twentyseven - id
    twentyeight - id
    twentynine - id
    thirty - id
    thirtyone - id
    thirtytwo - id
    thirtythree - id
    thirtyfour - id
)
(:init

    (hasStartId robot start)
    (hasStartId sally start)
    (hasStartId anne start)

    (follow second first)
    (follow third second)
    (follow fourth third)
    (follow fifth fourth)

    (disjuncted sally anne)
    (disjuncted sally robot)
    (disjuncted sally chest)
    (disjuncted sally box)
    (disjuncted sally ball)
    (disjuncted sally room)
    (disjuncted sally elsewhere)
    
    (disjuncted anne sally)
    (disjuncted anne robot)
    (disjuncted anne chest)
    (disjuncted anne box)
    (disjuncted anne ball)
    (disjuncted anne room)
    (disjuncted anne elsewhere)

    (disjuncted robot sally)
    (disjuncted robot anne)
    (disjuncted robot chest)
    (disjuncted robot box)
    (disjuncted robot ball)
    (disjuncted robot room)
    (disjuncted robot elsewhere)

    (disjuncted chest anne)
    (disjuncted chest robot)
    (disjuncted chest sally)
    (disjuncted chest box)
    (disjuncted chest ball)
    (disjuncted chest room)
    (disjuncted chest elsewhere)

    (disjuncted box anne)
    (disjuncted box robot)
    (disjuncted box chest)
    (disjuncted box sally)
    (disjuncted box ball)
    (disjuncted box room)
    (disjuncted box elsewhere)  

    (disjuncted ball anne)
    (disjuncted ball robot)
    (disjuncted ball chest)
    (disjuncted ball box)
    (disjuncted ball sally)
    (disjuncted ball room)
    (disjuncted ball elsewhere) 

    (disjuncted room anne)
    (disjuncted room robot)
    (disjuncted room chest)
    (disjuncted room box)
    (disjuncted room ball)
    (disjuncted room sally)
    (disjuncted room elsewhere) 

    (disjuncted elsewhere anne)
    (disjuncted elsewhere robot)
    (disjuncted elsewhere chest)
    (disjuncted elsewhere box)
    (disjuncted elsewhere ball)
    (disjuncted elsewhere room)
    (disjuncted elsewhere sally) 

    ;--- First scene
    (Know start robot one first)
    (isIn one robot room first)
    (See start robot two first)
    (isIn two sally room first)
    (See start robot three first)
    (isIn three anne room first)
    (See start robot four first)
    (isIn four chest room first)
    (See start robot five first)
    (isIn five box room first)
    (See start robot six first)
    (isHappy six sally end first)
    (See start robot seven first)
    (isHappy seven anne end first)


    ; ;--- Second scene
    (Know start robot eight second)
    (isIn eight robot room second)
    (See start robot nine second)
    (isIn nine sally room second)
    (See start robot ten second)
    (isIn ten anne room second)
    (See start robot eleven second)
    (isIn eleven chest room second)
    (See start robot twelve second)
    (isIn twelve box room second)
    (See start robot thirteen second)
    (isHappy thirteen sally end second)
    (See start robot fourteen second)
    (isHappy fourteen anne end second)
    (See start robot fifteen second)
    (isIn fifteen ball room second)
    (See start robot sixteen second)
    (isPutting sixteen sally ball chest second)


    ; ;-- Third scene
    (Know start robot seventeen third)
    (isIn seventeen robot room third)
    (See start robot eighteen third)
    (isIn eighteen sally room third)
    (See start robot nineteen third)
    (isIn nineteen anne room third)
    (See start robot twenty third)
    (isIn twenty chest room third)
    (See start robot twentyone third)
    (isIn twentyone box room third)
    (See start robot twentytwo third)
    (isHappy twentytwo sally end third)
    (See start robot twentythree third)
    (isGoing twentythree sally room elsewhere third)


    ; --- Fourth scene
    (Know start robot twentyfour fourth)
    (isIn twentyfour robot room fourth)
    (See start robot twentyfive fourth)
    (isIn twentyfive anne room fourth)
    (See start robot twentysix fourth)
    (isIn twentysix chest room fourth)
    (See start robot twentyseven fourth)
    (isIn twentyseven box room fourth)
    (See start robot twentyeight fourth)
    (isHappy twentyeight anne end fourth)
    (See start robot twentynine fourth)
    (isPutting twentynine anne ball box fourth)


    ; --- Fifth scene
    (Know start robot thirty fifth)
    (isIn thirty robot room fifth)
    (See start robot thirtyone fifth)
    (isIn thirtyone sally room fifth)
    (See start robot thirtytwo fifth)
    (isIn thirtytwo chest room fifth)
    (See start robot thirtythree fifth)
    (isIn thirtythree box room fifth)
    (See start robot thirtyfour fifth)
    (isHappy thirtyfour sally end fifth)
)

(:goal  
    (and (ok))
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
