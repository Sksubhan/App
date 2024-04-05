import streamlit as st
import time as ts
from datetime import time
head1=st.write("# :upside_down_face: A Small App for timer using Streamlit :slightly_smiling_face:")
timer=st.time_input("Set Timer:", value=time(0,0,0))#Default value of time 
lists=[":clock1",":clock3",":clock5"]
def converting(value):
    minutes,secs,millisecs=value.split(":")
    total_seconds=int(minutes)*60+int(secs)+int(millisecs)/1000
    return total_seconds
if str(timer)=="00:00:00":
    st.write("# Start Timer :clock1: :clock2: :clock3: :clock4:")
else:
    sec=converting(str(timer))
    bar=st.progress(0)
    sec=sec/100
    time_print=st.empty()
    for i in range(100):
        bar.progress(i+1)
        ts.sleep(sec)
        if i<10:
            time_print.write(str(i+1)+" % completed "+":new_moon:")
        elif 10<i<20:
            time_print.write(str(i+1)+" % completed "+":waxing_crescent_moon:")
        elif 20<i<30:
            time_print.write(str(i+1)+" % completed "+":first_quarter_moon:")
        elif 30<i<40:
            time_print.write(str(i+1)+" % completed "+":moon:")
        elif 40<i<50:
            time_print.write(str(i+1)+" % completed "+":waxing_gibbous_moon:")
        elif 50<i<60:
            time_print.write(str(i+1)+" % completed "+":full_moon:")
        elif 60<i<70:
            time_print.write(str(i+1)+" % completed "+":waning_gibbous_moon:")
        elif 70<i<80:
            time_print.write(str(i+1)+" % completed "+":last_quarter_moon:")
        elif 80<i<90:
            time_print.write(str(i+1)+" % completed "+":waning_crescent_moon:")
        elif 90<i<99:
            time_print.write(str(i+1)+" % completed "+":full_moon_with_face:")
        elif i==99:
            st.write("# Timer stopped :raised_back_of_hand:")
st.success("done")