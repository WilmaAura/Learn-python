# indent = lekukan
import time, sys
indent = 0
indent_increasing = True # 

try: 
    while True:
        print(' ' * indent, end ='')
        print ('********')
        time.sleep(0.1) # Pause it

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # change direction:
                indent_increasing = False
        else:
        # Decrease the number of spaces:
            indent = indent - 1
            # change direction
            indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
