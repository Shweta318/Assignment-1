{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n",
      "*****\n",
      "****\n",
      "***\n",
      "**\n",
      "*\n"
     ]
    }
   ],
   "source": [
    "for i in range (1,6):\n",
    "    for j in range (1,i+1):\n",
    "        print (\"*\",end='')\n",
    "    print()\n",
    "for i in range (1,6):\n",
    "    for k in range (6-i):\n",
    "           \n",
    "        print (\"*\",end='')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dligdacA\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print('Acadgild'[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input some comma seprated numbers : 3,4,5,6\n",
      "List :  ['3', '4', '5', '6']\n"
     ]
    }
   ],
   "source": [
    "values = input(\"Input some comma seprated numbers : \")\n",
    "list = values.split(\",\")\n",
    "\n",
    "print('List : ',list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
