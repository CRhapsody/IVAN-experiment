import os
from pathlib import Path




def ptxt_to_vnnlib(radius,data):

    ptxt_dir = Path('/home/abc/test-marabou/Delta-Marabou/finally_experiment/ex_3/properties/robustness')
    ptxt_path = ptxt_dir / f"advproperty_network_5_2_delta_{radius}_data_{data}.txt"
    with open(ptxt_path, "r") as f:
        ptxt_lines = f.readlines()
        ptxt_lines = [line.strip() for line in ptxt_lines]
        ptxt_lines = [line for line in ptxt_lines if line]
        
    
    

    vnnlib_path = Path(f"5_2_data{data}.vnnlib")

    with open(vnnlib_path, "w+") as f:
        f.write(
            f'; ACAS Xu 5_2 network data {data} at radius {radius}\n'
            '(declare-const X_0 Real)\n'
            '(declare-const X_1 Real)\n'
            '(declare-const X_2 Real)\n'
            '(declare-const X_3 Real)\n'
            '(declare-const X_4 Real)\n'

            '(declare-const Y_0 Real)\n'
            '(declare-const Y_1 Real)\n'
            '(declare-const Y_2 Real)\n'
            '(declare-const Y_3 Real)\n'
            '(declare-const Y_4 Real)\n'

        )

        for i,line in enumerate(ptxt_lines) :
            if i!=len(ptxt_lines)-1:
                index,relation,rangeline = line.split(' ')
        
                f.write(f'(assert ({relation} X_{index[-1]} {rangeline}))\n')
            else:
                larger,smaller,relation,rangeline = line.split(' ')
                f.write(f'(assert (<= Y_{smaller[-1]} Y_{larger[-1]}))\n')

    f.close()   
if __name__ == '__main__':
    ptxt_to_vnnlib(0.12265625,15)
    ptxt_to_vnnlib(0.00703125,18)
    ptxt_to_vnnlib(0.0023437500000000003,19)
    ptxt_to_vnnlib(0.19921875,20)
    ptxt_to_vnnlib(0.16796875,21)
    ptxt_to_vnnlib(0.10234375000000001,22)
    ptxt_to_vnnlib(0.041406250000000006,23)
    ptxt_to_vnnlib(0.07890625000000001,24)
    ptxt_to_vnnlib(0.041406250000000006,25)
    ptxt_to_vnnlib(0.07890625000000001,26)
    ptxt_to_vnnlib(0.14921875,27)
    ptxt_to_vnnlib(0.06953125,28)
    ptxt_to_vnnlib(0.07109375000000001,29)
    ptxt_to_vnnlib(0.08203125000000001,30)
    ptxt_to_vnnlib(0.05390625,31)
    ptxt_to_vnnlib(0.05390625,32)
    ptxt_to_vnnlib(0.00703125,33)
    ptxt_to_vnnlib(0.017968750000000002,34)
    ptxt_to_vnnlib(0.01171875,35)


