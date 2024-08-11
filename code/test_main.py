import module
import os
import math

def whole_process(filepath,max_para):
    
    filename=filepath.split('/')[-1].split('.')[0]

    gcode_orig=orig_gcode(filepath,max_para[0],max_para[1],max_para[2])
    module.output_gcode('./test_output/{0}/_orig_{1}_X{2:.5f}_Y{3:.5f}_T{4:.5f}.gcode'.format(filename,filename,max_para[0],max_para[1],max_para[2]),gcode_orig)
    trim_sup,gcode_trim=trim_gcode(filepath,max_para[0],max_para[1],max_para[2])
    module.output_gcode('./test_output/{0}/_trim_{1}_X{2:.5f}_Y{3:.5f}_T{4:.5f}.gcode'.format(filename,filename,max_para[0],max_para[1],max_para[2]),gcode_trim)
    print(trim_sup)
    return None

def orig_gcode(filepath,x_comp,y_comp,t_comp):
    
    gcode=module.get_gcode(filepath)

    gcode_Trans_Detect,_=module.prefix_Translation_HeightDetection(gcode,x_comp=x_comp,y_comp=y_comp,z_comp=0,theta=math.pi/180*t_comp)
    
    # return None if the model out of the range
    if not gcode_Trans_Detect:
        return None
    
    ratio=filepath.split('/')[-1].split('.')[0].split('_')[-1]

    gcode_orig_final=module.suffix_Mark(gcode_Trans_Detect,[ratio,x_comp,y_comp,t_comp])
    
    return gcode_orig_final

def trim_gcode(filepath,x_comp,y_comp,t_comp):

    gcode=module.get_gcode(filepath)

    gcode_Trans_Detect,platform_matrix=module.prefix_Translation_HeightDetection(gcode,x_comp=x_comp,y_comp=y_comp,z_comp=module.z0,theta=math.pi/180*t_comp)
    
    # return None if the model out of the range
    if not gcode_Trans_Detect:
        return None,None
    
    gcode_reset=module.platform_reset(platform_matrix)
    
    gcode_reset.extend(gcode_Trans_Detect)
    
    gcode_Trans_Detect_Trim,total_trim_e=module.prefix_Trim3(gcode_reset,platform_matrix)
 
    gcode_Trans_Detect_Trim_Sep=module.suffix_Separate3(gcode_Trans_Detect_Trim)
    
    ratio=filepath.split('/')[-1].split('.')[0].split('_')[-1]

    gcode_trim_final=module.suffix_Mark(gcode_Trans_Detect_Trim_Sep,[ratio,x_comp,y_comp,t_comp])

    return total_trim_e,gcode_trim_final

def test_loop(filepath,max_loop_times,step):
    def i_to_comp(range,i):
        return range[0]+i*(range[1]-range[0])/step
    
    t_range=[0,90]
    x_range=[-module.lx/2+module.lx*module.nx/2,module.lx/2+module.lx*module.nx/2]
    y_range=[-module.ly/2+module.ly*module.ny/2,module.ly/2+module.ly*module.ny/2]

    max_para=[0,0,0]
    max_e=0
    last_max_e=math.inf

    while max_loop_times>0:
        for t_i in range(step):
            for y_i in range(step):
                for x_i in range(step):
                    x_comp=i_to_comp(x_range,x_i)
                    y_comp=i_to_comp(y_range,y_i)
                    t_comp=i_to_comp(t_range,t_i)
                    print([x_comp,y_comp,t_comp])

                    total_trim_e,gcode_trim=trim_gcode(filepath,x_comp,y_comp,t_comp)
                    if not total_trim_e:
                        continue
                    if total_trim_e>max_e:
                        max_e=total_trim_e
                        max_para=[x_comp,y_comp,t_comp]

                    print("{} mm".format(total_trim_e))
        
        if abs(last_max_e-max_e)>module.err:
            last_max_e=max_e
            whole_process(filepath,max_para)

        else:
            print("Early End")
            break

        x_range=[max_para[0]-(x_range[1]-x_range[0])/step,max_para[0]+(x_range[1]-x_range[0])/step]
        y_range=[max_para[1]-(y_range[1]-y_range[0])/step,max_para[1]+(y_range[1]-y_range[0])/step]
        t_range=[max_para[2]-(t_range[1]-t_range[0])/step,max_para[2]+(t_range[1]-t_range[0])/step]

        max_loop_times=max_loop_times-1
        # step=int(step-1)

    print(max_para)
    print("{:.8f} mm".format(max_e))

    whole_process(filepath,max_para)

    return None

filepath='./gcode_cura/CE3E3V2_bridge_rect_final_14.gcode'
filename=filepath.split('/')[-1].split('.')[0]

CE3E3V2_bridge_rect_final_10=[76.5,41.8,0.0]
CE3E3V2_bridge_rect_final_12=[77.52,78.53999999999999,-9.0]
CE3E3V2_bridge_rect_final_14=[61.2,90.0,0.0]
CE3E3V2_bridge_rect_final_16=[86.7,75.4,9.0]
CE3E3V2_bridge_rect_final_18=[100.98000,77.30000,1.80000]
CE3E3V2_bridge_rect_final_20=[107.1, 96.9, 0.0]
CE3E3V2_bridge_rect_final_22=[107.1, 107.1, 0.0]
CE3E3V2_bridge_rect_final_24=[100.98000,77.30000,1.80000]
_verticle_blade_400_0=[76.5,86.7, 324.0]
_Template_ladder=[51,51,90]
whole_process(filepath,CE3E3V2_bridge_rect_final_14)


'''

# nested for-loop for variable x,y,t

max_loop_times=5
step=8

test_loop(filepath,max_loop_times,step)

# '''