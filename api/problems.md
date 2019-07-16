**Fit** - we want to allow them to fit the model to data over time -e.g. they continue to hit the API with individual rows and the model progressively updates.

**Predictions** - we will start by only including classifiers, so that predictions are easy - just pass in a row, get back the model's prediction.

**Server** - we need the model to be running on some type of asynchronous python server (**twisted** would be good for this) that accepts new rows to train based off of and can return predictions. The server needs to have some type of cron job system to write the model to a file (say every hour) and a method of rebuilding the server from the file when it goes down.

We start with only config, build a model based off that. The model will be constantly running on a Python server that just responds to /learn and /predict commands. Find a way to keep track of the various docker instances, which user / instances they are connected to in the database, and a way to alert them when new rows are uploaded and predictions need to be made.
