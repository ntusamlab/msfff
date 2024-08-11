import serial
import time
import module

# ser: 3d printer
ser = serial.Serial('COM19', 115200)
time.sleep(1)
# serA: arduino
serA=serial.Serial('COM20',9600)
time.sleep(1)

print(str(ser.read_all()))
module.serWrite(ser,'M20')
file_name=""
while True:
    res=ser.readline().decode('big5')
    print(res,end="")
    if ".GCO" in res:
        file_name=res.split(" ")
        break

module.serWrite(ser,'M23 /'+file_name[0])

module.serWrite(ser,'M24')

t1=time.time()
t1_fill=0
sum_t_fill=0
t0_pause=0
sum_t_pause=0
parameters=0
total_time=0

while True:
    try:
        res=ser.readline().decode('big5')
        print(res,end="")
        if "time_start" in res:
            t1=time.time()
        if "time_end" in res:
            total_time=float(time.time()-t1-sum_t_pause)
            sum_t_fill=float(sum_t_fill)
            print(total_time)
            print(total_time-sum_t_fill)
            break
        if "time_fill_start" in res:
            t1_fill=time.time()
        if "time_fill_end" in res:
            sum_t_fill=sum_t_fill+time.time()-t1_fill
        if "pause1" in res:
            t0_pause=time.time()
        if "pause2" in res:
            sum_t_pause=sum_t_pause+time.time()-t0_pause
            
        if "down" in res:
            serA.write(b'down\n')
            time.sleep(1)
        if "up" in res:
            serA.write(b'up\n')
            time.sleep(1)
        if "parameter" in res:
            parameters=res.split('_')[1:]
        print("time pass:{0}s".format(float(time.time()-t1-sum_t_pause)))
        print("sup time pass:{0}s".format(float(time.time()-t1-sum_t_fill-sum_t_pause)))

    except:
        print("disconnect")
        time.sleep(1)
        try:
            ser = serial.Serial('COM19', 115200)
            serA=serial.Serial('COM20',9600)
        except:
            pass

if total_time != 0:
    if 'ORIG' in file_name[0]:
        module.output_excel('test_table.xlsx',parameters,'F{0},G{1}'.format(total_time,total_time-sum_t_fill))
    else:
        module.output_excel('test_table.xlsx',parameters,'H{0},I{1}'.format(total_time,total_time-sum_t_fill))

ser.close()
