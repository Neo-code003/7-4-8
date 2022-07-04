#!/usr/bin/env python
# coding: utf-8

# In[15]:


from flask import Flask, render_template, request


# In[16]:


app = Flask(__name__)


# In[17]:


import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        model = joblib.load("DBS_Prediction")
        pred = model.predict([[rate]])
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




