import serial
import time
import module
import matplotlib.pyplot as plt
import math
import os
import openpyxl
import cv2

# cv2.imread("")

# filename="./test_output/1/2pre_THT_suf_S_2_X2_Y3_T4.gcode"
# filepath='/'.join(filename.split('/')[:-1])
# print(filepath)
# print(os.path.isdir(filepath))
# os.makedirs(filepath)


# a=[50.43134, 131.26308]
# b=[35.4762, 36.84007]

# p_list=module.line_cross2(a,b)
# # p_list.append(a)
# print(p_list)

# plt.scatter([ele[0] for ele in p_list],[ele[1] for ele in p_list])
# plt.show()
# module.output_excel('test_table.xlsx',[10,76.5,91.8,0],'F20,G30')

# nx=module.nx
# ny=module.ny
# ly=module.ly
# lx=module.lx
# gcode_raise=module.gcode_raise
# z_init=103
# z_target=module.z0

# gcode_reset=['G28',
#                 'G92 E0',
#                 'G0 Z120',
#                 "G0 F9000 X{0:.5f} Y{1:.5f} Z{2:.5f}".format(int(nx/2)*lx,int(ny/2)*ly,z_init+3),
#                 'M0']

# for i in range(nx):
#     for j in range(ny):
#         gcode_reset.extend(gcode_raise([(i+0.5)*lx,(j+0.5)*ly,z_init],z_target))

# module.output_gcode('test_reset_all.gcode',gcode_reset)

# a=105
# l=50
# print(math.floor(a/l))

# book = openpyxl.load_workbook('test_table.xlsx')

# sheet = book.active

# a1 = sheet['A11']
# a2 = sheet['A22']
# a3 = sheet.cell(row=3, column=1)

# a3.value='A3'
# sheet.append((1,2,3))

# book.save('test_table.xlsx')

# gcode=module.get_gcode('./gcode_cura/CE3PRO_bridge_rect_10_60_5.gcode')

# new_gcode=module.suffix_Mark(gcode)

# module.output_gcode('test_time.gcode',new_gcode)

serA=serial.Serial('COM20',9600)
time.sleep(3)
while True:
    print("down")
    serA.write(b'down\n')
    time.sleep(2)
    print("up")
    serA.write(b'up\n')
    time.sleep(2)

# G0 F9000 X33.23597 Y51.00000
# G1 F1500 X30.14071 Y47.90474 E1.43497

# filepath='./test_file'
# filename='/a.txt'

# try:
#     os.makedirs(filepath)
# except:
#     pass

# with open(filepath+filename, 'w') as f_gcode:
#     f_gcode.write("3"+"\n")


# print(0)