{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The return from the portfolio is: 16.67\n"
     ]
    }
   ],
   "source": [
    "# Assign various values\n",
    "MV0 = 100000\n",
    "MVt = 200000\n",
    "CF0 = 50000\n",
    "CFt = 25000\n",
    "\n",
    "# Calculate portfolio return\n",
    "Rt = ((MVt - CFt) - (MV0 + CF0)) / (MV0 + CF0)\n",
    "\n",
    "print('The return from the portfolio is:', round(Rt*100, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The TWRR for the portfolio is (in %age):  27.22\n"
     ]
    }
   ],
   "source": [
    "# Define the market value and cashflow lists\n",
    "MV = [100000, 110000, 120000, 125000, 140000]\n",
    "CF = [[0, 0], [5000, 0], [0, 0], [0, 7000]]\n",
    "\n",
    "# Compute returns from each period\n",
    "ret = [0, 0, 0, 0]\n",
    "\n",
    "for i in range(len(MV)-1):\n",
    "    ret[i] = ((MV[i+1]-CF[i][1])-(MV[i]+CF[i][0]))/(MV[i]+CF[i][0])\n",
    "\n",
    "TWRR = 1\n",
    "\n",
    "for i in range(len(ret)):\n",
    "    TWRR = TWRR*(1+ret[i])\n",
    "\n",
    "TWRR = TWRR-1\n",
    "\n",
    "print('The TWRR for the portfolio is (in %age): ', round(TWRR*100, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The MWRR for the portfolio is (in %age):  24.65\n"
     ]
    }
   ],
   "source": [
    "# Import library\n",
    "import numpy as np\n",
    "\n",
    "# Compute MWRR of the portfolio is same as computing IRR of the below list\n",
    "IRR_list = [-100000,-5000,0,0,-7000+140000]\n",
    "\n",
    "# Calculate IRR\n",
    "IRR_quarterly = np.irr(IRR_list)\n",
    "IRR_yearly = 4*IRR_quarterly\n",
    "\n",
    "print ('The MWRR for the portfolio is (in %age): ', round(IRR_yearly*100,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum of portfolio weights is:  100\n",
      "The sum of benchmark weights is:  100\n",
      "The return from the portfolio is:  1.34\n",
      "The return from the benchmark is:  0.56\n",
      "The active return is:  0.78\n",
      "The pure selection return is:  0.05\n",
      "The selection interaction return is:  -0.08\n",
      "The within-sector selection return is:  0.81\n",
      "The total active return from the components is:  0.78\n"
     ]
    }
   ],
   "source": [
    "# Define the weights and returns of all sectors in portfolio and benchmark\n",
    "port_weights = [6.77, 8.52, 36.22, 5.24, 18.53, 14.46, 10.26]\n",
    "bench_weights = [6.45, 8.99, 37.36, 4.65, 16.56, 18.87, 7.12]\n",
    "port_returns = [-0.82, -3.28, 1.96, 0.44, 2.98, 2.32, 0.54]\n",
    "bench_returns = [-0.73, -4.34, 1.98, 0.24, 2.22, -0.48, -0.42]\n",
    "\n",
    "# Calculate and print the sum of weights of sector in portfolio\n",
    "sum_port_weights = 0\n",
    "for i in range(len(port_weights)):\n",
    "    sum_port_weights += port_weights[i]\n",
    "\n",
    "print('The sum of portfolio weights is: ', round(sum_port_weights))\n",
    "\n",
    "# Calculate and printing the sum of weights of sector in benchmark\n",
    "sum_bench_weights = 0\n",
    "for i in range(len(bench_weights)):\n",
    "    sum_bench_weights += bench_weights[i]\n",
    "\n",
    "print('The sum of benchmark weights is: ', round(sum_bench_weights))\n",
    "\n",
    "# Calculate and print the return from the portfolio\n",
    "ret_port = 0\n",
    "for i in range(len(port_returns)):\n",
    "    ret_port += port_weights[i]*port_returns[i]/sum_port_weights\n",
    "\n",
    "print('The return from the portfolio is: ', round(ret_port, 2))\n",
    "\n",
    "# Calculate and print the return from the benchmark\n",
    "ret_bench = 0\n",
    "for i in range(len(bench_returns)):\n",
    "    ret_bench += bench_weights[i]*bench_returns[i]/sum_bench_weights\n",
    "\n",
    "print('The return from the benchmark is: ', round(ret_bench, 2))\n",
    "\n",
    "# Calculat active return from the portfolio\n",
    "ret_active = ret_port - ret_bench\n",
    "print('The active return is: ', round(ret_active, 2))\n",
    "\n",
    "# Calculating pure sector return\n",
    "pure_sec_ret = 0\n",
    "for i in range(len(port_weights)):\n",
    "    pure_sec_ret += (port_weights[i]-bench_weights[i]) * \\\n",
    "        (bench_returns[i]-ret_bench)/sum_port_weights\n",
    "\n",
    "print('The pure selection return is: ', round(pure_sec_ret, 2))\n",
    "\n",
    "# Calculate selection interaction return\n",
    "sel_int_ret = 0\n",
    "for i in range(len(port_weights)):\n",
    "    sel_int_ret += (port_weights[i]-bench_weights[i]) * \\\n",
    "        (port_returns[i]-bench_returns[i])/sum_port_weights\n",
    "\n",
    "print('The selection interaction return is: ', round(sel_int_ret, 2))\n",
    "\n",
    "# Calculate within-sector selection return\n",
    "wit_sec_ret = 0\n",
    "for i in range(len(port_weights)):\n",
    "    wit_sec_ret += bench_weights[i] * \\\n",
    "        (port_returns[i]-bench_returns[i])/sum_port_weights\n",
    "    \n",
    "print('The within-sector selection return is: ', round(wit_sec_ret, 2))\n",
    "\n",
    "# Sum up all the components\n",
    "ret_active_2 = pure_sec_ret + sel_int_ret + wit_sec_ret\n",
    "print('The total active return from the components is: ', round(ret_active_2, 2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
