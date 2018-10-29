{
 "cells": [
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
       "      <th>Airline</th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>From_To</th>\n",
       "      <th>RecentDelays</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KLM(!)</td>\n",
       "      <td>10045.0</td>\n",
       "      <td>LoNDon_paris</td>\n",
       "      <td>[23, 47]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>&lt;Air France&gt; (12)</td>\n",
       "      <td>NaN</td>\n",
       "      <td>MAdrid_miLAN</td>\n",
       "      <td>[]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>(British Airways. )</td>\n",
       "      <td>10065.0</td>\n",
       "      <td>londON_StockhOlm</td>\n",
       "      <td>[24, 43, 87]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12. Air France</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Budapest_PaRis</td>\n",
       "      <td>[13]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>\"Swiss Air\"</td>\n",
       "      <td>10085.0</td>\n",
       "      <td>Brussels_londOn</td>\n",
       "      <td>[67, 32]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Airline  FlightNumber           From_To  RecentDelays\n",
       "0               KLM(!)       10045.0      LoNDon_paris      [23, 47]\n",
       "1    <Air France> (12)           NaN      MAdrid_miLAN            []\n",
       "2  (British Airways. )       10065.0  londON_StockhOlm  [24, 43, 87]\n",
       "3       12. Air France           NaN    Budapest_PaRis          [13]\n",
       "4          \"Swiss Air\"       10085.0   Brussels_londOn      [67, 32]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',\n",
    "'Budapest_PaRis', 'Brussels_londOn'],\n",
    "'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],\n",
    "'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],\n",
    "'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',\n",
    "'12. Air France', '\"Swiss Air\"']})\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
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
       "      <th>Airline</th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>From_To</th>\n",
       "      <th>RecentDelays</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KLM(!)</td>\n",
       "      <td>10045</td>\n",
       "      <td>LoNDon_paris</td>\n",
       "      <td>[23, 47]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>&lt;Air France&gt; (12)</td>\n",
       "      <td>10055</td>\n",
       "      <td>MAdrid_miLAN</td>\n",
       "      <td>[]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>(British Airways. )</td>\n",
       "      <td>10065</td>\n",
       "      <td>londON_StockhOlm</td>\n",
       "      <td>[24, 43, 87]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12. Air France</td>\n",
       "      <td>10075</td>\n",
       "      <td>Budapest_PaRis</td>\n",
       "      <td>[13]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>\"Swiss Air\"</td>\n",
       "      <td>10085</td>\n",
       "      <td>Brussels_londOn</td>\n",
       "      <td>[67, 32]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Airline  FlightNumber           From_To  RecentDelays\n",
       "0               KLM(!)         10045      LoNDon_paris      [23, 47]\n",
       "1    <Air France> (12)         10055      MAdrid_miLAN            []\n",
       "2  (British Airways. )         10065  londON_StockhOlm  [24, 43, 87]\n",
       "3       12. Air France         10075    Budapest_PaRis          [13]\n",
       "4          \"Swiss Air\"         10085   Brussels_londOn      [67, 32]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          0          1\n",
      "0    LoNDon      paris\n",
      "1    MAdrid      miLAN\n",
      "2    londON  StockhOlm\n",
      "3  Budapest      PaRis\n",
      "4  Brussels     londOn\n"
     ]
    }
   ],
   "source": [
    "print (df.From_To.str.split(\"_\",expand=True))"
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
      "0        London_Paris\n",
      "1        Madrid_Milan\n",
      "2    London_Stockholm\n",
      "3      Budapest_Paris\n",
      "4     Brussels_London\n",
      "Name: From_To, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print (df.From_To.str.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
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
       "      <th>Airline</th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>RecentDelays</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>KLM(!)</td>\n",
       "      <td>10045</td>\n",
       "      <td>[23, 47]</td>\n",
       "      <td>London_Paris</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>&lt;Air France&gt; (12)</td>\n",
       "      <td>10055</td>\n",
       "      <td>[]</td>\n",
       "      <td>Madrid_Milan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>(British Airways. )</td>\n",
       "      <td>10065</td>\n",
       "      <td>[24, 43, 87]</td>\n",
       "      <td>London_Stockholm</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12. Air France</td>\n",
       "      <td>10075</td>\n",
       "      <td>[13]</td>\n",
       "      <td>Budapest_Paris</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>\"Swiss Air\"</td>\n",
       "      <td>10085</td>\n",
       "      <td>[67, 32]</td>\n",
       "      <td>Brussels_London</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Airline  FlightNumber  RecentDelays               new\n",
       "0               KLM(!)         10045      [23, 47]      London_Paris\n",
       "1    <Air France> (12)         10055            []      Madrid_Milan\n",
       "2  (British Airways. )         10065  [24, 43, 87]  London_Stockholm\n",
       "3       12. Air France         10075          [13]    Budapest_Paris\n",
       "4          \"Swiss Air\"         10085      [67, 32]   Brussels_London"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
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
       "      <th>RecentDelay1</th>\n",
       "      <th>RecentDelay2</th>\n",
       "      <th>RecentDelay3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>23.0</td>\n",
       "      <td>47.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>24.0</td>\n",
       "      <td>43.0</td>\n",
       "      <td>87.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>67.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RecentDelay1  RecentDelay2  RecentDelay3\n",
       "0          23.0          47.0           NaN\n",
       "1           NaN           NaN           NaN\n",
       "2          24.0          43.0          87.0\n",
       "3          13.0           NaN           NaN\n",
       "4          67.0          32.0           NaN"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = (pd.DataFrame(df.pop('RecentDelays').values.tolist(), index=df.index)\n",
    "        .rename(columns = lambda x: 'RecentDelay{}'.format(x+1)))\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
