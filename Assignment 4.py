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
      "Enter the value of a = 2\n",
      "Enter the value of b = 3\n",
      "Enter the value of c = 4\n",
      "area : 2.9047375096555625\n"
     ]
    }
   ],
   "source": [
    "class Triangle:\n",
    " \n",
    "    def __init__(self,a,b,c):\n",
    "        self.a = float(a)\n",
    "        self.b = float(b)\n",
    "        self.c = float(c)\n",
    " \n",
    "    def area(self):\n",
    "        s=(self.a + self.b + self.c)/2\n",
    "        return((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)\n",
    " \n",
    "a=input(\"Enter the value of a = \")\n",
    "b=input(\"Enter the value of b = \")\n",
    "c=input(\"Enter the value of c = \")\n",
    "t = Triangle(a, b, c)\n",
    "print(\"area : {}\".format(t.area()))"
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
      "Enter words:wqdhqvd,qjwdbqmnkln\n",
      "Enter Min Length:4\n",
      "Words with at least min length: ['wqdhqvd', 'qjwdbqmnkln']\n"
     ]
    }
   ],
   "source": [
    "def filter_long_words(l,a):\n",
    "    words=[]\n",
    "    for j in l:\n",
    "        if(len(j)>=a):\n",
    "            words.append(j)\n",
    "    return words\n",
    "\n",
    "n=input(\"Enter words:\")\n",
    "nt=n.split(\",\")\n",
    "na=input(\"Enter Min Length:\")\n",
    "long=filter_long_words(nt,int(na))\n",
    "\n",
    "print(\"Words with at least min length:\",long)"
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
      "List of words:['wordOne', 'wordTwo', 'wordThree', 'wordFour', 'wordFive']\n",
      "List of wordlength:[7, 7, 9, 8, 8]\n"
     ]
    }
   ],
   "source": [
    "listOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']\n",
    " \n",
    "listOfInts = []\n",
    " \n",
    "for i in range(len(listOfWords)):\n",
    "    listOfInts.append(len(listOfWords[i]))\n",
    " \n",
    "print (\"List of words:\"+str(listOfWords))    \n",
    "print (\"List of wordlength:\"+str(listOfInts))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def char(alphabet):\n",
    "    vowel=('a','e','i','o','u')\n",
    "    return alphabet in vowel\n",
    "print(char('c'))\n",
    "print(char('e'))\n",
    "    \n",
    "    \n",
    "    "
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
