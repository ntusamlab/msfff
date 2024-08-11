import module
gcode=['M104 S200.0']

# matrix=[[1,1,0,0],
#         [1,1,1,1],
#         [0,0,1,1],
#         [0,0,0,0]]
matrix=[[1,1,1,0],
        [1,1,1,0],
        [1,1,1,0],
        [0,0,0,0]]

gcode.extend(module.platform_reset(matrix))

pos=[[-20,-20],[-20,20],[20,20],[20,-20]]

E_sum=0

for ix in range(module.nx):
    for iy in range(module.ny-1,-1,-1):
        if matrix[ix][iy]==0:
            continue
        cx=(ix+0.5)*module.lx
        cy=(iy+0.5)*module.ly
        gcode.append('G0 F9000 X{0:.5f} Y{1:.5f} Z{2:.5f}'.format(cx+pos[-1][0],cy+pos[-1][1],module.z0+module.layer_height))
        for ih in range(1,4,1):
            gcode.append('G1 F1500 Z{0:.5f}'.format(module.z0+module.layer_height*ih))
            for ele in pos:
                E_sum=E_sum+40*module.ratio_e_xy
                gcode.append('G1 F1500 X{0:.5f} Y{1:.5f} E{2:.5f}'.format(cx+ele[0],cy+ele[1],E_sum))


module.output_gcode('./test_raise_compensation.gcode',gcode)