{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199\n"
     ]
    }
   ],
   "source": [
    "l=[]\n",
    "def num(a,b):\n",
    "    for i in range (a,b):\n",
    "        if i % 7==0 and i % 5 !=0:  \n",
    "            l.append(str(i))\n",
    "    print (','.join(l))\n",
    "num (2000,3201)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First Name:Shweta\n",
      "f_name: Shweta\n",
      "enter your last name:Vyas\n",
      "L_name: Vyas\n",
      "Vyas Shweta\n"
     ]
    }
   ],
   "source": [
    "f_name= input (\"First Name:\")\n",
    "print (\"f_name:\",f_name)\n",
    "L_name= input (\"enter your last name:\")\n",
    "print (\"L_name:\",L_name)\n",
    "x=f_name,L_name\n",
    "print (L_name,f_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "904.3199999999998 cm³\n"
     ]
    }
   ],
   "source": [
    "d= 12\n",
    "r= d/2\n",
    "vol= 4/3*3.14*r*r*r\n",
    "print (vol,\"cm³\")"
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
