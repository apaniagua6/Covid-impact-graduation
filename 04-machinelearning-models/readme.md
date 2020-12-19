# Machine Learning models

Based on the data we have. 
https://datasetteplugins.herokuapp.com/district_data_sample

And the insights we gathered from our dashboards can we create a framework to explore various machine learning techniques on this data set? 

Maybe we can create our own extended cases (for machine learning!)

# Preface

We can use a common repeatable frame-work in order to create these models. 

https://www.educative.io/courses/grokking-the-machine-learning-interview/m2NPGEPwkqn


# Idea Exploration 

Here are various ideas on what we can do with our datasets as it pertains to classical and regression models. 

The general idea, required data, risks, model selection flow and use-case will be described in detail before writing any code. This will enforce proper mental models and encourage academic rigor in our conclusions. 

## How accurately can we classify schools based on their reading and math outcome? 

The researcher will anchor this question using classification techniques. At the end the researching will have a [p-value](https://en.wikipedia.org/wiki/P-value) that they will want to improve and use various techniques to make it happen.  

https://machinelearningmastery.com/types-of-classification-in-machine-learning/

1. Get the labeled data at the per school level. Provides insights on scores per school. I guess we can also, label the data at a per race - some data manipulation will be required but this is doable. 

2. We will make a decision how to split the data into "good grades" vs "bad grades" 

3. Once we have labeled data we will decided on what accuracy metric to use. P-value, Root Mean square error etc.

4. We can now choose a model and start trying different features. 

5. At the end we will have a model that we will be able to input the features and it will provide to us a label such as good grade vs bad grade school. How we use this model will be interesting. We can find the optimal parameters for a particular school, maybe there is a cap on the ROI for instructional spend or adding more teachers will significantly boost the scores(or maybe not). Based on this model we can identify at risk schools in real time and send them an email with our finding and proposed recommendations. The risk is that the model overfitted on our data-set. We have to be careful on using latitude and longtitude coordinates or some other inputs that map a school accurately thus not allowing us to generalize our model to other places in the USA. Furthermore, we might want to create different models for different regions in the USA, puerto rico and Alaska might not fit well into a model that was based on historical data from the USA. 



# Can we predict high school dropout rate?

Adding this as a place-holder since this was our original question. 

