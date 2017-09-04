# Nagarro-Hackathon

This project was made in uder 24 hours for Hackathon code-n-counter 2.0 hosted by Nagarro on 2nd September 2017, in which our team "Einsteam" made it to top 15 out of 75 teams participating in onsite round from various states of India after qualifying an offline round of more than 4700 teams. 


Inspiration
You go to any street, town, village or city in India, you are sure to find trash everywhere. Cans, plastic, food waste, papers - our streets are filled with all kinds of rubbish and notorious for resembling landfills! In fact, littering i.e. throwing things anywhere except for in the dustbin is a socially acceptable norm! No one even thinks twice before littering.

It is believed that due to our huge population and the problem of illiteracy, it is difficult to put an end to this menace. Agreed, to some extent, it might hold some truth. However, we all have seen even educated people throw garbage on the streets.

The need of the hour is to change our mindset. We Indians are known to keep our houses spick and span, at the same time, have no qualms about making our neighborhood dirty. This mentality needs to be changed.

We wish to do so by providing them incentive for proper disposal of trash by introducing a SmartBin and Reward Point System.

What it does
We propose to install SmartBins at various public places. They should be capable of detect when trash is put into it, which then checks if the type of trash is put into correct kind of bin (Recyclable, Non Recyclable) and provides points to the user if he used the correct bin. The user can then redeem these points for bill payments, charity etc.

How we built it
We used Tensorflow framework in Python to build and train a Convolution Neural Network (CNN) for deciding the kind of trash by computer vision. We trained our model on set of 2700 images (80/20 training/testing ratio) for classifying "cardboard, paper, metal, plastic, glass, other ". Accuracy on Test was approximately 60%. We then used Flask framework to use our machine learning engine as an web service API. For user interface we built an Web based application (usable by mobile devices) using HTML, CSS, Javascript and PHP, which keep track of user's points and provide a system for redeeming points.

Data set used can be found here: link

Challenges we ran into
Implementing the classifier for trash with a significant accuracy was a very tedious process. We tried to implement Visual bag of words algorithm for classification but was unable to do so. Keeping track of which user should be provided points for some particular trash that is put into the bin.

Accomplishments that I'm proud of
We are proud that we were able to submit a demo, after hours of non-stop hardwork. Being able to participate at such a level with so many great teams is also an accomplishment in itself.

What we learned
I learned basics of Flask framework for python and how to use it to build APIs. Various Feature extraction methods for images such as SIFT, SURF etc. Implementing Client-Server networking.

What's next for Cash Your Trash
We wish to build a more attractive and easier-to-use User interface, collect more data for higher accuracy on classification of trash and finally approach Indian Government to execute this plan all over India.
