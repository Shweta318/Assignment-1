{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  3,   5,   7,   2,   8,  10,  11,  65,  72,  81,  99, 100, 150])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=(3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150)\n",
    "np.array(a)\n",
    "\n",
    "    \n",
    "    \n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  5.           4.66666667   5.66666667   6.66666667   9.66666667\n",
      "  28.66666667  49.33333333  72.66666667  84.          93.33333333\n",
      " 116.33333333]\n"
     ]
    }
   ],
   "source": [
    "def movingaverage(values,window):\n",
    "    b=np.repeat(1.0,window)/window\n",
    "    c=np.convolve(values,b,'valid')\n",
    "    return c\n",
    "print(movingaverage(a,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
