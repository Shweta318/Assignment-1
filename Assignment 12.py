{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "PandaSQLException",
     "evalue": "(sqlite3.OperationalError) near \"sqlite3\": syntax error [SQL: \"sqlite3.connect('sqladb')\"] (Background on this error at: http://sqlalche.me/e/e3q8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, *args)\u001b[0m\n\u001b[0;32m   1192\u001b[0m                         \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1193\u001b[1;33m                         context)\n\u001b[0m\u001b[0;32m   1194\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mdo_execute\u001b[1;34m(self, cursor, statement, parameters, context)\u001b[0m\n\u001b[0;32m    508\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 509\u001b[1;33m         \u001b[0mcursor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    510\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: near \"sqlite3\": syntax error",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandasql\\sqldf.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, query, env)\u001b[0m\n\u001b[0;32m     60\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 61\u001b[1;33m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mread_sql\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     62\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mDatabaseError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mex\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mread_sql\u001b[1;34m(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)\u001b[0m\n\u001b[0;32m    415\u001b[0m             \u001b[0mcoerce_float\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcoerce_float\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparse_dates\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparse_dates\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 416\u001b[1;33m             chunksize=chunksize)\n\u001b[0m\u001b[0;32m    417\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mread_query\u001b[1;34m(self, sql, index_col, coerce_float, parse_dates, params, chunksize)\u001b[0m\n\u001b[0;32m   1091\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1092\u001b[1;33m         \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1093\u001b[0m         \u001b[0mcolumns\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeys\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandas\\io\\sql.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    982\u001b[0m         \u001b[1;34m\"\"\"Simple passthrough to SQLAlchemy connectable\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 983\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnectable\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    984\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, object, *multiparams, **params)\u001b[0m\n\u001b[0;32m    941\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobject\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mutil\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstring_types\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 942\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_execute_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobject\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmultiparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    943\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_text\u001b[1;34m(self, statement, multiparams, params)\u001b[0m\n\u001b[0;32m   1103\u001b[0m             \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1104\u001b[1;33m             \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1105\u001b[0m         )\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, *args)\u001b[0m\n\u001b[0;32m   1199\u001b[0m                 \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1200\u001b[1;33m                 context)\n\u001b[0m\u001b[0;32m   1201\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_handle_dbapi_exception\u001b[1;34m(self, e, statement, parameters, cursor, context)\u001b[0m\n\u001b[0;32m   1412\u001b[0m                     \u001b[0msqlalchemy_exception\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1413\u001b[1;33m                     \u001b[0mexc_info\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1414\u001b[0m                 )\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\util\\compat.py\u001b[0m in \u001b[0;36mraise_from_cause\u001b[1;34m(exception, exc_info)\u001b[0m\n\u001b[0;32m    264\u001b[0m     \u001b[0mcause\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc_value\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mexc_value\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mexception\u001b[0m \u001b[1;32melse\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 265\u001b[1;33m     \u001b[0mreraise\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mexception\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mexc_tb\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcause\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    266\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\util\\compat.py\u001b[0m in \u001b[0;36mreraise\u001b[1;34m(tp, value, tb, cause)\u001b[0m\n\u001b[0;32m    247\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__traceback__\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mtb\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 248\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwith_traceback\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    249\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, *args)\u001b[0m\n\u001b[0;32m   1192\u001b[0m                         \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1193\u001b[1;33m                         context)\n\u001b[0m\u001b[0;32m   1194\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mdo_execute\u001b[1;34m(self, cursor, statement, parameters, context)\u001b[0m\n\u001b[0;32m    508\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 509\u001b[1;33m         \u001b[0mcursor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    510\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: (sqlite3.OperationalError) near \"sqlite3\": syntax error [SQL: \"sqlite3.connect('sqladb')\"] (Background on this error at: http://sqlalche.me/e/e3q8)",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mPandaSQLException\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-26901c546c83>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[0msqladb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0mpysqldf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"\"\"sqlite3.connect('sqladb')\"\"\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m pysqldf(\"\"\"CREATE TABLE adult (\n",
      "\u001b[1;32m<ipython-input-3-26901c546c83>\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(q)\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mpandasql\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msqldf\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mpysqldf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mlambda\u001b[0m \u001b[0mq\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0msqldf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mglobals\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[0msqladb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandasql\\sqldf.py\u001b[0m in \u001b[0;36msqldf\u001b[1;34m(query, env, db_uri)\u001b[0m\n\u001b[0;32m    154\u001b[0m     \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[0msqldf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"select avg(x) from df;\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlocals\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    155\u001b[0m     \"\"\"\n\u001b[1;32m--> 156\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mPandaSQL\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdb_uri\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0menv\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\vyass\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages\\pandasql\\sqldf.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, query, env)\u001b[0m\n\u001b[0;32m     61\u001b[0m                 \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mread_sql\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     62\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mDatabaseError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mex\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 63\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mPandaSQLException\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mex\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     64\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mResourceClosedError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     65\u001b[0m                 \u001b[1;31m# query returns nothing\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mPandaSQLException\u001b[0m: (sqlite3.OperationalError) near \"sqlite3\": syntax error [SQL: \"sqlite3.connect('sqladb')\"] (Background on this error at: http://sqlalche.me/e/e3q8)"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "from pandas import DataFrame, Series\n",
    "\n",
    "from pandasql import sqldf\n",
    "pysqldf = lambda q: sqldf(q, globals())\n",
    "\n",
    "sqladb = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')\n",
    "\n",
    "pysqldf(\"\"\"sqlite3.connect('sqladb')\"\"\")\n",
    "\n",
    "pysqldf(\"\"\"CREATE TABLE adult (\n",
    "            age   int,\n",
    "            workclass   varchar(40),\n",
    "            fnlwgt   int,\n",
    "            education   varchar(40),\n",
    "            education_num   int,\n",
    "            marital_status   varchar(40),\n",
    "            occupation   varchar(20),\n",
    "            relationship   varchar(40),\n",
    "            race   varchar(20),\n",
    "            sex   varchar(10),\n",
    "            capital_gain   int,\n",
    "            capital_loss   int,\n",
    "            hours_per_week   int,\n",
    "            native_country   varchar(50),\n",
    "            label    varchar(10))\"\"\")\n",
    "#question 1\n",
    "pysqldf(\"SELECT * FROM adult LIMIT 10;\")\n",
    "     \n"
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
