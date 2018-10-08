{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Incorrect division number\n"
     ]
    }
   ],
   "source": [
    "def exceptions(x,y):\n",
    "    try:\n",
    "        result = x%y\n",
    "        print(\"answer is\",result)\n",
    "    except ZeroDivisionError:\n",
    "        print(\"Incorrect division number\")\n",
    "exceptions(3,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Americans  play Baseball\n",
      "Americans  play Cricket\n",
      "Americans  watch Baseball\n",
      "Americans  watch Cricket\n",
      "Indians play Baseball\n",
      "Indians play Cricket\n",
      "Indians watch Baseball\n",
      "Indians watch Cricket\n"
     ]
    }
   ],
   "source": [
    "subject=[\"Americans \",\"Indians\"]\n",
    "verb=[\"play\",\"watch\"]\n",
    "object=[\"Baseball\",\"Cricket\"]\n",
    "sentence_list = [(sub+\" \"+ vb + \" \" + ob) for sub in subject for vb in verb for ob in object]\n",
    "for sentence in sentence_list:\n",
    " print (sentence)"
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
