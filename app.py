#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
import openai
openai.api_key="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"

app=Flask(_name_)
@app.route("/",methods["GET","POST"])
def index()
    if request.method=="POST":
        q=request.from.get("question")
        r=openai.ChatCompletion.create( 
    model="gpt-3.5-turbo", 
    messages=[
        {
            "role": "user",
            
            "content": q
        }
    ]
   
)
        return(render_template("index.html",result=r["choices"][0]["message"]["content"]))
    else:
        return(render_template("index.html",result="waiting"))
if__name__=="__main__":
    app.run()


# In[ ]:




