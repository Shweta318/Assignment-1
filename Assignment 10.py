{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Min and max temperature')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "temp_max =np.array ([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])\n",
    "temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])\n",
    "import matplotlib.pyplot as plt\n",
    "months=np.arange(12)\n",
    "plt.plot(months, temp_max, 'ro')\n",
    "plt.plot(months,temp_min, 'bo')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Min and max temperature')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import optimize\n",
    "def yearly_temps(times, avg, ampl, time_offset):\n",
    "    return (avg\n",
    "            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))\n",
    "\n",
    "res_max, cov_max = optimize.curve_fit(yearly_temps, months,\n",
    "                                      temp_max, [20, 10, 0])\n",
    "res_min, cov_min = optimize.curve_fit(yearly_temps, months,\n",
    "                                      temp_min, [-40, 20, 0])\n",
    "\n",
    "from scipy import optimize\n",
    "def yearly_temps(times, avg, ampl, time_offset):\n",
    "    return (avg\n",
    "            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))\n",
    "\n",
    "res_max, cov_max = optimize.curve_fit(yearly_temps, months,\n",
    "                                      temp_max, [20, 10, 0])\n",
    "res_min, cov_min = optimize.curve_fit(yearly_temps, months,\n",
    "                                      temp_min, [-40, 20, 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "days = np.linspace(0, 12, num=365)\n",
    "\n",
    "plt.figure()\n",
    "plt.plot(months, temp_max, 'ro')\n",
    "plt.plot(days, yearly_temps(days, *res_max), 'r-')\n",
    "plt.plot(months, temp_min, 'bo')\n",
    "plt.plot(days, yearly_temps(days, *res_min), 'b-')\n",
    "plt.xlabel('Month')\n",
    "plt.ylabel('Temperature ($^\\circ$C)')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>pclass</th>\n",
       "      <th>survived</th>\n",
       "      <th>name</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>ticket</th>\n",
       "      <th>fare</th>\n",
       "      <th>cabin</th>\n",
       "      <th>embarked</th>\n",
       "      <th>boat</th>\n",
       "      <th>body</th>\n",
       "      <th>home.dest</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Allen, Miss. Elisabeth Walton</td>\n",
       "      <td>female</td>\n",
       "      <td>29.0000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>24160</td>\n",
       "      <td>211.3375</td>\n",
       "      <td>B5</td>\n",
       "      <td>S</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>St Louis, MO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Allison, Master. Hudson Trevor</td>\n",
       "      <td>male</td>\n",
       "      <td>0.9167</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>11</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Miss. Helen Loraine</td>\n",
       "      <td>female</td>\n",
       "      <td>2.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Mr. Hudson Joshua Creighton</td>\n",
       "      <td>male</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135.0</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Mrs. Hudson J C (Bessie Waldo Daniels)</td>\n",
       "      <td>female</td>\n",
       "      <td>25.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   pclass  survived                                             name     sex  \\\n",
       "0     1.0       1.0                    Allen, Miss. Elisabeth Walton  female   \n",
       "1     1.0       1.0                   Allison, Master. Hudson Trevor    male   \n",
       "2     1.0       0.0                     Allison, Miss. Helen Loraine  female   \n",
       "3     1.0       0.0             Allison, Mr. Hudson Joshua Creighton    male   \n",
       "4     1.0       0.0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female   \n",
       "\n",
       "       age  sibsp  parch  ticket      fare    cabin embarked boat   body  \\\n",
       "0  29.0000    0.0    0.0   24160  211.3375       B5        S    2    NaN   \n",
       "1   0.9167    1.0    2.0  113781  151.5500  C22 C26        S   11    NaN   \n",
       "2   2.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "3  30.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN  135.0   \n",
       "4  25.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "\n",
       "                         home.dest  \n",
       "0                     St Louis, MO  \n",
       "1  Montreal, PQ / Chesterville, ON  \n",
       "2  Montreal, PQ / Chesterville, ON  \n",
       "3  Montreal, PQ / Chesterville, ON  \n",
       "4  Montreal, PQ / Chesterville, ON  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "a=pd.read_csv(\"https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv\")\n",
    "a.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male      843\n",
       "female    466\n",
       "Name: sex, dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a['sex'].value_counts()\n",
    "#print(b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "gender= 'male','female'\n",
    "sizes= [843,466]\n",
    "plt.pie(sizes,labels=gender)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
       "      <th>pclass</th>\n",
       "      <th>survived</th>\n",
       "      <th>name</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>ticket</th>\n",
       "      <th>fare</th>\n",
       "      <th>cabin</th>\n",
       "      <th>embarked</th>\n",
       "      <th>boat</th>\n",
       "      <th>body</th>\n",
       "      <th>home.dest</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Allen, Miss. Elisabeth Walton</td>\n",
       "      <td>1.0</td>\n",
       "      <td>29.0000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>24160</td>\n",
       "      <td>211.3375</td>\n",
       "      <td>B5</td>\n",
       "      <td>S</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>St Louis, MO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Allison, Master. Hudson Trevor</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.9167</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>11</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Miss. Helen Loraine</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Mr. Hudson Joshua Creighton</td>\n",
       "      <td>0.0</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135.0</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Allison, Mrs. Hudson J C (Bessie Waldo Daniels)</td>\n",
       "      <td>1.0</td>\n",
       "      <td>25.0000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   pclass  survived                                             name  sex  \\\n",
       "0     1.0       1.0                    Allen, Miss. Elisabeth Walton  1.0   \n",
       "1     1.0       1.0                   Allison, Master. Hudson Trevor  0.0   \n",
       "2     1.0       0.0                     Allison, Miss. Helen Loraine  1.0   \n",
       "3     1.0       0.0             Allison, Mr. Hudson Joshua Creighton  0.0   \n",
       "4     1.0       0.0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  1.0   \n",
       "\n",
       "       age  sibsp  parch  ticket      fare    cabin embarked boat   body  \\\n",
       "0  29.0000    0.0    0.0   24160  211.3375       B5        S    2    NaN   \n",
       "1   0.9167    1.0    2.0  113781  151.5500  C22 C26        S   11    NaN   \n",
       "2   2.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "3  30.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN  135.0   \n",
       "4  25.0000    1.0    2.0  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "\n",
       "                         home.dest  \n",
       "0                     St Louis, MO  \n",
       "1  Montreal, PQ / Chesterville, ON  \n",
       "2  Montreal, PQ / Chesterville, ON  \n",
       "3  Montreal, PQ / Chesterville, ON  \n",
       "4  Montreal, PQ / Chesterville, ON  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "a['sex'].replace('female',1,inplace=True)\n",
    "a['sex'].replace('male',0,inplace=True)\n",
    "a.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x821490>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(a.age,a.fare)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mapping={'male':'blue','female':'red'}\n",
    "plt.scatter(a['age'],a['fare'],s=50,c=a['sex'])\n",
    "plt.show()"
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
