{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Id</th>\n",
       "      <th>Name</th>\n",
       "      <th>Year</th>\n",
       "      <th>Gender</th>\n",
       "      <th>State</th>\n",
       "      <th>Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11349</td>\n",
       "      <td>11350</td>\n",
       "      <td>Emma</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11350</td>\n",
       "      <td>11351</td>\n",
       "      <td>Madison</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11351</td>\n",
       "      <td>11352</td>\n",
       "      <td>Hannah</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11352</td>\n",
       "      <td>11353</td>\n",
       "      <td>Grace</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11353</td>\n",
       "      <td>11354</td>\n",
       "      <td>Emily</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0     Id     Name  Year Gender State  Count\n",
       "0       11349  11350     Emma  2004      F    AK     62\n",
       "1       11350  11351  Madison  2004      F    AK     48\n",
       "2       11351  11352   Hannah  2004      F    AK     46\n",
       "3       11352  11353    Grace  2004      F    AK     44\n",
       "4       11353  11354    Emily  2004      F    AK     41"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "info=pd.read_csv(\"https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv\")\n",
    "info.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Name</th>\n",
       "      <th>Year</th>\n",
       "      <th>Gender</th>\n",
       "      <th>State</th>\n",
       "      <th>Count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11350</td>\n",
       "      <td>Emma</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11351</td>\n",
       "      <td>Madison</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11352</td>\n",
       "      <td>Hannah</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11353</td>\n",
       "      <td>Grace</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11354</td>\n",
       "      <td>Emily</td>\n",
       "      <td>2004</td>\n",
       "      <td>F</td>\n",
       "      <td>AK</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Id     Name  Year Gender State  Count\n",
       "0  11350     Emma  2004      F    AK     62\n",
       "1  11351  Madison  2004      F    AK     48\n",
       "2  11352   Hannah  2004      F    AK     46\n",
       "3  11353    Grace  2004      F    AK     44\n",
       "4  11354    Emily  2004      F    AK     41"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "info.drop(info.loc[:,info.columns.str.contains('Unnamed')],axis=1).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "F    558846\n",
       "M    457549\n",
       "Name: Gender, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "info['Gender'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Riley     1112\n",
       "Avery     1080\n",
       "Jordan    1073\n",
       "Peyton    1064\n",
       "Hayden    1049\n",
       "Name: Name, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "info['Name'].value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "could not convert string to float: 'Waylon'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36mf\u001b[1;34m(values, axis, skipna, **kwds)\u001b[0m\n\u001b[0;32m    127\u001b[0m                 \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 128\u001b[1;33m                     \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0malt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    129\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36mnanmedian\u001b[1;34m(values, axis, skipna)\u001b[0m\n\u001b[0;32m    381\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mis_float_dtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 382\u001b[1;33m         \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'f8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    383\u001b[0m         \u001b[0mvalues\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnan\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'Waylon'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36mf\u001b[1;34m(values, axis, skipna, **kwds)\u001b[0m\n\u001b[0;32m    130\u001b[0m                 \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 131\u001b[1;33m                     \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0malt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    132\u001b[0m                 \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36mnanmedian\u001b[1;34m(values, axis, skipna)\u001b[0m\n\u001b[0;32m    381\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mis_float_dtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 382\u001b[1;33m         \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'f8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    383\u001b[0m         \u001b[0mvalues\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnan\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'Waylon'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-43-91092e281a1c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0minfo\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Name'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmedian\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36mstat_func\u001b[1;34m(self, axis, skipna, level, numeric_only, **kwargs)\u001b[0m\n\u001b[0;32m   7313\u001b[0m                                       skipna=skipna)\n\u001b[0;32m   7314\u001b[0m         return self._reduce(f, name, axis=axis, skipna=skipna,\n\u001b[1;32m-> 7315\u001b[1;33m                             numeric_only=numeric_only)\n\u001b[0m\u001b[0;32m   7316\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   7317\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mset_function_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstat_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcls\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m_reduce\u001b[1;34m(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)\u001b[0m\n\u001b[0;32m   2575\u001b[0m                                           'numeric_only.'.format(name))\n\u001b[0;32m   2576\u001b[0m             \u001b[1;32mwith\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merrstate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mall\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'ignore'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2577\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdelegate\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2578\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2579\u001b[0m         return delegate._reduce(op=op, name=name, axis=axis, skipna=skipna,\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36m_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     75\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     76\u001b[0m                 \u001b[1;32mwith\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merrstate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minvalid\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'ignore'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 77\u001b[1;33m                     \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     78\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mValueError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     79\u001b[0m                 \u001b[1;31m# we want to transform an object array\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\core\\nanops.py\u001b[0m in \u001b[0;36mf\u001b[1;34m(values, axis, skipna, **kwds)\u001b[0m\n\u001b[0;32m    137\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    138\u001b[0m                     \u001b[1;32mif\u001b[0m \u001b[0mis_object_dtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 139\u001b[1;33m                         \u001b[1;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    140\u001b[0m                     \u001b[1;32mraise\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    141\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: could not convert string to float: 'Waylon'"
     ]
    }
   ],
   "source": [
    "info['Name'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender  State\n",
       "F       CA       45144\n",
       "        TX       39760\n",
       "        NY       28158\n",
       "        FL       25781\n",
       "        IL       21268\n",
       "        GA       19385\n",
       "        OH       18143\n",
       "        PA       17480\n",
       "        NC       17357\n",
       "        MI       16038\n",
       "        NJ       15041\n",
       "        VA       14759\n",
       "        AZ       14518\n",
       "        WA       13329\n",
       "        TN       13063\n",
       "        IN       13056\n",
       "        MO       11948\n",
       "        CO       11424\n",
       "        MD       11276\n",
       "        MN       10677\n",
       "        MA       10580\n",
       "        WI       10549\n",
       "        LA       10510\n",
       "        AL        9878\n",
       "        OK        9519\n",
       "        UT        9515\n",
       "        SC        9465\n",
       "        KY        8817\n",
       "        OR        8604\n",
       "        KS        7753\n",
       "                 ...  \n",
       "M       WI        8940\n",
       "        MA        8609\n",
       "        AL        8419\n",
       "        UT        8233\n",
       "        SC        8195\n",
       "        OK        8138\n",
       "        OR        7333\n",
       "        KY        7267\n",
       "        MS        6862\n",
       "        KS        6748\n",
       "        AR        6475\n",
       "        IA        6307\n",
       "        NV        6024\n",
       "        CT        5733\n",
       "        NE        5029\n",
       "        NM        4966\n",
       "        ID        4833\n",
       "        WV        3733\n",
       "        HI        3546\n",
       "        DC        3000\n",
       "        MT        2986\n",
       "        SD        2908\n",
       "        ME        2777\n",
       "        NH        2659\n",
       "        AK        2587\n",
       "        ND        2581\n",
       "        RI        2468\n",
       "        DE        2440\n",
       "        WY        1904\n",
       "        VT        1618\n",
       "Name: State, Length: 102, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "info.groupby('Gender')['State'].value_counts()"
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
