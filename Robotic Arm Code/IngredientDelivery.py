def home_to_fry_cutter(ardu):
    home_position()
    posD01 = [0.16151249642469204,
              0.5346051066825475,
              0.25884643903434074,
              -1.4990040050250124,
              0.5930586855463937,
              0.6284033511022445]
    rtde_c.moveL(posD01, 0.1, 0.1)
    posD02 = [0.25103196461996685,
              0.4467411826285578,
              0.26952671470405415,
              -0.5844514569574193,
              1.5069150246057268,
              -0.7234667888315434]
    rtde_c.moveL(posD02, 0.1, 0.1)

    posD02j = [1.444921612739563,
               -2.0678227583514612,
               -1.9023597876178187,
               0.7829328775405884,
               0.03556693345308304,
               0.7833155393600464]
    rtde_c.moveJ(posD02j)

    posD03 = [0.2552583357978885,
              0.48027367896595063,
              0.26701397457237,
              -1.7572987124691122,
              0.8371940309248319,
              -1.808736645175887]
    rtde_c.moveL(posD03, 0.1, 0.1)

    posD04 = [0.23828029654069716,
              0.5756584800930565,
              0.3652514095344129,
              -1.7660311075425632,
              0.7970947859836965,
              -1.8010212468224873]
    rtde_c.moveL(posD04, 0.1, 0.1)

    posD05 = [0.21909811395619191,
              0.5659336514887756,
              0.41239803287049903,
              -1.752100172781796,
              0.7823539875660221,
              -1.7704106458732871]
    rtde_c.moveL(posD05, 0.1, 0.1)

    # this is drop off point
    posD06 = [0.2055678744441904,
              0.5557398375783428,
              0.4135890176322863,
              -1.7573324016245109,
              0.7544657436742626,
              -1.7570559430253785]
    rtde_c.moveL(posD06, 0.1, 0.1)

    #drop the ingredient
    gripper_open(ardu)
    gripper_close(ardu)

    posD05 = [0.21909811395619191,
              0.5659336514887756,
              0.41239803287049903,
              -1.752100172781796,
              0.7823539875660221,
              -1.7704106458732871]
    rtde_c.moveL(posD05, 0.1, 0.1)

    posD04 = [0.23828029654069716,
              0.5756584800930565,
              0.3652514095344129,
              -1.7660311075425632,
              0.7970947859836965,
              -1.8010212468224873]
    rtde_c.moveL(posD04, 0.1, 0.1)

    posD03 = [0.2552583357978885,
              0.48027367896595063,
              0.26701397457237,
              -1.7572987124691122,
              0.8371940309248319,
              -1.808736645175887]
    rtde_c.moveL(posD03, 0.1, 0.1)

    posD02j = [1.444921612739563,
               -2.0678227583514612,
               -1.9023597876178187,
               0.7829328775405884,
               0.03556693345308304,
               0.7833155393600464]
    rtde_c.moveJ(posD02j)

    posD02 = [0.25103196461996685,
              0.4467411826285578,
              0.26952671470405415,
              -0.5844514569574193,
              1.5069150246057268,
              -0.7234667888315434]
    rtde_c.moveL(posD02, 0.1, 0.1)

    posD01 = [0.16151249642469204,
              0.5346051066825475,
              0.25884643903434074,
              -1.4990040050250124,
              0.5930586855463937,
              0.6284033511022445]
    rtde_c.moveL(posD01, 0.1, 0.1)
    home_position()